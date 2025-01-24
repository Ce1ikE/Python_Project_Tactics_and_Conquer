import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Menu:
    def __init__(self,ui_manager: pygame_gui.UIManager):
        self.manager = ui_manager
        self.effect_timer = 4000
        self.active_effect = False

        self.mainMenuBackground = pygame.Surface((WIN_X_PX,WIN_Y_PX))
        self.mainMenuBackground.fill((0,0,0))

        panel_width = 500
        panel_height = 550

        button_width = 200
        button_height = 50

        label_height = 100

        self.main_ui_panel = pygame_gui.elements.UIPanel(
            object_id=ObjectID(object_id='#main_menu'),
            relative_rect=pygame.Rect((WIN_X_PX/2 - panel_width/2,WIN_Y_PX/2 - panel_height/2),(panel_width,panel_height)),
            manager=self.manager,
            starting_height=2
        )

        self.label_gameTitle = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((panel_width/4,panel_height/25),(panel_width/2,label_height)),
            manager=self.manager,
            container=self.main_ui_panel,
            text="Tactics and Conquer",
        )

        self.start_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/2 - button_width/2,150),(button_width,button_height)),
            text="Start",
            manager=self.manager,
            container=self.main_ui_panel,
        )

        self.quit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/2 - button_width/2,250),(button_width,button_height)),
            text="Quit",
            manager=self.manager,
            container=self.main_ui_panel,
        )

        self.how_to_play_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/2 - button_width/2,350),(button_width,button_height)),
            text="How to play",
            manager=self.manager,
            container=self.main_ui_panel,
        )

        self.continue_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/2 - button_width/2,450),(button_width,button_height)),
            text="Continue",
            manager=self.manager,
            container=self.main_ui_panel,
        )

        self.continue_btn.hide()

        image_width = 60

        self.ui_panel_how_to_play = pygame_gui.elements.UIPanel(
            object_id=ObjectID(object_id='#howToPlay'),
            relative_rect=pygame.Rect((WIN_X_PX/2 - panel_width/2,WIN_Y_PX/2 - panel_height/2),(panel_width,panel_height)),
            manager=self.manager,
            starting_height=2
        )

        self.arrow_k_up = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((panel_width/4 - image_width,60),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_SY).image_at(ARROW_UP_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.arrow_k_down = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((2*panel_width/4 - image_width,60),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_SY).image_at(ARROW_DOWN_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.arrow_k_left = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((3*panel_width/4 - image_width,60),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_SY).image_at(ARROW_LEFT_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.arrow_k_right = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((4*panel_width/4 - image_width,60),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_SY).image_at(ARROW_RIGHT_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.esc_k = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((panel_width/4 - image_width,130),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_EX).image_at(ESC_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.enter_k = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((2*panel_width/4 - image_width,130),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_EX).image_at(ENTER_K,colorkey=-1),
                TILESIZE_64/TILESIZE
            ),
            container=self.ui_panel_how_to_play
        )
        self.mouse_k = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((3*panel_width/4 - image_width,130),(image_width,image_width)),
            manager=self.manager,
            starting_height=2,
            image_surface=pygame.transform.scale_by(
                SpriteSheet(SPRITESHEET_PATH_KEYBOARDS_INPUT_MO).image_at(MOUSE_K,colorkey=-1),
                TILESIZE_32/231
            ),
            container=self.ui_panel_how_to_play
        )

        self.main_menu = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/2 - button_width/2,250),(button_width,button_height)),
            text="Main Menu",
            manager=self.manager,
            container=self.ui_panel_how_to_play,
        )

        self.ui_panel_how_to_play.hide()


    def drawMainMenu(self,ui_window: pygame.Surface):
        ui_window.blit(self.mainMenuBackground,(0,0))
        self.manager.draw_ui(ui_window)

        current_time = pygame.time.get_ticks()
        
        if not self.active_effect and current_time - self.effect_timer < self.effect_timer:
            self.active_effect = True
            self.label_gameTitle.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,params={'time_per_letter': 0.1})    

        elif  current_time - self.effect_timer > self.effect_timer:
            self.label_gameTitle.set_active_effect(None)

    def handleMenuEvents(self,event,map_state):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_btn:
                return PLAYING
            elif event.ui_element == self.continue_btn:
                return CONTINUE
            elif event.ui_element == self.how_to_play_btn:
                self.main_ui_panel.hide()
                self.ui_panel_how_to_play.show()  
            elif event.ui_element == self.main_menu:
                self.ui_panel_how_to_play.hide()  
                self.main_ui_panel.show()
                if map_state is 1:
                    self.continue_btn.show()
                else :
                    self.continue_btn.hide()
            elif event.ui_element == self.quit_btn:
                return QUIT
        return


