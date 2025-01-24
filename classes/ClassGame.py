import pygame
import pygame_gui
import sys
import threading
from classes.ClassAnimate import Animation
from classes.ClassUnit import Unit
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu
from classes.ClassHUD import HUD
from classes.ClassMap import Map
from classes.ClassBuilding import Building
from classes.ClassPlayer import Player
from classes.ClassCursor import Cursor
from classes.ClassSpritesheet import SpriteSheet
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
        # "Menu" wordt getekent door "pygame_gui" dus moeten we een UIManager object doorgeven zodat we de juiste oppervlakte tekenen
        menu_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),MAIN_MENU_STYLE)
        self.menu = Menu(menu_ui_manager)
        # zelfde geld voor de HUD die wel meer UIManagers heeft omdat er meerdere menu's zijn tijdens het spel
        player_hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),MAIN_GAME_STYLE)
        unit_hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),MAIN_GAME_STYLE)
        building_hud_ui_manager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),MAIN_GAME_STYLE)
        self.hud = HUD(player_hud_ui_manager,unit_hud_ui_manager,building_hud_ui_manager,N_PLAYERS)

        # class that implements all complex animations
        self.animator = Animation()
        # De cursor houd bij waar de player iets selecteerd om zo makelijker de player te controleren
        self.cursor = Cursor(0,0)
        # De Game State houdt bij in welke modus we zijn van de game om zo makkelijker de game en het menu verdeelt te houden
        self.game_state = MENU # => Andere waarden : PLAYING,CREATING,etc...
        # Eens de player een map heeft aangemaakt moeten we wel zeker zijn of deze wel aangemaakt is
        self.map_state = 0
        self.map = Map()
        # In de game houden we bij welke deel van de map moet geprojecteerd worden op het scherm ("ui_window")
        self.camera = [0,0]
        # we maaken ook een list voor de players om zo als de "end_turn" in de HUD 
        # wordt ingedrukt dat de acties van de speler die worden uitgevoerd alleen 
        # voor die speciefieke speler worden uitgevoerd
        self.players: list[Player] = [ Player(x) for x in range(N_PLAYERS) ]
        self.player_turn = 0

        self.heldKey = None

        # before starting the game we load all required images/sprites for the game's animations
        self.loadAnimations()

        # HARD CODED DEBUG ============================================================================
        
        # self.players[0].addUnit(UNITS_DATA[INFANTRY],5,5)
        # self.players[0].addUnit(UNITS_DATA[TANK],7,7)
        # self.players[1].addUnit(UNITS_DATA[INFANTRY],6,6)
        
        # HARD CODED DEBUG ============================================================================

    def loadAnimations(self):
        # each player has a dictionary of animations because each player's owns his/her sprites
        for player in range(N_PLAYERS):
            for animationNameKey,coordinates in CAPTURE_ANIMATION_PLAYER[player].items():
                if animationNameKey == CAPTURE_UNIT:
                    self.players[player].captureAnimations[animationNameKey] = list()
                    for i in range(len(coordinates)): 
                        self.players[player].captureAnimations[animationNameKey].append(
                            pygame.transform.scale_by(
                                SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION_2).image_at(coordinates[i],colorkey=-1),
                                100/TILESIZE_32
                            )
                        )
                else :
                    self.players[player].captureAnimations[animationNameKey] = pygame.transform.scale_by(
                        SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION).image_at(coordinates,colorkey=-1),
                        200/TILESIZE_64
                    )

            for icon,coordinates in UNIT_ICONS[player].items():
                self.players[player].captureAnimations[icon] = pygame.transform.scale_by(
                    SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(coordinates,colorkey=None),
                    SCALETILE
                )

        # neutral Surfaces required for building animation are stored inside the map 
        for animationNameKey,coordinates in CAPTURE_ANIMATION_PLAYER[GAIA].items():
            self.map.captureAnimations[animationNameKey]  = pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION).image_at(coordinates,colorkey=-1),
                TILESIZE_64/TILESIZE
            )
            

        # the dictionary in the game object will have sprites required at each animation
        # independ of the player's color (number)
        self.animationSurfaces = {
            "buildingNumbers" : list(),
            "unitNumbers" : list()
        }

        animationCoord = UNIT_REMAINING_ICONS.copy()
        for n in range(9):
            # sprites are 9px apart in the SPRITESHEET_PATH_UNITS file
            animationCoord[0] += 9
            self.animationSurfaces["unitNumbers"].append(
                pygame.transform.scale_by(
                    SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(animationCoord,colorkey=(0,7)),
                    SCALETILE
                )   
            )
            
        animationCoord = CAPTURE_ANIMATION_NUMBERS.copy()
        for i in range(10):
            # sprites are 10px apart in the SPRITESHEET_PATH_CAPTURE_ANIMATION file
            animationCoord[0] += 10 
            self.animationSurfaces["buildingNumbers"].append(
                pygame.transform.scale_by(
                    SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION).image_at(animationCoord,colorkey=-1),
                    SCALETILE
                )
            )
        self.animationSurfaces["capture_panel"] = pygame.transform.scale_by(
            SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION).image_at(CAPTURE_PANEL,colorkey=-1),
            250/TILESIZE_64
        )
        
        self.animationSurfaces["capture_complete"] = pygame.transform.scale_by(
            SpriteSheet(SPRITESHEET_PATH_CAPTURE_ANIMATION).image_at(CAPTURE_COMPLETE,colorkey=-1),
            TILESIZE_32/TILESIZE
        )        
        

    def startMapGeneration(self):
        self.thread_for_map = threading.Thread(target=self.createMap,daemon=True)
        self.thread_for_map.start()

    def createMap(self):
        grid = Grid(WORLD_X, WORLD_Y,self.ui_window,self.players,self.map)
        while self.map_state == 0:
            result = grid.collapse_wave_function()
            if result == 0:

                if grid.validate_map():
                    self.map_state = 1
                    print("map generation succeeded, continuing...") 
                else :
                    print("validation failed, retrying...")
                    self.map_state = 0 
                    grid = Grid(WORLD_X, WORLD_Y,self.ui_window,self.players,self.map)                    

            elif result == -1:
                # eens het resultaat "-1" is betekent dat het algorithme een fout heeft gevonden 
                # => een "TILE_BLANK" is weg geschreven naar een "Cell" object
                # daarom vernietigen we het grid
                # see => https://gamedev.stackexchange.com/questions/178443/resolving-contradictions-in-wfc-more-efficiently-than-naive-backtracking

                # i quote : "In an old implementation of WFC I used to rebuild the possibility space around a contradiction. 
                # But I don't think that solution is good in most cases. You can't know when the seeds of the contradiction 
                # were sowed. Its usually faster to reset the whole thing." => NUKE IT !
                print("map generation failed, retrying...")
                self.map_state = 0 
                grid = Grid(WORLD_X, WORLD_Y,self.ui_window,self.players,self.map)

    def run(self):
        # de "run" functie runt de game
        while True:
            # Set framerate to max 40/s
            # per frame everything will be calculated 40 times -> if you want increase be advised the game might be less smoother
            time_delta = self.clock.tick(FPS)/1000.0
            
            # --------------------------------------------------------------------------------------------------------------

            # Er zijn 2 fases in de game loop
            # (1) de "event" fase
            # waarin we checken of er iets gebeurt is of iets zoals een knop die wordt ingedrukt
            # deze fase wordt nog eens in 6 gesplitst afhankelijk van de "game_state" :
            
            # (1.1) de CREATING state
            # is actief wanneer er een nieuwe map wordt aangemaakt en zal dus pas afgelopen zijn eens deze map gegenereerd is
            
            # (1.2) de PLAYING state
            # is actief wanneer er een nieuwe map is aangemaakt of de speler terug vanuit een menu naar de map gaat
            
            # (1.3) de MENU state
            # is actief eens in-game menu wordt geopent wanneer de game opstart wordt deze automatisch geopent
            
            # (1.4) de HUD_MENU_UNIT state
            # is actief eens er in de PLAYING state een object "Unit" wordt geselecteerd. Deze fase wordt zelf afgesplist in 3 fases
            
            # (1.4.1) de ATTACK_MODE
            # is actief eens er in de HUD_MENU_UNIT de knop "Attack" wordt geselecteerd. 
            # wordt terug inactief na dat "ESC" is ingedrukt of eens een vakje is geselecteerd waarin een vijandelijke eenheid in staat
            
            # (1.4.2) de MOVE_MODE
            # is actief eens er in de HUD_MENU_UNIT de knop "Move" wordt geselecteerd
            # wordt terug inactief na dat "ESC" is ingedrukt of eens een vakje is geselecteerd waarin een geen andere eenheid in staat 
            
            # (1.4.3) de DEFENSE_MODE
            # is actief eens er in de HUD_MENU_UNIT de knop "Defend" wordt geselecteerd
            # verlaat de HUD_MENU state en zet het spel in de PLAYING state
            
            # (1.5) de HUD_MENU_BUILDING state

            # (1.6) de CAPTURE state

            # --------------------------------------------------------------------------------------------------------------
            
            # (2) de "draw" fase
            # waarin we alle layers in volgorde gaan tekenen dus 
            # bv.: 
            # 1->map 
            # 2->characters 
            # 3->HUD
            # zodanig dat alles juist ovelapt met elkaar
            # deze wordt net als de "event" fase in gesplitst in verschillende delen afhankelijk van de "game_state" maar hier zijn maar 3 fases
            # de CREATING fase is hier niet van toepassing

            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (1) EVENT FASE ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # Game events zoals "pygame_gui.UI_BUTTON_PRESSED" of "pygame.KEY_D"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.heldKey = "up"
                    elif event.key == pygame.K_LEFT:
                        self.heldKey = "left"
                    elif event.key == pygame.K_DOWN:
                        self.heldKey = "down"
                    elif event.key == pygame.K_RIGHT:
                        self.heldKey = "right"

                if event.type == pygame.KEYUP:
                    self.heldKey = None

            # MENU STATE ---------------------------------------------------------------------------------------------------

                if self.game_state == MENU:
                    result = self.menu.handleMenuEvents(event,self.map_state)

                    if result == PLAYING:
                        self.map_state = 0
                        self.startMapGeneration()
                        self.game_state = CREATING

                    elif result == CONTINUE:
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")

                    elif result == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    self.menu.manager.process_events(event)
            
            # CREATING STATE -----------------------------------------------------------------------------------------------
            
                elif self.game_state == CREATING:
                    if self.map_state == 1:
                        self.thread_for_map = None
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")
                    
            # PLAYING STATE ------------------------------------------------------------------------------------------------

                elif self.game_state == PLAYING:                    
                    result = self.hud.handlePlayerHUDEvents(event)

                    if result == PLAYING:
                        self.players[self.player_turn].endTurn(True)
                        self.player_turn = (self.player_turn + 1) % N_PLAYERS # of course i can't go out of bounds so modulo by the number of players
                        self.hud.player_label_funds.set_text("G. " + str(self.players[self.player_turn].funds))
                        self.hud.setPlayerHUDPanel(0,0,self.player_turn)
                        print(f"next turn => current player {self.player_turn}")
                    
                    elif result == MENU:
                        if self.map_state is 1:
                            self.menu.continue_btn.show()
                        self.game_state = MENU
                        print(f"changed to MENU state")

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        result = self.players[self.player_turn].playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]] 
                        
                        unitPresent = False
                        captureEnabled = False
                        checkBuilding = True
                        
                        # only allow a unit to be selected when there is one at the current location and it's in the active state
                        if result is not False and self.players[self.player_turn].unitsPlayerList[result].active:
                            # We select the right unit by :
                            # 1) selecting the right "player" object within the list "players", the "player_turn" variable will tell us which player's turn it is
                            # 2) inside this "player" object i have created a map that holds all Unit ID's
                            self.currentlySelectedUnit: Unit = self.players[self.player_turn].unitsPlayerList[result]
                            if self.currentlySelectedUnit.unitType in UNITS_CAN_CAPTURE:
                                # once a unit is selected we check whether their is a building at the same position
                                # that is not from this player or a other player
                                # else we check on the map if their is a building on that position
                                for player in self.players:
                                    if player != self.players[self.player_turn]:
                                        result = player.playerBuildingsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                                        if result is not False:
                                            captureEnabled = True 
                                            checkBuilding = False
                                            self.requiredAnimationsForCapture = player.captureAnimations[
                                                player.buildingsPlayerList[result].buildingType
                                            ]
                                    if player == self.players[self.player_turn]:
                                        result = player.playerBuildingsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                                        if result is not False:
                                            captureEnabled = False
                                            checkBuilding = False

                                if checkBuilding is True :
                                    result = self.map.mapTerrain[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                                    if result in POTENIAL_CAPTURES and result not in POTENIAL_TRAINING:
                                        captureEnabled = True 
                                        self.requiredAnimationsForCapture = self.map.captureAnimations[result]

                            self.hud.setUnitHUDPanels(captureEnabled)
                            self.game_state = HUD_MENU_UNIT
                            print(f"changed to HUD_MENU_UNIT state")
                        
                        # If no unit was detected on the cursor's position for the current player
                        # we check if the current player has a building at the cursor's position
                        # NOTE: units have a higher priority then buildings because of the simple fact that buildings are useless
                        # when a unit is at that current location
                        elif result is False:
                            for player in self.players:
                                if player != self.players[self.player_turn]:
                                    result = player.playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                                    if result is not False:
                                        unitPresent = True

                            if not unitPresent:
                                result = self.players[self.player_turn].playerBuildingsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]] 

                                if result is not False and self.players[self.player_turn].buildingsPlayerList[result].active:
                                    self.currentlySelectedBuilding: Building = self.players[self.player_turn].buildingsPlayerList[result]
                                    self.hud.setBuildingHUDPanel(self.currentlySelectedBuilding,self.players[self.player_turn])
                                    self.game_state = HUD_MENU_BUILDING
                                    print(f"changed to HUD_MENU_UNIT state")

                    self.hud.player_manager.process_events(event)        

            # HUD UNIT STATE -----------------------------------------------------------------------------------------------

                elif self.game_state == HUD_MENU_UNIT:
                    result = self.hud.handleUnitHUDEvents(event)

                    if result == ATTACK_MODE:
                        print(f"changed to ATTACK mode")
                        ZoneCoord = self.currentlySelectedUnit.getAttackZone(self.players)
                        self.game_state = ATTACK_MODE
                    
                    elif result == MOVE_MODE:
                        print(f"changed to MOVE mode")
                        ZoneCoord = self.currentlySelectedUnit.getTravelZone(self.map)
                        self.game_state = MOVE_MODE
                    
                    elif result == DEFEND_MODE:
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")

                    elif result == CAPTURE:
                        self.animator.isAnimating = True
                        self.game_state = CAPTURE
                        print(f"changed to CAPTURE state")

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")    
                    
                    self.hud.unit_manager.process_events(event)

            # ATTACK STATE -------------------------------------------------------------------------------------------------

                # key difference between move and attack is whether there is a unit or not
                # on the selected tile
                elif self.game_state == ATTACK_MODE:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        # if in ATTACK mode and enter is pressed i got to check whether there
                        # is in fact a unit on that position that does NOT belong to the current player
                        for player in self.players:
                            if player != self.players[self.player_turn]:
                                result = player.playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]] 
                                if result is not False:
                                    
                                    self.enemyUnit: Unit = player.unitsPlayerList[result]
                                    print(f"unit attacks square --> X : {self.cursor.X + self.camera[0]} Y : {self.cursor.Y + self.camera[1]}")
                                    self.currentlySelectedUnit.attack(self.enemyUnit,self.map.mapTerrain[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]])
                                    
                                    if self.enemyUnit.health == 0 :
                                        player.playerUnitsMap[self.enemyUnit.Y][self.enemyUnit.X] = False
                                        player.unitsPlayerList.pop(result)
                                        print(f"unit killed enemy unit")

                                    elif self.enemyUnit.health  > 0 :
                                        enemyAttackZone = self.enemyUnit.getAttackZone(self.players)
                                        
                                        if (self.currentlySelectedUnit.X,self.currentlySelectedUnit.Y) in enemyAttackZone:
                                            print(f"enemy counters and attacks square --> X : {self.currentlySelectedUnit.X} Y : {self.currentlySelectedUnit.Y}")
                                            self.enemyUnit.attack(self.currentlySelectedUnit,self.map.mapTerrain[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]])
                                        
                                    if self.currentlySelectedUnit.health == 0 :
                                        self.players[self.player_turn].playerUnitsMap[self.currentlySelectedUnit.Y][self.currentlySelectedUnit.X] = False
                                        self.players[self.player_turn].unitsPlayerList.pop(self.currentlySelectedUnit.unitID)
                                        print(f"enemy killed unit")
                                    elif self.currentlySelectedUnit.health > 0 :
                                        self.currentlySelectedUnit.active = False

                                    self.game_state = PLAYING
                                    print(f"changed to PLAYING state")                            
                        
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.game_state = HUD_MENU_UNIT
                        print(f"changed to HUD_MENU_UNIT state")                            

            # MOVE STATE ---------------------------------------------------------------------------------------------------

                elif self.game_state == MOVE_MODE:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        # if in MOVE mode and enter is pressed i got to check whether there
                        # is in fact a unit on that position
                        allowedMove = True
                        for player in self.players:
                            result = player.playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                            if result is not False:
                                allowedMove = False
                                
                        if allowedMove:
                            self.players[self.player_turn].changeUnitPresence(
                                self.currentlySelectedUnit.X,
                                self.currentlySelectedUnit.Y,
                                self.cursor.X + self.camera[0],
                                self.cursor.Y + self.camera[1],
                                self.currentlySelectedUnit.unitID
                            )
                            print(f"unit moves to --> X : {self.cursor.X + self.camera[0]} Y : {self.cursor.Y + self.camera[1]}")
                            
                            if self.currentlySelectedUnit.isCapturing:
                                self.currentlySelectedUnit.capturedBuildingHealth = 20
                                self.currentlySelectedUnit.isCapturing= False
                            print(f"unit was capturing a building but has been cancelled")

                            self.game_state = PLAYING
                            print(f"changed to PLAYING state")

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.game_state = HUD_MENU_UNIT
                        print(f"changed to HUD_MENU state")
             
            # HUD BUILDING STATE -------------------------------------------------------------------------------------------
            
                elif self.game_state == HUD_MENU_BUILDING:
                    result = self.hud.handleBuildingHUDEvents(event,self.player_turn)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        unitSelected = self.hud.possibleUnits[self.hud.cycleListUnits] 
                        if UNITS_COST[unitSelected] <= self.players[self.player_turn].funds:
                            self.players[self.player_turn].funds -= UNITS_COST[unitSelected]
                            self.players[self.player_turn].addUnit(UNITS_DATA[unitSelected],self.cursor.X + self.camera[0],self.cursor.Y + self.camera[1])
                            self.game_state = PLAYING
                            print(f"changed to PLAYING state")

                        if result == PLAYING:
                            self.game_state = PLAYING
                            print(f"changed to PLAYING state")

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state")    

                    self.hud.building_manager.process_events(event)

            # CAPTURE STATE ----------------------------------------------------------------------------------------------

                elif self.game_state == CAPTURE:
                    if self.animator.isAnimating is False:
                        self.currentlySelectedUnit.isCapturing = True
                        self.currentlySelectedUnit.active = False
                        self.currentlySelectedUnit.capturedBuildingHealth -= self.currentlySelectedUnit.health 
                        
                        self.game_state = PLAYING
                        print(f"changed to PLAYING state") 

                        # once a capture is completed we reassign the default values of this unit
                        if self.currentlySelectedUnit.capturedBuildingHealth <= 0:
                            self.currentlySelectedUnit.capturedBuildingHealth = 20
                            self.currentlySelectedUnit.isCapturing = False

                            for player in self.players:
                                result = player.playerBuildingsMap[self.currentlySelectedUnit.Y][self.currentlySelectedUnit.X]
                                if result is not False:
                                    player.buildingsPlayerList.pop(result)

                            # the "CAPTURE_MATRIX" describes what a building tile a building should become after capture 
                            newBuildingType = CAPTURE_MATRIX[self.player_turn][self.map.mapTerrain[self.currentlySelectedUnit.Y][self.currentlySelectedUnit.X]]

                            self.players[self.player_turn].addBuilding(newBuildingType,self.cursor.X + self.camera[0],self.cursor.Y + self.camera[1])

                            # if somebody captures a HQ the player wins the game
                            if newBuildingType in WINNING_CAPTURES:

                                if self.player_turn == PLAYER_1:
                                    winning_message = str("Player 1 has won")
                                    self.menu.label_gameTitle.bg_colour = pygame.Color("#F8B8780A")
                                elif self.player_turn == PLAYER_2:
                                    self.menu.label_gameTitle.bg_colour = pygame.Color("#B8F0F80A")
                                    winning_message = str("Player 2 has won")
                                elif self.player_turn == PLAYER_3:
                                    self.menu.label_gameTitle.bg_colour = pygame.Color("#F8F8980A")
                                    winning_message = str("Player 3 has won")
                                elif self.player_turn == PLAYER_4:
                                    self.menu.label_gameTitle.bg_colour = pygame.Color("#D8F8C80A")
                                    winning_message = str("Player 4 has won")

                                self.menu.label_gameTitle.set_text(winning_message)
                                self.game_state = MENU                            
                                print(f"changed to MENU state")    
                                print(f"winning condition met")   
                           
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # (2) DRAW FASE /////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if self.game_state == MENU:
                self.menu.drawMainMenu(self.ui_window)
                self.menu.manager.update(time_delta)

            # PLAYING STATE ------------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) Map
            # (2) Buildings
            # (3) Units
            # (4) Unit Details
            # (5) Cursor
            # (5) Player HUD
            elif self.game_state == PLAYING:
                if self.heldKey:
                    self.camera = self.cursor.UpdatePosition(self.camera[0],self.camera[1],self.heldKey)
                    self.hud.setPlayerHUDPanel(self.cursor.X,self.cursor.Y,False)

                self.map.drawMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                
                result = self.players[self.player_turn].playerUnitsMap[self.cursor.Y + self.camera[1]][self.cursor.X + self.camera[0]]
                if result is not False:
                    self.players[self.player_turn].unitsPlayerList[result].showUnitsDetails(self.ui_window,time_delta)
                
                self.cursor.drawCursor(self.ui_window)
                self.hud.drawPlayerHUD(self.ui_window)
                self.hud.player_manager.update(time_delta)

            # HUD UNIT STATE -----------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) HUDMap
            # (2) Buildings
            # (3) Units
            # (4) Unit HUD
            elif self.game_state == HUD_MENU_UNIT:
                self.map.drawHUDMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                self.hud.drawUnitHUD(self.ui_window)
                self.hud.unit_manager.update(time_delta)

            # ATTACK STATE -------------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) HUDMap
            # (2) Buildings
            # (3) Units
            # (4) Unit Attack Zone
            elif self.game_state == ATTACK_MODE:
                if self.heldKey:
                    self.camera = self.cursor.setPosition(self.camera[0],self.camera[1],ZoneCoord,self.heldKey)

                self.map.drawHUDMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                self.currentlySelectedUnit.showAttackZone(self.camera[0],self.camera[1],self.ui_window,ZoneCoord)
                self.cursor.drawAttackCursor(self.ui_window)
 
            # MOVE STATE ---------------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) HUDMap
            # (2) Buildings
            # (3) Units
            # (4) Unit Travel Zone
            elif self.game_state == MOVE_MODE:
                if self.heldKey:
                    self.camera = self.cursor.cyclePosition(self.camera[0],self.camera[1],ZoneCoord,self.heldKey)
                    
                self.map.drawHUDMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                self.currentlySelectedUnit.showTravelZone(self.camera[0],self.camera[1],self.ui_window,ZoneCoord)
                self.cursor.drawCursor(self.ui_window)

            # HUD BUILDING STATE -------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) HUDMap
            # (2) Buildings
            # (3) Units
            # (4) Building HUD 
            elif self.game_state == HUD_MENU_BUILDING:
                self.map.drawHUDMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                self.hud.drawBuildingHUD(self.ui_window)
                self.hud.building_manager.update(time_delta)

            # CAPTURE STATE ----------------------------------------------------------------------------------------------
            # order of drawing:
            # -----------------
            # (1) Map
            # (2) Buildings
            # (3) Units
            # (4) Capture Animation
            elif self.game_state == CAPTURE:
                self.map.drawMap(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawBuildings(self.camera[0],self.camera[1],self.ui_window)
                for player in self.players:
                    player.drawUnits(self.camera[0],self.camera[1],self.ui_window,self.animationSurfaces)
                self.animator.animateCapture(self.ui_window)

            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            # after drawing everything (virtually) we need to update the display (ui_window)
            # and afterwards a new frame is calculated and new events will be processed
            pygame.display.update()


