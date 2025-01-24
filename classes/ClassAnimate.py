import pygame
import pygame_gui
from data.Configuration import *
from classes.ClassSpritesheet import SpriteSheet


class Animation:
    def __init__(self):
        self.captureTimer = 0
        self.captureCounter = 0
        self.counter = 0
        self.offsetSurface = 0
        self.isAnimating = True


        self.attackCounter = 0
        self.attackTimer = 0

        self.landAttackAnimationSprites = SpriteSheet(SPRITESHEET_PATH_UNITS).images_at(LAND_UNIT_DESTRUCTION)

        for sprite  in self.landAttackAnimationSprites: 
            sprite = pygame.transform.scale_by(sprite,TILESIZE/TILESIZE_32)
    
    def animateAttack(self,x,y,window_ui: pygame.Surface):
        if self.isAnimating :
            attackTimeGap = 100
            current_time = pygame.time.get_ticks()
            if current_time - self.attackTimer > attackTimeGap:
                self.attackCounter = (self.attackCounter + 1) % len(LAND_UNIT_DESTRUCTION)
            window_ui.blit(self.landAttackAnimationSprites[self.attackCounter],(x*TILESIZE*SCALETILE,y*TILESIZE*SCALETILE))

            if self.attackCounter == 0 :
                self.isAnimating = False

    def animateRun(self,window_ui: pygame.Surface):
        pass

    def animateDead(self,window_ui: pygame.Surface):
        pass

    def animateCapture(self,window_ui: pygame.Surface):     
        self.isAnimating = False   
        pass
            
            

    


