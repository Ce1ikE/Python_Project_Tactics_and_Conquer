from classes.ClassUnit import Unit

class Player:
    def __init__(self):
        self.player_number = 0
        self.funds = 1000
        # Default 1 because there will be a HQ
        self.buildings = 1
        self.Units = list()

    def endTurn(self,end_turn):
        if end_turn:
            self.funds += 1000*self.buildings
            for unit in self.Units:
                unit.active = True

    def addUnit(self,newUnitType,newUnit_x,newUnit_y):
        newUnit = Unit(newUnitType,newUnit_x,newUnit_y,self.player_number)
        self.Units.append(newUnit)