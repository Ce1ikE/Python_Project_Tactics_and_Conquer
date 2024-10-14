import pygame
import pygame_gui
from data.Configuration import *

class Menu:
    def __init__(self,ui_manager):
        self.manager = ui_manager
        panel_width = 200
        panel_height = 200
        self.ui_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((WIN_X/2 - panel_width/2,WIN_Y/2 - panel_height/2),(panel_width,panel_height)),
                                               manager=self.manager,
                                               starting_height=2)
        self.text_box = pygame_gui.elements.UITextBox(html_text="<effect id=fade>welcome</effect>",
                                                 relative_rect=pygame.Rect((50,25),(100,50)),
                                                 manager=self.manager,container=self.ui_panel)                                           
        self.text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50,80),(100,25)),
                                                         manager=self.manager,
                                                         placeholder_text="Username...",
                                                         container=self.ui_panel)
        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50,110),(100,25)),
                                                 text="Start",
                                                 manager=self.manager,
                                                 container=self.ui_panel)
        self.quit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50,140),(100,25)),
                                                 text="Quit",
                                                 manager=self.manager,
                                                 container=self.ui_panel)
    def mainMenu(self,ui_window):
        self.manager.draw_ui(ui_window)      
    
    def handleMenuEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_btn:
                return PLAYING
            elif event.ui_element == self.quit_btn:
                return QUIT
        return MENU


