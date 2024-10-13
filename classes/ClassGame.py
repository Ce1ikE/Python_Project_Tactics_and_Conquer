import pygame
import pygame_gui
import sys
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu

from data.Configuration import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("tactics & Conquer")
        self.ui_manager = pygame_gui.UIManager((WIN_X,WIN_Y),"./data/theme.json")
        self.ui_window = pygame.display.set_mode((WIN_X,WIN_Y))
        self.clock = pygame.time.Clock()

    def createMap(self):
        # wave grid (2D) array
        grid = Grid(WORLD_X, WORLD_Y,tileRuleset)
        grid.collapse_wave_function()
        grid.display_grid(tileSprites,self.ui_window)

    def showMenu(self):
        # "Menu" wordt getekent door "pygame_gui" dus moeten we een UIManager object doorgeven zodat we op het juiste vlak tekenen
        Menu(self.ui_manager).mainMenu()

    def run(self):
        self.showMenu()
    # de run functie runt de game
        while True:
             # Set framerate to max 40/s
            time_delta = self.clock.tick(40)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.ui_manager.process_events(event)

            self.ui_manager.update(time_delta)
            self.ui_manager.draw_ui(self.ui_window)
            pygame.display.update()
