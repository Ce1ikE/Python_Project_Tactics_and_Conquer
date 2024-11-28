import pygame
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Cursor:
    def __init__(self,x,y):
        self.X = 0
        self.Y = 0
        self.cursorSpritesheet = SpriteSheet(SPRITESHEET_PATH_CURSOR_2).images_at(CursorSprites[0],(0,25))
        for i in range(len(self.cursorSpritesheet.copy())):
            self.cursorSpritesheet[i] = pygame.transform.scale_by(self.cursorSpritesheet[i],SCALETILE/2)
        self.spritesheetTimer = 0
        self.spritesheetCounter = 0
        self.spritesheetTimeGap = 200

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

    def setPosition(self,event,camera_x,camera_y,newX,newY):
        if event.key == pygame.K_UP:
            if camera_y > 0 and 0 == self.Y:
                camera_y -= 1
            if self.Y > 0:
                self.Y -= 1
        elif event.key == pygame.K_LEFT:
            if camera_x > 0 and 0 == self.X:
                camera_x -= 1
            if self.X > 0:
                self.X -= 1
        elif event.key == pygame.K_DOWN:
            if camera_y <= CAMERA_Y - 1 and self.Y == WIN_Y - 1:
                camera_y += 1
            if self.Y < WIN_Y - 1:
                self.Y += 1
        elif event.key == pygame.K_RIGHT:
            if camera_x <= CAMERA_X - 1 and self.X == WIN_X - 1:
                camera_x += 1
            if self.X < WIN_X - 1:
                self.X += 1
        return [camera_x,camera_y]

    def UpdatePosition(self,event,camera_x,camera_y):
        if event.key == pygame.K_UP:
            if camera_y > 0 and 0 == self.Y :
                camera_y -= 1
            if self.Y > 0:
                self.Y -= 1
        elif event.key == pygame.K_LEFT:
            if camera_x > 0 and 0 == self.X:
                camera_x -= 1
            if self.X > 0:
                self.X -= 1
        elif event.key == pygame.K_DOWN:
            if camera_y <= CAMERA_Y - 1 and self.Y == WIN_Y - 1:
                camera_y += 1
            if self.Y < WIN_Y - 1:
                self.Y += 1
        elif event.key == pygame.K_RIGHT:
            if camera_x <= CAMERA_X - 1 and self.X == WIN_X - 1:
                camera_x += 1
            if self.X < WIN_X - 1:
                self.X += 1
        return [camera_x,camera_y]
