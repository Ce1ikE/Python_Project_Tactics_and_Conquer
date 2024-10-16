import pygame
import time
from classes.ClassCell import Cell
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Grid:
    def __init__(self, width, height, tile_set,tile_set_coord,ui_window):
        self.width = width
        self.height = height
        self.tile_set = tile_set  # Dictionary of tile data (neighbors etc.)
        self.tile_set_coord = tile_set_coord
        self.ui_window = ui_window
        self.grid = [[Cell(list(tile_set.keys())) for _ in range(width)] for _ in range(height)]
        self.plant_seeds()

    def plant_seeds(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or y == self.height - 1 or x == self.width - 1:
                    self.grid[y][x].options = [TILE_WATER]
                    self.grid[y][x].collapsed = True
                    self.grid[y][x].entropy = 0
                    self.draw_tile(x,y)
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
    
    def propagate(self, x, y,level=0):
        current_tile = self.grid[y][x].options[0]  # Collapsed cell's tile
        neighbors = self.get_neighbors(x, y)
        allowed_tiles = []
        for direction, (ny, nx) in neighbors.items():
            if not self.grid[ny][nx].is_collapsed():
                
                if direction == NORTH: opposite = SOUTH
                if direction == SOUTH: opposite = NORTH
                if direction == WEST : opposite = EAST
                if direction == EAST : opposite = WEST

                for i in range(len(self.tile_set) - 1):
                    if self.tile_set[i][opposite]  in self.tile_set[current_tile][direction]:
                        allowed_tiles.append(self.tile_set[i])
                self.grid[ny][nx].reduce_options(allowed_tiles,x,y)
                # if level < 1:
                #     self.propagate(nx,ny,1)

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
        previous_grid_state = []
        while not all(cell.is_collapsed() for row in self.grid for cell in row):
            # Step 1: Find the cell with the lowest entropy
            chosen_cell = self.find_lowest_entropy_cell()
            if not chosen_cell:
                break
            x, y = chosen_cell

            # Step 2: Copy current grid state to a history (which a copy in order to revert back)
            previous_grid_state.append([[cell for cell in row] for row in self.grid])

            # Step 3: Collapse the chosen cell
            self.grid[y][x].collapse()
            self.draw_tile(x,y)
            
            # Step 4: Propagate the constraints to neighbors
            self.propagate(x, y)

            # Step 5: Check for contradictions
            if self.check_contradiction():
                # Step 6: On contradiction back track
                self.grid = previous_grid_state.pop()
            if self.has_low_entropy():
                self.grid = previous_grid_state.pop()

    def check_contradiction(self):
        for row in self.grid:
            for cell in row:
                # Makes sense because how can a cell be collapse but have no options ?!
                if not cell.is_collapsed() and len(cell.options) == 0:
                    return True
        return False
    
    def has_low_entropy(self, threshold=2):
        for row in self.grid:
            for cell in row:
                if not cell.is_collapsed() and cell.entropy < threshold:
                    return True
        return False

    def draw_tile(self,x,y):
        # draw the chosen cell
        image_cell = SpriteSheet(SPRITESHEET_PATH).image_at(self.tile_set_coord[self.grid[y][x].options[0]],colorkey=(0,0,0))
        self.ui_window.blit(image_cell, (x * TILESIZE, y * TILESIZE))
        # update the display
        pygame.display.update()
        # debugging and nic look (asthetic)
        # time.sleep(0.001)


