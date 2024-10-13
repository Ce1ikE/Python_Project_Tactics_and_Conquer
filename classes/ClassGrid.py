import pygame
from classes.ClassCell import Cell
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Grid:
    def __init__(self, width, height, tile_set):
        self.width = width
        self.height = height
        self.tile_set = tile_set  # Dictionary of tile data (neighbors etc.)
        self.grid = [[Cell(list(tile_set.keys())) for _ in range(width)] for _ in range(height)]
        self.plant_seeds()

    def plant_seeds(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or y == self.height - 1 or x == self.width - 1:
                    self.grid[y][x].options = [TILE_MOUNTAIN]
                    self.grid[y][x].collapsed = True
                    self.grid[y][x].entropy = 0
                    self.propagate(x,y)
    
    def get_neighbors(self, x, y):
        neighbors = {}
        if y > 0:  # Up
            neighbors[NORTH] = (y - 1, x)
        if y < self.height - 1:  # Down
            neighbors[SOUTH] = (y + 1, x)
        if x > 0:  # Left
            neighbors[WEST] = (y, x - 1)
        if x < self.width - 1:  # Right
            neighbors[EAST] = (y, x + 1)
        return neighbors
    
    def propagate(self, x, y):
        current_tile = self.grid[y][x].options[0]  # Collapsed cell's tile
        neighbors = self.get_neighbors(x, y)
        
        for direction, (ny, nx) in neighbors.items():
            if not self.grid[ny][nx].is_collapsed():
                allowed_tiles = self.tile_set[current_tile]["allowed_neighbors"][direction]
                # allowed_tiles = [
                #     tile for tile in self.grid[ny][nx].options 
                #     if current_tile in self.tile_set[tile]["allowed_neighbors"][direction]
                # ]
                self.grid[ny][nx].reduce_options(allowed_tiles,x,y)

    def find_lowest_entropy_cell(self):
        min_entropy = float('inf')
        chosen_cell = None
        for y in range(self.height):
            for x in range(self.width):
                if not self.grid[y][x].is_collapsed() and self.grid[y][x].entropy < min_entropy:
                    min_entropy = self.grid[y][x].entropy
                    chosen_cell = (x, y)
        return chosen_cell

    def collapse_wave_function(self):
        while not all(cell.is_collapsed() for row in self.grid for cell in row):
            # Step 1: Find the cell with the lowest entropy
            chosen_cell = self.find_lowest_entropy_cell()
            if not chosen_cell:
                break
            x, y = chosen_cell

            # Step 2: Collapse the chosen cell
            self.grid[y][x].collapse()
            
            # Step 3: Propagate the constraints to neighbors
            self.propagate(x, y)

    def display_grid(self,tile_set_coord,display):
        for y in range(self.height):
            for x in range(self.width):
                image_cell = SpriteSheet(SPRITESHEET_PATH).image_at(tile_set_coord[self.grid[y][x].options[0]])
                display.blit(image_cell, (x * TILESIZE, y * TILESIZE))
                # update the display
                pygame.display.update()

