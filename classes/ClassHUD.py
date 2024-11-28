import pygame
import pygame_gui
import pygame_gui.ui_manager
from data.Configuration import *

# HUD == head up display
class HUD:
    def __init__(self,player_ui_manager: pygame_gui.ui_manager,unit_ui_manager: pygame_gui.ui_manager):
        self.player_manager = player_ui_manager
        self.unit_manager = unit_ui_manager
        panel_width = 150
        panel_height = 250

        self.player_ui_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,0),(panel_width,panel_height)),manager=self.player_manager,starting_height=2,object_id=pygame_gui.core.ObjectID(object_id="#HUD_panel"))
        self.unit_ui_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,0),(panel_width,panel_height)),manager=self.unit_manager,starting_height=2,object_id=pygame_gui.core.ObjectID(object_id="#HUD_panel"))

        self.next_player_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,15),(70,25)),text="End Turn",manager=self.player_manager,container=self.player_ui_panel)
        self.play_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,50),(70,25)),text="Play",manager=self.player_manager,container=self.player_ui_panel)
        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,80),(70,25)),text="Pause",manager=self.player_manager,container=self.player_ui_panel)

        self.moveUnit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,15),(70,25)),text="Move",manager=self.unit_manager,container=self.unit_ui_panel)
        self.attackUnit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,50),(70,25)),text="Attack",manager=self.unit_manager,container=self.unit_ui_panel)
        self.defendUnit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,80),(70,25)),text="Defend",manager=self.unit_manager,container=self.unit_ui_panel)

    def setHUDPanels(self,x,y):
        panel_width = 150
        panel_height = 250
        if  WIN_X_PX - panel_width < x* TILESIZE * SCALETILE:
            x -= 5
        if WIN_Y_PX - panel_height < y* TILESIZE * SCALETILE:
            y += 6
        new_position = (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE)
        self.unit_ui_panel.set_position(new_position)

    def drawUnitHUD(self,ui_window):
        self.unit_manager.draw_ui(ui_window)

    def drawPlayerHUD(self,ui_window):
        self.player_manager.draw_ui(ui_window)

    def handlePlayerHUDEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_player_btn:
                return PLAYING
            elif event.ui_element == self.pause_btn:
                return MENU
            else :            
                return 0
            
    def handleUnitHUDEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.moveUnit_btn:
                return MOVE_MODE
            elif event.ui_element == self.attackUnit_btn:
                return ATTACK_MODE
            elif event.ui_element == self.defendUnit_btn:
                return PLAYING