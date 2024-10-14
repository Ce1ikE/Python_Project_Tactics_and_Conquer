import pygame
import pygame_gui
import sys
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu
from classes.ClassHUD import HUD

from data.Configuration import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("tactics & Conquer")
        self.hud_ui_manager = pygame_gui.UIManager((WIN_X,WIN_Y),"./data/theme.json")
        self.menu_ui_manager = pygame_gui.UIManager((WIN_X,WIN_Y),"./data/theme.json")
        self.ui_window = pygame.display.set_mode((WIN_X,WIN_Y))
        self.clock = pygame.time.Clock()
         # "Menu" wordt getekent door "pygame_gui" dus moeten we een UIManager object doorgeven zodat we op het juiste vlak tekenen
        self.menu = Menu(self.menu_ui_manager)
        self.hud = HUD(self.hud_ui_manager)
        self.game_state = MENU

    def createMap(self):
        # wave grid (2D) array
        grid = Grid(WORLD_X, WORLD_Y,tileRuleset)
        grid.collapse_wave_function()
        grid.display_grid(tileSprites,self.ui_window)
        return 0

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
                        self.map_state = 1
                    elif result == QUIT:
                        pygame.quit()
                        sys.exit()
                    self.menu_ui_manager.process_events(event)

                if self.game_state == PLAYING:
                    self.hud_ui_manager.process_events(event)
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            # (2) DRAW FASE ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if self.game_state == MENU:
                self.menu.mainMenu(self.ui_window)
                self.menu_ui_manager.update(time_delta)
            if self.game_state == PLAYING:
                if self.map_state == 1:
                    self.map_state = self.createMap()
                    self.hud.drawHUD(self.ui_window)
                self.hud_ui_manager.update()
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                

            
            pygame.display.update()
