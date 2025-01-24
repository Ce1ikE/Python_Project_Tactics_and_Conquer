import pygame
import pygame_gui
from classes.ClassBuilding import Building
from classes.ClassPlayer import Player
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

# HUD == head up display
class HUD:
    def __init__(self,player_ui_manager: pygame_gui.UIManager,unit_ui_manager: pygame_gui.UIManager,building_ui_manager: pygame_gui.UIManager,numberOfPlayers: int):
        panel_width = 200
        panel_height = 200

        button_height = 30
        button_padding = 10

        # I seperate all different panels into their own "managers" for simplicity you can however do it with 1 single manager
        # but that requires clearing the whole each time you want to change your UI during run time
        # also if the UI is redrawn but a previous element was not erased from the parent container
        # this element can still interactive even though it is not shown. When working with multiple UIManagers you don't have this problem
        # since you can decide in your main game loop what is drawn upon each other and because how "pygame_gui" works these UI get split into layers
        # Now if you would like to learn with 1 single UIManager you can of course do so but you will have to implement some logic to use the
        # "hide" and "show" methods -> which i use -> see the "HUD" "setBuildingHUDPanel" 

        # ---------------------------------------------------------------------------------------------------------------------------------
        # manager and elements for the unit HUD during the HUD_MENU_UNIT state

        panel_height = 3*(button_height + 2*button_padding)

        self.unit_manager = unit_ui_manager
        self.unit_ui_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((0,0),(panel_width,panel_height)),
            manager=self.unit_manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_panel")
        )
        self.moveUnit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,20),(panel_width/2,button_height)),
            text="Move",
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )
        self.attackUnit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,60),(panel_width/2,button_height)),
            text="Attack",
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )
        self.defendUnit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,100),(panel_width/2,button_height)),
            text="Defend",
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )

        self.captureUnit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,140),(panel_width/2,button_height)),
            text="Capture",
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )

        self.captureUnit_btn.hide()

        move_surface = SpriteSheet(SPRITESHEET_PATH_HUD_DEFEND).image_at([0,0,18,18],colorkey=-1)
        move_surface = pygame.transform.rotate(move_surface,90)
        self.attack_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,20),(30,30)),
            image_surface=pygame.transform.scale_by(move_surface,30/18),
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )

        attack_surface = SpriteSheet(SPRITESHEET_PATH_HUD_ATTACK).image_at([0,0,18,18],colorkey=-1)
        self.attack_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,60),(30,30)),
            image_surface=pygame.transform.scale_by(attack_surface,30/18),
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )
        
        defend_surface = SpriteSheet(SPRITESHEET_PATH_HUD_DEFEND).image_at([0,0,18,18],colorkey=-1)
        self.defend_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,100),(30,30)),
            image_surface=pygame.transform.scale_by(defend_surface,30/18),
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )

        capture_surface = SpriteSheet(SPRITESHEET_PATH_HUD_CAPTURE).image_at([0,0,18,18],colorkey=-1)
        self.capture_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,140),(30,30)),
            image_surface=pygame.transform.scale_by(capture_surface,30/18),
            manager=self.unit_manager,
            container=self.unit_ui_panel
        )

        self.capture_image.hide()

        # ---------------------------------------------------------------------------------------------------------------------------------
        # manager and elements for the player HUD during the PLAYING state
        self.player_manager = player_ui_manager

        panel_height = 2*(button_height + 2*button_padding)

        self.player_ui_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((0,0),(panel_width,panel_height)),
            manager=self.player_manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_playerPanel")
        )
        self.player_ui_panel_funds = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((panel_width,0),(panel_width,button_height)),
            manager=self.player_manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_funds_panel")
        )
        self.player_label_funds = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0,0),(panel_width/1.5,button_height)),
            manager=self.player_manager,
            container=self.player_ui_panel_funds,
            text="G. 0",            
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_funds_panel.label")
        )
        self.next_player_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,20),(panel_width/2,button_height)),
            text="End Turn",
            manager=self.player_manager,
            container=self.player_ui_panel
        )
        self.pause_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((panel_width/4,60),(panel_width/2,button_height)),
            text="Main Menu",
            manager=self.player_manager,
            container=self.player_ui_panel
        )

        next_player_surface = SpriteSheet(SPRITESHEET_PATH_HUD_NEXT_PLAYER).image_at([0,0,30,30],colorkey=-1)
        self.next_player_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,20),(30,30)),
            image_surface=next_player_surface,
            manager=self.player_manager,
            container=self.player_ui_panel
        )
        
        pause_surface = SpriteSheet(SPRITESHEET_PATH_HUD_GENERAL_ICONS).image_at([2,150,16,16],colorkey=-1)
        self.pause_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,60),(30,30)),
            image_surface=pygame.transform.scale_by(pause_surface,30/16),
            manager=self.player_manager,
            container=self.player_ui_panel
        )


        # ---------------------------------------------------------------------------------------------------------------------------------
        # manager and elements for the building (BARRACKS) HUD during the HUD_MENU_BUILDING state
        self.building_manager = building_ui_manager

        panel_width  = WIN_X_PX/2
        panel_height = WIN_Y_PX/2
        row_height = 40
        padding = 20

        self.barracks_ui_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((padding,padding),(WIN_X_PX - padding,WIN_Y_PX - padding)),
            manager=self.building_manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Panel"),
        )

        # UIScrollingContainers are not yet customizable in pygame_gui so we will have to do with it
        self.barracks_ui_ScrollingContainer = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect((0,0),(WIN_X_PX/2,WIN_Y_PX)),
            manager=self.building_manager,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Panel.scroll"),
            allow_scroll_x=True,
            allow_scroll_y=False,
            container=self.barracks_ui_panel
        )

        self.barracks_ui_ScrollingContainer.set_scrollable_area_dimensions(
            (WIN_X_PX/2,row_height*len([INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]))
        )

        self.barracks_ui_sidePanel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((WIN_X_PX/2,0),(WIN_X_PX/2,WIN_Y_PX/2)),
            manager=self.building_manager,
            container=self.barracks_ui_panel,
            starting_height=2,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Panel.side"),
        )

        HUDimage = 200
        # one UIImage to display the currently selected unit
        self.unitHUDImage = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(((WIN_X_PX/4 - HUDimage/2),100),(HUDimage,HUDimage)),
            manager=self.building_manager,
            container=self.barracks_ui_sidePanel,
            image_surface=pygame.Surface((HUDimage,HUDimage)),
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Unit.HUDImage")
        )

        # create a 2D array (list) to hold all sprites
        self.imageUnitList = [list() for _ in range(N_PLAYERS)]

        # implemented units 
        # NOTE: the following units are implemented correctly in the configuration file
        # if others are added all their configuration must be correctly done beforehand 
        possibleUnits = [INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]

        self.elementsList: list = list()
        # in order to avoid to reload new sprites(images) during run time each time a building is selected
        # i store them all inside the HUD object. we will just have to implement some logic 
        # to display the right image/sprite
        # How do i set them up ?
        # (1) and (2) overlap but the one that is shown depends on the money the user has
        # (3) is set next to (1) or (2) with a "text_horiz_alignment" in the style file set to "left"
        # (4) is set next to (3) with a "text_horiz_alignment" in the style file set to "right"
        # (5) is set apart in it's own panel
        for i,unit in enumerate(possibleUnits):
            
            # for each unit add a row of UIlabels and UIImages 
            label_name = UNITS_NAMES[unit]
            label_cost = str(UNITS_COST[unit])
            # elements required for each table entry
            unitImage = pygame_gui.elements.UIImage(
                relative_rect=pygame.Rect((10,row_height*(i + 1)),(row_height,row_height)),
                manager=self.building_manager,
                container=self.barracks_ui_ScrollingContainer,
                image_surface=pygame.Surface((row_height,row_height)),
                object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Unit.image")
            )

            unitLabelName = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((10 + row_height,row_height*(i + 1)),(120,row_height)),
                text=label_name,
                manager=self.building_manager,
                container=self.barracks_ui_ScrollingContainer,
                object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Unit.label_name")
            )

            unitLabelCost = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((130 + row_height,row_height*(i + 1)),(120,row_height)),
                text=label_cost,
                manager=self.building_manager,
                container=self.barracks_ui_ScrollingContainer,
                object_id=pygame_gui.core.ObjectID(object_id="#HUD_Barracks_Unit.label_cost")
            )
            # and store these elements in a 2D array for later use
            self.elementsList.append((unitImage,unitLabelName,unitLabelCost))

            for player in range(N_PLAYERS):

                spritesheetCoord_idle = UNITS_SPRITES[unit][12].copy()
                spritesheetCoord_una  = UNITS_SPRITES[unit][18].copy()
                spritesheetCoord_idle[0] += PLAYERS_SPRITESHEET_OFFSET[player][0]
                spritesheetCoord_idle[1] += PLAYERS_SPRITESHEET_OFFSET[player][1]
                spritesheetCoord_una[0] += PLAYERS_SPRITESHEET_OFFSET[player][0]
                spritesheetCoord_una[1] += PLAYERS_SPRITESHEET_OFFSET[player][1]
                spritesheetCoord_hud  = UNITS_HUD_SPRITES[unit].copy()
                spritesheetCoord_hud[1] += PLAYERS_SPRITESHEET_OFFSET_2[player][1] 

                idle_l_1 = pygame.transform.scale_by(SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(spritesheetCoord_idle,colorkey=-1),row_height/TILESIZE)
                una_l_1 = pygame.transform.scale_by(SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(spritesheetCoord_una,colorkey=-1),row_height/TILESIZE)
                hud = pygame.transform.scale_by(SpriteSheet(SPRITESHEET_PATH_HUD_UNITS).image_at(spritesheetCoord_hud,colorkey=-1),HUDimage/TILESIZE_64)

                self.imageUnitList[player].append((idle_l_1,una_l_1,hud))

        # add Cursor at the end such that it overlaps in the right order
        self.cycleListUnits = 0
        cursor = SpriteSheet(SPRITESHEET_PATH_HUD_PLAY).image_at([0,0,30,30],colorkey=-1)
        self.barracks_ui_cursor = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10,row_height + padding),(row_height,row_height)),
            image_surface=pygame.transform.scale_by(cursor,30/TILESIZE),
            manager=self.building_manager,
            container=self.barracks_ui_ScrollingContainer,
        )

    def setBuildingHUDPanel(self,building: Building,player: Player):
        # display the correct parts of the building HUD based upon the selected building (PLAYER,COLOR,etc...)
        # better ideas (perhaps) : 
        # -> "set_image" method keeps the UIImage element but changes the pygame.Surface instead which means no additional UIImage elements should be created
        # -> "disable" and "enable" have can be set and so different styling will be applied if set in the right json file
        # -> 

        playerTeam = player.player_number
        playerFunds = player.funds
        idle_surface = 0
        una_surface = 1
        hud_surface = 2

        unit_UIImage = 0
        unit_UILabel_name = 1
        unit_UILabel_cost = 2

        # if more units are to be implemented expand this list to required units
        # or add other building tiles to POTENIAL_TRAINING  
        if building.buildingType == TILE_HQ_RED:
            self.possibleUnits = [INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]

        elif building.buildingType == TILE_BARRACKS_RED:
            self.possibleUnits = [INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]
        
        elif building.buildingType == TILE_HQ_BLUE:
            self.possibleUnits = [INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]
        
        elif building.buildingType == TILE_BARRACKS_BLUE:
            self.possibleUnits = [INFANTRY,HEAVY_INFANTRY,TANK,MEDIUM_TANK,HEAVY_TANK,ARTILLERY]

        # always set to the first top unit
        self.cycleListUnits = 0
        # each Element in Pygame_Gui is based upon the UIElement Class which is abstract class
        # and so every UIElement such as UILabel ans UIScrollingContainer can "hide" itself and "show"  
        self.barracks_ui_ScrollingContainer.hide()
        self.barracks_ui_sidePanel.show()        

        if playerTeam == PLAYER_1:
            self.barracks_ui_sidePanel.background_colour = pygame.Color("#F8B878A0")

        elif playerTeam == PLAYER_2:
            self.barracks_ui_sidePanel.background_colour = pygame.Color("#B8F0F8A0")
        
        elif playerTeam == PLAYER_3:
            self.barracks_ui_sidePanel.background_colour = pygame.Color("#F8F898A0")
        
        elif playerTeam == PLAYER_4:
            self.barracks_ui_sidePanel.background_colour = pygame.Color("#D8F8C8A0")

        self.barracks_ui_sidePanel.rebuild()

        self.unitHUDImage.set_image(self.imageUnitList[playerTeam][self.cycleListUnits][hud_surface])
        self.unitHUDImage.show()
        # each time the panel is opened i look wich player opened a Building HUD 
        # and which type of building, to create different types of HUD's
        for unit in range(len(self.possibleUnits)):
            # if the player has enough funds(money) to pay for the unit we set the idle_l_1 image
            # if the player has NOT enough funds to pay we set the una_l_1 image + labels to disable
            # NOTE: while "set_image" is specified you can see that it requires a Pygame.Surface which is actually provided 
            UIImage: pygame_gui.elements.UIImage = self.elementsList[unit][unit_UIImage]
            UILabel_name: pygame_gui.elements.UILabel = self.elementsList[unit][unit_UILabel_name]
            UILabel_cost: pygame_gui.elements.UILabel = self.elementsList[unit][unit_UILabel_cost]

            UILabel_name.show()
            UILabel_cost.show()
            UIImage.show()

            if UNITS_COST[unit] <= playerFunds: 
                UIImage.set_image(self.imageUnitList[playerTeam][unit][idle_surface])
                UILabel_name.enable()
                UILabel_cost.enable()
            else :
                UIImage.set_image(self.imageUnitList[playerTeam][unit][una_surface])
                UILabel_name.disable()
                UILabel_cost.disable()

        self.barracks_ui_cursor.show()
                  
    def setUnitHUDPanels(self,captureEnabled: bool):
        # readjust the unit HUD to the position where the unit is
        button_padding = 10
        panel_width = 200
        button_height = 30

        if captureEnabled:
            panel_height = 4*(button_height + 2*button_padding)
            self.captureUnit_btn.show()
            self.capture_image.show()
        else:
            panel_height = 3*(button_height + 2*button_padding)
            self.captureUnit_btn.hide()
            self.capture_image.hide()

        new_dimensions = (panel_width,panel_height)
        self.unit_ui_panel.set_dimensions(new_dimensions)

    def setPlayerHUDPanel(self,x,y,playerTeam):
        # readjust the player HUD if the cursor is in the same position
        # else change the player's HUD to the right color
        panel_width = 200
        panel_height = 200
        if playerTeam is False:
            if x* TILESIZE * SCALETILE <= panel_width and y* TILESIZE * SCALETILE <= panel_height:
                new_position = ((WIN_X_PX - panel_width),0)
                self.player_ui_panel.set_position(new_position)
                new_position = (WIN_X_PX - 2*panel_width,0)
                self.player_ui_panel_funds.set_position(new_position)

            if WIN_X_PX - panel_width  <= x* TILESIZE * SCALETILE  and y* TILESIZE * SCALETILE <= panel_height:
                new_position = (0,0)
                self.player_ui_panel.set_position(new_position)
                new_position = (panel_width,0)
                self.player_ui_panel_funds.set_position(new_position)
        else:
            if playerTeam == PLAYER_1:
                self.player_ui_panel.background_colour = pygame.Color("#F8B878")
                self.player_ui_panel_funds.background_colour = pygame.Color("#F8B878")

            elif playerTeam == PLAYER_2:
                self.player_ui_panel.background_colour = pygame.Color("#B8F0F8")
                self.player_ui_panel_funds.background_colour = pygame.Color("#B8F0F8")
            
            elif playerTeam == PLAYER_3:
                self.player_ui_panel.background_colour = pygame.Color("#F8F898")
                self.player_ui_panel_funds.background_colour = pygame.Color("#F8F898")
            
            elif playerTeam == PLAYER_4:
                self.player_ui_panel.background_colour = pygame.Color("#D8F8C8")
                self.player_ui_panel_funds.background_colour = pygame.Color("#D8F8C8")

            self.player_ui_panel_funds.rebuild()
            self.player_ui_panel.rebuild()

    def drawBuildingHUD(self,ui_window):
        self.building_manager.draw_ui(ui_window)

    def drawUnitHUD(self,ui_window):
        self.unit_manager.draw_ui(ui_window)

    def drawPlayerHUD(self,ui_window):
        self.player_manager.draw_ui(ui_window)

    def handleBuildingHUDEvents(self,event,playerTeam):
        rowHeight = 40
        padding = 20
        hud_surface = 2
        moveCursor = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveCursor = True
                self.cycleListUnits = (self.cycleListUnits - 1) % len(self.possibleUnits)
                if self.cycleListUnits == -1:
                    self.cycleListUnits = len(self.possibleUnits) - 1
            elif event.key == pygame.K_DOWN:
                moveCursor = True
                self.cycleListUnits = (self.cycleListUnits + 1) % len(self.possibleUnits)

        if moveCursor:
            self.barracks_ui_cursor.set_position((10,padding + rowHeight*(self.cycleListUnits + 1)))
            self.unitHUDImage.set_image(self.imageUnitList[playerTeam][self.cycleListUnits][hud_surface])               
            
    
    def handlePlayerHUDEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.next_player_btn:
                return PLAYING
            elif event.ui_element == self.pause_btn:
                return MENU
            
    def handleUnitHUDEvents(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.moveUnit_btn:
                return MOVE_MODE
            elif event.ui_element == self.attackUnit_btn:
                return ATTACK_MODE
            elif event.ui_element == self.defendUnit_btn:
                return DEFEND_MODE
            elif event.ui_element == self.captureUnit_btn:
                return CAPTURE