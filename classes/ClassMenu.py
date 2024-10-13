import pygame
import pygame_gui

class Menu:
    def __init__(self,ui_manager):
        self.manager = ui_manager

    def mainMenu(self):
        size_ele = pygame.Rect((150,25),(100,50))
        size_ele_2 = pygame.Rect((150,75),(200,50))
        size_ele_3 = pygame.Rect((150,150),(100,25))
        hello_btn = pygame_gui.elements.UIButton(relative_rect=size_ele,text="Say Hello",tool_tip_text="<p>Print hello</p>",manager=self.manager)
        text_box = pygame_gui.elements.UITextBox(html_text="<effect id=fade>Hello world</effect>",relative_rect=size_ele_2,manager=self.manager)
        text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=size_ele_3,manager=self.manager,placeholder_text="Username...")

    # def characterMenu():
        ## some code


