from classes.ClassUnit import Unit
from classes.ClassBuilding import *
from data.Configuration import *

class Player:
    def __init__(self,player_number):
        self.player_number = player_number
        self.funds = 1000
        self.playerBuildingsMap = [[ False for x in range(WORLD_X)] for y in range(WORLD_Y)]
        self.buildingsPlayerList = list()

        self.playerUnitsMap =  [[ False for x in range(WORLD_X)] for y in range(WORLD_Y)]
        self.unitsPlayerList = list()

    def endTurn(self,end_turn):
        if end_turn:
            self.funds += 1000*len(self.buildingsPlayerList)
            for unit in self.unitsPlayerList:
                unit.active = True

    def drawUnits(self,x_offset,y_offset,window_ui):
        for unit in self.unitsPlayerList:
            # before blitting a unit to the screen we need to check if it is necessary to blit a unit
            # x_offset & y_offset are the camera coordinates which means i am checking of the
            # X , Y coordinates of the unit are between the current X_s , Y_s screen coordinates  
            if x_offset <= unit.X < WIN_X + x_offset and y_offset <= unit.Y < WIN_Y + y_offset:
                unit.drawUnit(x_offset,y_offset,window_ui)
    
    def drawBuildings(self,x_offset,y_offset,window_ui):
        for building in self.buildingsPlayerList:
            if x_offset <= building.X < WIN_X + x_offset and y_offset <= building.Y < WIN_Y + y_offset:
                building.drawBuilding(x_offset,y_offset,window_ui)

    def addUnit(self,newUnitType,newUnit_x,newUnit_y):
        newUnit = Unit(newUnitType,newUnit_x,newUnit_y,self.player_number,len(self.unitsPlayerList))
        self.unitsPlayerList.append(newUnit)
        self.playerUnitsMap[newUnit_y][newUnit_x] = len(self.unitsPlayerList)

    def removeUnit(self,unitIndex):
        self.unitsPlayerList.remove(unitIndex)

    def addBuilding(self,newBuildingType,newBuilding_x,newBuilding_y):
        newBuilding =  Building(newBuildingType,newBuilding_x,newBuilding_y,self.player_number,len(self.buildingsPlayerList))
        self.buildingsPlayerList.append(newBuilding)
        self.playerBuildingsMap[newBuilding_y][newBuilding_x] = len(self.buildingsPlayerList)

    def removeBuilding(self,x,y,buildingIndex):
        self.playerBuildingsMap.remove(buildingIndex)

    def changeUnitPresence(self,old_x_pos,old_y_pos,new_x_pos,new_y_pos,unitID):
        self.playerUnitsMap[old_y_pos][old_x_pos] = False
        self.playerUnitsMap[new_y_pos][new_x_pos] = unitID
        return True