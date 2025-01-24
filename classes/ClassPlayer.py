import pygame
from classes.ClassUnit import Unit
from classes.ClassBuilding import Building
from data.Configuration import *

class Player:
    def __init__(self,player_number):
        self.player_number = player_number
        self.funds = 1000
        # houd bij waar een gebouw zich bevind dat van dit "Player" object is
        self.playerBuildingsMap = [[ False for x in range(WORLD_X)] for y in range(WORLD_Y)]
        # houd bij waar een eenheid zich bevind dat van dit "Player" object is
        self.playerUnitsMap =  [[ False for x in range(WORLD_X)] for y in range(WORLD_Y)]

        # a player keeps track of it's units and buildings
        self.buildingsPlayerList: dict[int,Building] = dict()
        self.unitsPlayerList: dict[int,Unit] = dict()
        self.captureAnimations: dict = dict()

        self.unitID     = 1
        self.buildingID = 1

    def endTurn(self,end_turn):
        if end_turn:
            self.funds += 1000*len(self.buildingsPlayerList)
            for unit in self.unitsPlayerList.values():
                unit.active = True

    def drawUnits(self,x_offset,y_offset,window_ui,unitDetailsSprites: dict):
        for unit in self.unitsPlayerList.values():
            # before blitting a unit to the screen we need to check if it is necessary to blit a unit
            # x_offset & y_offset are the camera coordinates which means i am checking if the
            # X , Y coordinates of the unit are between the current X_s , Y_s screen coordinates  
            if x_offset <= unit.X < WIN_X + x_offset and y_offset <= unit.Y < WIN_Y + y_offset:
                unit.drawUnit(x_offset,y_offset,window_ui,unitDetailsSprites,self.captureAnimations)
    
    def drawBuildings(self,x_offset,y_offset,window_ui):
        for building in self.buildingsPlayerList.values():
            if x_offset <= building.X < WIN_X + x_offset and y_offset <= building.Y < WIN_Y + y_offset:
                building.drawBuilding(x_offset,y_offset,window_ui)

    def addUnit(self,newUnitType,newUnit_x,newUnit_y):
        newUnit = Unit(
            newUnitType,
            newUnit_x,
            newUnit_y,
            self.player_number,
            self.unitID
        )
        self.playerUnitsMap[newUnit_y][newUnit_x] = self.unitID
        self.unitsPlayerList[self.unitID] = newUnit
        self.unitID += 1

    def removeUnit(self,unitID: int):
        self.unitsPlayerList.pop(unitID)

    def addBuilding(self,newBuildingType,newBuilding_x,newBuilding_y):
        newBuilding = Building(
            newBuildingType,
            newBuilding_x,
            newBuilding_y,
            self.player_number,
            self.buildingID
        )
        self.playerBuildingsMap[newBuilding_y][newBuilding_x] = self.buildingID
        self.buildingsPlayerList[self.buildingID] = newBuilding
        self.buildingID += 1

    def removeBuilding(self,buildingID: int):
        self.playerBuildingsMap.pop(buildingID)

    def changeUnitPresence(self,old_x_pos,old_y_pos,new_x_pos,new_y_pos,unitID):
        self.playerUnitsMap[old_y_pos][old_x_pos] = False
        self.playerUnitsMap[new_y_pos][new_x_pos] = unitID
        self.unitsPlayerList[unitID].travel(new_x_pos,new_y_pos)
        return True