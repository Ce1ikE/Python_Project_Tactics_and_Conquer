import pygame
import pygame_gui
import sys
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu
from classes.ClassHUD import HUD
from classes.ClassMap import Map
from classes.ClassPlayer import Player
from classes.ClassCursor import Cursor
from data.Configuration import *

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("tactics & Conquer")
        # !!! eerst de display initialiseren anders krijg je problemen met de UIManager's thema files
        self.ui_window = pygame.display.set_mode((WIN_X_PX,WIN_Y_PX))
        # "Menu" wordt getekent door "pygame_gui" dus moeten we een UIManager object doorgeven zodat we op het juiste vlak tekenen
        self.menu_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),"./data/theme.json")
        self.menu = Menu(self.menu_ui_manager)
        # zelfde geld voor de HUD
        self.hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),"./data/theme.json")
        self.hud = HUD(self.hud_ui_manager)

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
        self.players = [ Player(x) for x in range(N_PLAYERS) ]
        self.player_turn = 0

    def createMap(self):
        # wave grid (2D) array
        grid = Grid(WORLD_X, WORLD_Y,self.ui_window)
        self.map_state = 0 
        while self.map_state == 0:
            result = grid.collapse_wave_function()
            if result == False:
                self.map_state = 1
                # Hier kopieeren we een "Map" object dat in het "Grid" object werdt aangemaakt 
                # naar een ander "Map" object om zo alleen essentiele dingen bij te houden
                self.map =  grid.copy_map()     

    def run(self):
        # de "run" functie runt de game
        while True:
             # Set framerate to max 40/s
            time_delta = self.clock.tick(40)/1000.0

            # Er zijn 2 fases in de game loop
            # (1) de "event" fase
            # waarin we checken of er iets gebeurt of niet zoals een knop die wordt ingedrukt
            # deze fase wordt nog eens in 2 gesplitst afhankelijk van de "game_state"

            # (2) de "draw" fase
            # waarin we alle layers in volgorde gaan tekenen dus bv.: 1) map 2) characters 3) HUD
            # deze wordt net als de "event" fase in 2 gesplitst afhankelijk van de "game_state"

            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (1) EVENT FASE ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # Game events zoals "pygame_gui.UI_BUTTON_PRESSED" of "pygame.KEY_D"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.game_state == MENU:
                    result = self.menu.handleMenuEvents(event)
                    if result == PLAYING:
                        self.game_state = PLAYING
                    elif result == QUIT:
                        pygame.quit()
                        sys.exit()
                    self.menu_ui_manager.process_events(event)

            # -----------------------------------------------------------------------------------------------

                if self.game_state == PLAYING:
                    result = self.hud.handleHUDEvents(event)
                    if result == PLAYING:
                        self.players[self.player_turn].endTurn()
                        self.player_turn += 1
                        self.player_turn = (self.player_turn) % N_PLAYERS
                    elif result == MENU:
                        self.game_state = MENU

                    if event.type == pygame.KEYDOWN:
                       self.camera = self.cursor.UpdatePosition(event,self.camera[0],self.camera[1])
                    elif event.type == pygame.K_RETURN:
                        result = self.map.checkUnitPresence(self.cursor.X,self.cursor.Y)
                        if result :
                            self.players[self.player_turn].Units[0]#....need a way to select the right unit....
                    self.hud_ui_manager.process_events(event)
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (2) DRAW FASE ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if self.game_state == MENU:
                self.menu.mainMenu(self.ui_window)
                self.menu_ui_manager.update(time_delta)

            # -----------------------------------------------------------------------------------------------

            if self.game_state == PLAYING:
                if self.map_state == 0:
                    self.createMap()
                self.map.drawMap(self.camera[0],self.camera[1],self.ui_window)
                self.cursor.drawCursor(self.ui_window)
                self.hud.drawHUD(self.ui_window)
                self.hud_ui_manager.update(time_delta)
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            
            pygame.display.update()
