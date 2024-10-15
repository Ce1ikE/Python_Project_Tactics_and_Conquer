import pygame
import pygame_gui
from data.Configuration import *


class Cursor:

    def __init__(self,pos: list) -> None:
        self.position = pos





    def showCursor():
        print("showed cursor")

    def hideCursor():
        print("hide cursor")

    
    def UpdatePosition(direction):
        if(direction =="UP"):
            print("cursor moves up")
        elif(direction =="DOWN"):
            print("cursor moves down")
        elif(direction == "LEFT"):
            print("cursor moves left")
        elif(direction == "RIGHT"):
            print("cursor moves right")
        else:
            print("cursor did not get the right argument")

