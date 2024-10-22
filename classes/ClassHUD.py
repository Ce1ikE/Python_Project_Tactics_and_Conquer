import pygame
import pygame_gui
from data.Configuration import *

class HUD:
    def __init__(self,ui_manager):
        self.manager = ui_manager
        panel_width = 200
        panel_height = 100
        self.ui_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((WIN_X_PX - panel_width - 15,WIN_Y_PX - panel_height - 15),(panel_width,panel_height)),
            manager=self.manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_panel")
            )
        self.next_player_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50,15),(35,25)),
            text="  ",
            manager=self.manager,
            container=self.ui_panel,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_next_player")
            )
        self.play_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((45,50),(25,25)),
            text="  ",
            manager=self.manager,
            container=self.ui_panel
            )
        self.pause_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((75,50),(25,25)),
            text="  ",
            manager=self.manager,
            container=self.ui_panel
            )
    def drawHUD(self,ui_window):
        self.manager.draw_ui(ui_window)

    def handleHUDEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_player_btn:
                return PLAYING
            elif event.ui_element == self.pause_btn:
                return MENU