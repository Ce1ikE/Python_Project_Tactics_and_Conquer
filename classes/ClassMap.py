from data.Configuration import *
import pygame
class Map:
    def __init__(self):
        self.mapSize = (WORLD_X_PX,WORLD_Y_PX)
        self.mapTerrain = list()
        self.mapSurface = pygame.Surface((self.mapSize))
        self.mapTerrain = list()
        self.mapUnits = list([[ False for x in range(WORLD_X)] for y in range(WORLD_Y)])
        self.mapBuildings = list()

    def drawMap(self,x_offset,y_offset,ui_window):
        map_rect = pygame.Rect([x_offset*TILESIZE*SCALETILE,y_offset*TILESIZE*SCALETILE,WIN_X_PX,WIN_Y_PX])

        ui_window.blit(self.mapSurface,(0,0),map_rect)

    def createMapSurface(self,image,x,y):
        self.mapSurface.blit(image,(x,y))