import pygame
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Cursor:
    def __init__(self,x,y):
        self.X = 0
        self.Y = 0
        self.cursorSpritesheet = SpriteSheet(SPRITESHEET_PATH_CURSOR_2).images_at(CURSOR_SPRITES[0],(0,25))
        for i in range(len(self.cursorSpritesheet.copy())):
            self.cursorSpritesheet[i] = pygame.transform.scale_by(self.cursorSpritesheet[i],SCALETILE/2)

        self.attackCursorSpritesheet = SpriteSheet(SPRITESHEET_PATH_CURSOR_1).images_at(CURSOR_SPRITES[1],colorkey=-1)
        for i in range(len(self.attackCursorSpritesheet.copy())):
            self.attackCursorSpritesheet[i] = pygame.transform.scale_by(self.attackCursorSpritesheet[i],SCALETILE/1.5)

        self.spritesheetTimer = 0
        self.spritesheetCounter = 0
        self.spritesheetTimeGap = 100

        self.cameraSpeed = 200
        self.cursorSpeed = 150
        self.lastMove = 0

        self.cursorCycleList = 0

    def drawCursor(self,ui_window):
        # get the time in milliseconds so if we run the game at 40 frames/sec
        # and want the cursor's image changes every "t" in milliseconds then
        # we need to check if the difference between "current time" and "last time"
        # is greater then then "t" => 
        # current_time - last_time > time_gap
        current_time = pygame.time.get_ticks()
        if current_time - self.spritesheetTimer > self.spritesheetTimeGap:
            self.spritesheetTimer = current_time
            self.spritesheetCounter = (self.spritesheetCounter + 1) % (len(self.cursorSpritesheet))
        ui_window.blit(self.cursorSpritesheet[self.spritesheetCounter], (self.X*TILESIZE*SCALETILE, self.Y*TILESIZE*SCALETILE))

    def drawAttackCursor(self,ui_window):
        current_time = pygame.time.get_ticks()
        if current_time - self.spritesheetTimer > self.spritesheetTimeGap:
            self.spritesheetTimer = current_time
            self.spritesheetCounter = (self.spritesheetCounter + 1) % (len(self.attackCursorSpritesheet))
        ui_window.blit(self.attackCursorSpritesheet[self.spritesheetCounter], (self.X*TILESIZE*SCALETILE, self.Y*TILESIZE*SCALETILE))

    def setPosition(self,camera_x,camera_y,coordinates,keyPress):

        setNextCoord = False
        current_time = pygame.time.get_ticks()
        if current_time - self.lastMove > self.cursorSpeed:
            self.lastMove = current_time

            if keyPress == "up" or keyPress == "right":
                self.cursorCycleList = (self.cursorCycleList + 1) % len(coordinates)
                setNextCoord = True
            elif keyPress == "down" or keyPress == "left":
                self.cursorCycleList = (self.cursorCycleList - 1) % len(coordinates)
                if self.cursorCycleList == -1:
                        self.cursorCycleList = len(coordinates) - 1
                setNextCoord = True

            if setNextCoord :
                newX = coordinates[self.cursorCycleList][0]
                newY = coordinates[self.cursorCycleList][1] 


                if not camera_x <= newX < camera_x + WIN_X:
                    if newX < camera_x:
                        camera_x = newX
                    if camera_x + WIN_X <= newX:
                        camera_x = newX - WIN_X
                
                if not camera_y <= newY < camera_y + WIN_Y:
                    if newY < camera_y:
                        camera_y = newY
                    if camera_y + WIN_X <= newY:
                        camera_y = newY - WIN_X

                self.X = newX - camera_x
                self.Y = newY - camera_y


        return [camera_x,camera_y]

    def cyclePosition(self,camera_x,camera_y,coordinates: list[tuple],keyPress):
        # in order to cycle through a list of coordinates we need to readjust
        # the camera's position and the cursor accordingly  
        # of course first you check whether it was requested by the user to move to the next coordinate
        # in the list => if so:
        
        # (1) check first if the coordinate is in between the current domain or outside
        # dom_x = [camera_x ; camera_x + WIN_X[
        # img_y = [camera_y ; camera_y + WIN_Y[

        # (2) if it is outside of the window check on which part of the domain it is under 
        # (2.1) domain x_left  : -inf;camera_x[  
        # (2.2) domain x_right : ]camera_x + WIN_X ; +inf  
        # (2.3) domain y_left  : -inf;camera_y[  
        # (2.4) domain y_right : ]camera_y ; +inf
         
        # (3) once the game window is readjusted we can set the the cursor coordinates
        # relative to the game window by substracting
        # the new coordinates by the camera_x and camera_y   

        current_time = pygame.time.get_ticks()
        if current_time - self.lastMove > self.cursorSpeed:
            self.lastMove = current_time
            counter = 0
            setNextCoord = False
            if keyPress == "up":
                while counter < len(coordinates) and setNextCoord is False:
                    coord = coordinates[counter]
                    counter += 1 
                    if (coord[0] == camera_x + self.X) and (coord[1] == camera_y + self.Y - 1):
                        setNextCoord = True
                        newCoordinate = coord
                
            elif keyPress == "down":
                while counter < len(coordinates) and setNextCoord is False:
                    coord = coordinates[counter]
                    counter += 1 
                    if (coord[0] == camera_x + self.X) and (coord[1] == camera_y + self.Y + 1):
                        setNextCoord = True
                        newCoordinate = coord

            elif keyPress == "left":
                while counter < len(coordinates) and setNextCoord is False:
                    coord = coordinates[counter]
                    counter += 1 
                    if (coord[0] == camera_x + self.X - 1) and (coord[1] == camera_y + self.Y):
                        setNextCoord = True
                        newCoordinate = coord
            
            elif keyPress == "right":
                while counter < len(coordinates) and setNextCoord is False:
                    coord = coordinates[counter]
                    counter += 1 
                    if (coord[0] == camera_x + self.X + 1) and (coord[1] == camera_y + self.Y):
                        setNextCoord = True
                        newCoordinate = coord

            if setNextCoord:

                if not camera_x <= newCoordinate[0] < camera_x + WIN_X:
                    if newCoordinate[0] < camera_x:
                        camera_x = newCoordinate[0]
                    if camera_x + WIN_X <= newCoordinate[0]:
                        camera_x = newCoordinate[0] - WIN_X
                
                if not camera_y <= newCoordinate[1] < camera_y + WIN_Y:
                    if newCoordinate[1] < camera_y:
                        camera_y = newCoordinate[1]
                    if camera_y + WIN_X <= newCoordinate[1]:
                        camera_y = newCoordinate[1] - WIN_X

                self.X = newCoordinate[0] - camera_x
                self.Y = newCoordinate[1] - camera_y

        return [camera_x,camera_y]

    def UpdatePosition(self,camera_x,camera_y,keyPress):
    # UpdatePosition is just a method to move the camera and the cursor's position
    # depending on where the cursor itself is relative to the window (WIN_X,WIN_y)
    # the camera (aka offset of the window compared to the world map) can only be updated
    # when it isn't equal to the minimum (0) or maximum (CAMERA_X or CAMERA_Y) offset
    # the cursor can only be updated if it hasn't reached the edges of the window yet
    # if it has the camera will be updated and the window moves it's offset
    # see "Schema_Python_Game.png" for more info

        X_delimiter = 3
        Y_delimiter = 3

        current_time = pygame.time.get_ticks()
        if current_time - self.lastMove > self.cursorSpeed:
            self.lastMove = current_time

            if keyPress == "up":
                if camera_y > 0 and 0 == self.Y :
                    camera_y -= 1
                if self.Y > 0:
                    self.Y -= 1

            elif keyPress == "left":
                if camera_x > 0 and 0 == self.X:
                    camera_x -= 1
                if self.X > 0:
                    self.X -= 1

            elif keyPress == "down":
                if camera_y <= CAMERA_Y - 1 and self.Y == WIN_Y - 1:
                    camera_y += 1
                if self.Y < WIN_Y - 1:
                    self.Y += 1

            elif keyPress == "right":
                if camera_x <= CAMERA_X - 1 and self.X == WIN_X - 1:
                    camera_x += 1
                if self.X < WIN_X - 1:
                    self.X += 1

        return [camera_x,camera_y]
