import pygame, sys
from pytmx.util_pygame import load_pygame
from classes.ClassCursor import Cursor
from classes.ClassUnit import unit

from data.Configuration import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((1280,720))
tmx_data = load_pygame('./assets/Debug_map/Debug_map.tmx')
sprite_group = pygame.sprite.Group()
Cursor = Cursor(1,1)
unit = unit(INFANTRY,2,3,1)

# cycle through all layers
for layer in tmx_data.visible_layers:
    for x,y,surf in layer.tiles():
        pos = (x * 16, y * 16)
        Tile(pos = pos, surf = surf, groups = sprite_group)
        print(pos)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				Cursor.UpdatePosition("UP")
			elif event.key == pygame.K_DOWN:
				Cursor.UpdatePosition("DOWN")
			elif event.key == pygame.K_LEFT:
				Cursor.UpdatePosition("LEFT")
			elif event.key == pygame.K_RIGHT:
				Cursor.UpdatePosition("RIGHT")
	screen.fill('black')
	sprite_group.draw(screen)
	Cursor.showCursor(screen)
	unit.Spawn(screen)

	pygame.display.update()
	
#https://www.youtube.com/watch?v=N6xqCwblyiw

