import pygame
import pygame_gui
from data.Configuration import *





class Cursor:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.cursor_IMG = pygame.image.load("./assets/png/cursor.png")

    def showCursor(self,surface):
        print("showed cursor")
        print((self.X * 16, self.Y * 16))
        surface.blit(self.cursor_IMG, (self.X * TILESIZE, self.Y * TILESIZE))

    def hideCursor():
        print("hide cursor")
        #moeten de cursor overschrijven met iets

    
    def UpdatePosition(self,direction):
        if(direction =="UP"):
            self.Y -= 1
        elif(direction =="DOWN"):
            print("cursor moves down")
            self.Y += 1
            
        elif(direction == "LEFT"):
            print("cursor moves left")
            self.X -= 1

        elif(direction == "RIGHT"):
            print("cursor moves right")
            self.X += 1
        else:
            print("cursor did not get the right argument")
#still needs to check wheter the cursor is out of bounds 
