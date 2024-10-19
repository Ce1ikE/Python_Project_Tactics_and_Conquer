import pygame
import pygame_gui
from data.Configuration import *

class unit:



    def __init__(self,UnitData: dict, x,y,team):
        self.name = UnitData.get("Name")
        self.movement = UnitData.get("movement")
        self.range = UnitData.get("range")
        self.defense = UnitData.get("defense")
        self.type = UnitData.get("type")
        self.x= x
        self.y = y
        self.team = team
        self.active = True
        self.health = 10
        self.Unit_IMG = pygame.image.load("./assets/png/cursor+default.png")

    def Spawn(self,surface):
       #print("unit spawned")
        #print((self.x * TILESIZE, self.y * TILESIZE))
        surface.blit(self.Unit_IMG, (self.x * TILESIZE, self.y * TILESIZE))

    def attack(self, enemy: 'unit'):
        if self.team == enemy.team:
            print("friendly fire")
        else:
            # if check if x or y coordinate is to far do know how to check diagonally
            if abs(self.x - enemy.x) > self.range or abs(self.y - enemy.y) > self.range:

                print("unit to far to attack")
            else:
                print("enemy will be attacked")
                enemy.health -= 10
    def die():
        print("this function runs when a unit dies and is removed from screen")

    def inactive():
        print("this function wil run when the unit attacked or traveled until next round this unit will be inactive")

    def active():
        print("this function will reactivate the inactive units from previous round")

    def ShowTravelZone():
        print("this function show the possible travel distance and routes")

    def ShowAttackZone():
        print("this function will show the possible attack range")

    def ShowMenu():
        print("this function will show a menu with information about the unit")

    def Travel(x,y):
        print("this function will make the unit travel to {position} coordinates")
        
