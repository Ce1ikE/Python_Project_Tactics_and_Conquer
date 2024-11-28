import pygame
import pygame_gui
import sys
from classes.ClassUnit import Unit
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu
from classes.ClassHUD import HUD
from classes.ClassMap import Map
from classes.ClassPlayer import Player
from classes.ClassCursor import Cursor
from data.Configuration import *

# indien je niet weet hoe pygame werkt (goeie introductie van het concept):
# https://www.codewithc.com/how-to-make-a-turn-based-strategy-game-in-pygame-%F0%9F%8E%B2/

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("tactics & Conquer")
        # !!! eerst de display initialiseren anders krijg je problemen met de UIManager's thema files
        self.ui_window = pygame.display.set_mode((WIN_X_PX,WIN_Y_PX),pygame.RESIZABLE)
        # "Menu" wordt getekent door "pygame_gui" dus moeten we een UIManager object doorgeven zodat we op het juiste vlak tekenen
        self.menu_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),"./data/theme.json")
        self.menu = Menu(self.menu_ui_manager)
        # zelfde geld voor de HUD
        self.player_hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),"./data/Tactics_and_conquers_style.json")
        self.unit_hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),"./data/Tactics_and_conquers_style.json")
        self.hud = HUD(self.player_hud_ui_manager,self.unit_hud_ui_manager)

        # De cursor houd bij waar de player iets selecteerd om zo makelijker de player te controleren
        self.cursor = Cursor(0,0)
        # De Game State houdt bij in welke modus we zijn van de game om zo makkelijker de game en het menu verdeelt te houden
        self.game_state = MENU # => Ander waarden : PLAYING
        # Eens de player een map heeft aangemaakt moeten we wel zeker zijn of deze wel aangemaakt is
        self.map_state = 0
        # In de game houden we bij welke deel van de map moet geprojecteerd worden op het scherm ("ui_window")
        self.camera = [0,0]
        # we maaken ook een list voor de players om zo als de "end_turn" in de HUD 
        # wordt ingedrukt dat de acties van de speler die worden uitgevoerd alleen 
        # voor die speciefieke speler worden uitgevoerd
        self.players = [Player(x) for x in range(N_PLAYERS) ]
        self.player_turn = 0
        self.players[0].addUnit(INFANTRY,5,5)

    def createMap(self):
        # wave grid (2D) array
        grid = Grid(WORLD_X, WORLD_Y,self.ui_window)
        while self.map_state == 0:
            # see => https://paulmerrell.org/wp-content/uploads/2021/06/thesis.pdf
            result = grid.collapse_wave_function()
            if result == False:
                self.map_state = 1
                # Hier kopieeren we een "Map" object dat in het "Grid" object werdt aangemaakt 
                # naar een ander "Map" object om zo alleen essentiele dingen bij te houden
                self.map =  grid.copy_map()   
            elif result == -1:
                # eens het resultaat "-1" is betekent dat het algorithme een fout heeft gevonden 
                # => een "TILE_BLANK" is weg geschreven naar een "Cell" object
                # daarom vernietigen we het grid
                # see => https://gamedev.stackexchange.com/questions/178443/resolving-contradictions-in-wfc-more-efficiently-than-naive-backtracking

                # i quote : "In an old implementation of WFC I used to rebuild the possibility space around a contradiction. 
                # But I don't think that solution is good in most cases. You can't know when the seeds of the contradiction 
                # were sowed. Its usually faster to reset the whole thing."
                self.map_state = 0 
                del grid
                grid = Grid(WORLD_X, WORLD_Y,self.ui_window)

        # once the map created i need to also copy the player buildings
        for player_n,player_HQ in grid.copy_playersHQ().items():
            self.players[player_n].addBuilding(player_HQ[2],player_HQ[0],player_HQ[1])

    def run(self):
        # de "run" functie runt de game
        while True:
             # Set framerate to max 40/s
            time_delta = self.clock.tick(FPS)/1000.0

            # Er zijn 2 fases in de game loop
            # (1) de "event" fase
            # waarin we checken of er iets gebeurt is of iets zoals een knop die wordt ingedrukt
            # deze fase wordt nog eens in 3 gesplitst afhankelijk van de "game_state" :
            # (1.1) de PLAYING state
            # is actief wanneer er een nieuwe map is aangemaakt of de speler terug vanuit een menu naar de map gaat
            # (1.2) de MENU state
            # is actief eens in-game menu wordt geopent wanneer de game opstart wordt deze automatisch geopent
            # (1.3) de HUD_MENU state
            # is actief eens er in de PLAYING state een object "Unit" wordt geselecteerd. Deze fase wordt zelf afgesplist in 3 fases
            # (1.3.1) de ATTACK_MODE
            # 
            # (1.3.2) de MOVE_MODE
            # 
            # (1.3.3) de DEFENSE_MODE
            #

            # (2) de "draw" fase
            # waarin we alle layers in volgorde gaan tekenen dus bv.: 1->map 2->characters 3->HUD
            # deze wordt net als de "event" fase in 3 gesplitst afhankelijk van de "game_state"

            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (1) EVENT FASE ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # Game events zoals "pygame_gui.UI_BUTTON_PRESSED" of "pygame.KEY_D"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif self.game_state == MENU:
                    result = self.menu.handleMenuEvents(event)
                    if result == PLAYING:
                        if self.map_state == 0:
                            self.createMap()
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")
                    elif result == QUIT:
                        pygame.quit()
                        sys.exit()
                    self.menu_ui_manager.process_events(event)

            # -----------------------------------------------------------------------------------------------

                elif self.game_state == PLAYING:
                    result = self.hud.handlePlayerHUDEvents(event)
                    if result == PLAYING:
                        self.players[self.player_turn].endTurn(True)
                        self.player_turn = (self.player_turn + 1) % N_PLAYERS # of course i can't go out of bounds so modulo by the number of players
                        print(f"next turn => current player " + self.player_turn)
                    elif result == MENU:
                        self.game_state = MENU
                        print(f"changed to MENU state")

                    if event.type == pygame.KEYDOWN:
                        self.camera = self.cursor.UpdatePosition(event,self.camera[0],self.camera[1])
                        if event.key == pygame.K_RETURN:
                            result = self.players[self.player_turn].playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]] 
                            if result != False:
                                # We select the right unit by :
                                # 1) selecting the right "player" object within the list "players", the "player_turn" variable will tell us which player's turn it is
                                # 2) inside this "player" object i have created a map that holds all Unit ID's (Indexes)
                                self.currentSelectedUnit = self.players[self.player_turn].unitsPlayerList[result - 1]
                                self.hud.setHUDPanels(self.cursor.X,self.cursor.Y)
                                self.game_state = HUD_MENU
                                print(f"changed to HUD_MENU state")
                            elif result == False:
                                self.game_state = PLAYING
                                print(f"changed to PLAYING state")
                        self.player_hud_ui_manager.process_events(event)

            # -----------------------------------------------------------------------------------------------

                elif self.game_state == HUD_MENU:
                    result = self.hud.handleUnitHUDEvents(event)
                    if result == PLAYING:
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")
                    elif result == ATTACK_MODE:
                        print(f"changed to ATTACK mode")
                        self.ZoneCoord = self.currentSelectedUnit.getAttackZone()
                        # self.game_state = ATTACK_MODE
                        pass
                    elif result == MOVE_MODE:
                        print(f"changed to MOVE mode")
                        self.ZoneCoord = self.currentSelectedUnit.getTravelZone()
                        # self.game_state = MOVE_MODE
                        pass
                    elif result == DEFEND_MODE:
                        print(f"changed to DEFEND mode")
                        pass
                    self.unit_hud_ui_manager.process_events(event)

            # -----------------------------------------------------------------------------------------------

                # elif self.game_state == ATTACK_MODE:
                    # if event.type == pygame.KEYDOWN:
                    #     self.camera = self.cursor.setPosition(event,self.camera[0],self.camera[1],self.ZoneCoord)

            # -----------------------------------------------------------------------------------------------


            # -----------------------------------------------------------------------------------------------

                    
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (2) DRAW FASE /////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if self.game_state == MENU:
                self.menu.mainMenu(self.ui_window)
                self.menu_ui_manager.update(time_delta)

            # -----------------------------------------------------------------------------------------------

            elif self.game_state == PLAYING:
                self.map.drawMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                result = self.players[self.player_turn].playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                if result != False:
                    self.players[self.player_turn].unitsPlayerList[result - 1].showUnitsDetails(self.ui_window)
                self.cursor.drawCursor(self.ui_window)
                self.hud.drawPlayerHUD(self.ui_window)
                self.player_hud_ui_manager.update(time_delta)

            elif self.game_state == HUD_MENU:
                self.map.drawHUDMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                self.cursor.drawCursor(self.ui_window)
                self.hud.drawUnitHUD(self.ui_window)
                self.unit_hud_ui_manager.update(time_delta)

            elif self.game_state == ATTACK_MODE:
                self.map.drawMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                self.currentSelectedUnit.showAttackZone()
                self.cursor.drawCursor(self.ui_window)
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            
            pygame.display.update()


