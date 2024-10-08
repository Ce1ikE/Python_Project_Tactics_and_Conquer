import pygame
import sys


#een object game
class Game:
    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption("tactics & Conquer")
        self.screen = pygame.display.set_mode((640,480))


        self.clock =pygame.time.Clock()

    def run(self):
    # de run functie runt de game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)




Game().run()
