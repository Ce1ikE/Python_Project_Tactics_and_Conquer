import pygame
from data.Configuration import *
from classes.ClassSpritesheet import SpriteSheet

class Map:
    def __init__(self):
        self.mapSize = (WORLD_X_PX,WORLD_Y_PX)
        self.windowSize = (WIN_X_PX,WIN_Y_PX)
        # dit houd de verschillende afbeeldingen bij die ik vanuit mijn "Grid" object heb gekopieerd
        # dus is dit eigenlijk een grote samenstelling van kleine afbeeldingen
        self.mapSurface = pygame.Surface((self.mapSize))
        
        # a surface that is drawn on top of the window to give a nice 
        # background look when a HUD is opened
        contrast_opacity = 128
        self.contrast_filterMap = pygame.Surface((self.windowSize))
        self.contrast_filterMap.set_alpha(contrast_opacity)
        self.contrast_filterMap.fill((0,0,0))

        # animations that might
        self.captureAnimations = dict()

        self.mapTerrain = [[TILE_BLANK for x in range(WORLD_X)] for y in range(WORLD_Y)]

        image_cell = SpriteSheet(SPRITESHEET_PATH_TILES).image_at(tileSprites[GRASS])
        image_cell = pygame.transform.scale_by(image_cell,SCALETILE)
        for x in range(WORLD_X):
            for y in range(WORLD_Y):
                self.mapSurface.blit(image_cell, (x * TILESIZE * SCALETILE,y * TILESIZE * SCALETILE))

    def createMapSurface(self,image,x,y):
        self.mapSurface.blit(image,(x,y))
    
    # heb hier "typing" toegevoegd omdat zo de IDE automatisch de methods en attributes kan zien
    def drawHUDMap(self,x_offset,y_offset,ui_window: pygame.Surface):
        # eigenlijk geen filter gewoon een tweede surface met een alpha value (opacity)
        # dat op de map surface wordt getekent
        map_rect = pygame.Rect([x_offset*TILESIZE*SCALETILE,y_offset*TILESIZE*SCALETILE,WIN_X_PX,WIN_Y_PX])
        ui_window.blit(self.mapSurface,(0,0),map_rect)
        ui_window.blit(self.contrast_filterMap,(0,0))

    def drawMap(self,x_offset,y_offset,ui_window: pygame.Surface):
        map_rect = pygame.Rect([x_offset*TILESIZE*SCALETILE,y_offset*TILESIZE*SCALETILE,WIN_X_PX,WIN_Y_PX])
        ui_window.blit(self.mapSurface,(0,0),map_rect)



    
