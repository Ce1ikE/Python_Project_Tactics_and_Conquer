import pygame
import pygame_gui

class HUD:
    def __init__(self,ui_manager):
        self.manager = ui_manager

    def drawHUD(self,ui_window):
        self.manager.draw_ui(ui_window)

    def handleHUDEvents(self,event):
        pass