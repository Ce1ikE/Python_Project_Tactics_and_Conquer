import pygame
import pygame_gui
from data.Configuration import *

class unit:



    def __init__(self,UnitData: dict, pos: list):
        self.name = UnitData.get("Name")
        self.movement = UnitData.get("movement")
        self.range = UnitData.get("range")
        self.defense = UnitData.get("defense")
        self.type = UnitData.get("type")
        self.pos = [0,0]


    def Spawn():
        print("spawns unit and maintains unit")

    def attack(enemy: 'unit'):
        print("this unit will attack the {enemy} inn this function")

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

    def Travel(position: list):
        print("this function will make the unit travel to {position} coordinates")
        