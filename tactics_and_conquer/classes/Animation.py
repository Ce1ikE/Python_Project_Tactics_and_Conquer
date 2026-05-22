import pygame
import pygame_gui
from ..configuration import *
from .Spritesheet import SpriteSheet


class Animation:
    """Manage short combat and capture animations on the map."""

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
        """Draw the land-unit destruction animation at the given tile."""
        if self.isAnimating :
            attackTimeGap = 100
            current_time = pygame.time.get_ticks()
            if current_time - self.attackTimer > attackTimeGap:
                self.attackCounter = (self.attackCounter + 1) % len(LAND_UNIT_DESTRUCTION)
            window_ui.blit(self.landAttackAnimationSprites[self.attackCounter],(x*TILESIZE*SCALETILE,y*TILESIZE*SCALETILE))

            if self.attackCounter == 0 :
                self.isAnimating = False

    def animateRun(self,window_ui: pygame.Surface):
        """Placeholder for movement animation hooks."""
        pass

    def animateDead(self,window_ui: pygame.Surface):
        """Placeholder for death animation hooks."""
        pass

    def animateCapture(self,window_ui: pygame.Surface):     
        """Placeholder for capture animation hooks."""
        self.isAnimating = False   
        pass
            
            

    


