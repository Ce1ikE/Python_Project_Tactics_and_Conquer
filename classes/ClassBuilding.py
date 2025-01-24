import pygame
import pygame_gui
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Building:
    def __init__(self,buildingType,x,y,team,buildingIndex):
        self.X = x
        self.Y = y
        self.team = team
        self.hitpoints = 20
        self.active = True
        self.buildingType = buildingType
        self.buildingIndex = buildingIndex
        self.buildingSpriteCoord = tileSprites[buildingType]
        self.Buildingpritesheet = SpriteSheet(SPRITESHEET_PATH_TILES).image_at(self.buildingSpriteCoord,colorkey=-1) 
        self.Buildingpritesheet = pygame.transform.scale_by(self.Buildingpritesheet,SCALETILE)

    # most buildings have a 32px by 16px ratio (see => SPRITESHEET_PATH_TILES) so i am not doing any checking wether it is a
    # TILESIZE_32 (32px) or TILESIZE (16px)
    # so if buildings are introduced with other ratios then checking will have to be implementent 
    def drawBuilding(self,x_offset,y_offset,window_ui: pygame.Surface):
        y_blit_offset = -16
        window_ui.blit(self.Buildingpritesheet,((self.X - x_offset)*SCALETILE*TILESIZE,(y_blit_offset * SCALETILE )+ (self.Y - y_offset)*SCALETILE*TILESIZE))

    def showBuildingDetails(self,ui_window: pygame.Surface):
        if self.buildingType in POTENIAL_TRAINING:
            pass
