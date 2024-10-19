import pygame
import random
from classes.ClassStack import Stack
from classes.ClassCell import Cell
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Grid:
    def __init__(self, width, height,ui_window):
        self.cols = width
        self.rows = height
        self.ui_window = ui_window
        # Each cell is initialized with the tile "ruleset" (all possible tiles) and it's neigbouring tiles
        self.grid = [[Cell(list(tileRuleset.keys()),x,y) for x in range(width)] for y in range(height)]
        # self.plant_seeds()

        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.grid[y][x]
                cell.neighbours = self.get_neighbours(x,y)

    # def plant_seeds(self):
    #     for y in range(self.rows):
    #         for x in range(self.cols):
    #             if x == 0 or y == 0 or y == self.rows - 1 or x == self.cols - 1:
    #                 self.grid[y][x].options = [TILE_WATER]
    #                 self.grid[y][x].entropy = 0
    #                 self.draw_tile(x,y)
    #                 self.grid[y][x].reduce_options(self.grid[y][x].options,)

    def draw_tile(self,x,y):
        # draw the chosen cell
        image_cell = SpriteSheet(SPRITESHEET_PATH).image_at(tileSprites[self.grid[y][x].options[0]])
        image_cell = pygame.transform.scale_by(image_cell,SCALETILE)
        self.ui_window.blit(image_cell, (x * TILESIZE, y * TILESIZE))
        # update the display
        pygame.display.update()
    
    def get_neighbours(self, x, y):
        neighbours = {}
        if y > 0:  # Up 
            neighbours[NORTH] = self.grid[y - 1][x]
        if y < self.rows - 1:  # Down
            neighbours[SOUTH] = self.grid[y + 1][x]
        if x > 0:  # Left
            neighbours[WEST] = self.grid[y][x - 1]
        if x < self.cols - 1:  # Right
            neighbours[EAST] = self.grid[y][x + 1]
        return neighbours
    

    def get_Lowest_Entropy(self):
        lowest_Entropy = len(list(tileRuleset.keys()))
        for y in range(self.rows):
            for x in range(self.cols):
                tile_entropy = self.grid[y][x].entropy
                if tile_entropy > 0:
                    if tile_entropy < lowest_Entropy:
                        lowest_Entropy = tile_entropy
        return lowest_Entropy
    
    def get_Tiles_Lowest_Entropy(self):
        lowest_Entropy = len(list(tileRuleset.keys()))
        tile_List = []

        for y in range(self.rows):
            for x in range(self.cols):
                tile_entropy = self.grid[y][x].entropy
                if tile_entropy > 0:
                    if tile_entropy < lowest_Entropy:
                        tile_List.clear()
                        lowest_Entropy = tile_entropy
                        tile_List.append(self.grid[y][x])
                    if tile_entropy == lowest_Entropy:
                        tile_List.append(self.grid[y][x])
        return tile_List

    def collapse_wave_function(self):
        # We need to recall upon this function a few times because otherwise the game does not respond
        tiles_Lowest_Entropy = self.get_Tiles_Lowest_Entropy()

        if tiles_Lowest_Entropy == []:
            return False
        
        tile_chosen = random.choice(tiles_Lowest_Entropy)
        tile_chosen.collapse()
        self.draw_tile(tile_chosen.pos_x,tile_chosen.pos_y)

        stack = Stack()
        stack.push(tile_chosen)

        while stack.is_empty() == False:
            tile = stack.pop()
            for direction in list(tile.neighbours.keys()):
                if tile.neighbours[direction].entropy != 0:
                    reduced = tile.neighbours[direction].reduce_options(tile.options,direction)
                    if reduced == True:
                        stack.push(tile.neighbours[direction])


        return True
    


