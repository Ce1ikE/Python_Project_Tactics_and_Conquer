import pygame
import random
from classes.ClassStack import Stack
from classes.ClassCell import Cell
from classes.ClassMap import Map
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Grid:
    def __init__(self, width, height,ui_window):
        self.cols = width
        self.rows = height
        self.ui_window = ui_window
        self.map = Map()
        self.playersHQ = dict()
        
        # Each cell is initialized with the tile "ruleset" (all possible tiles) and it's neigbouring tiles
        self.grid = [[Cell(list(tileRuleset.keys()),x,y) for x in range(width)] for y in range(height)]


        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.grid[y][x]
                cell.neighbours = self.get_neighbours(x,y)

        self.plant_seeds()

    def plant_seeds(self):
        random_HQ_Red = self.grid[2][random.choice(range(0,WORLD_X))]
        random_HQ_Red.options = [TILE_HQ_RED]
        random_HQ_Red.entropy = 0
        self.draw_tile(random_HQ_Red.pos_x,random_HQ_Red.pos_y)
        self.collapse_neighbours(random_HQ_Red)

        self.playersHQ[0] = (random_HQ_Red.pos_x,random_HQ_Red.pos_y,TILE_HQ_RED)

        random_HQ_Blue = self.grid[WORLD_Y - 2][random.choice(range(0,WORLD_X))]
        random_HQ_Blue.options = [TILE_HQ_BLUE]
        random_HQ_Blue.entropy = 0
        self.draw_tile(random_HQ_Blue.pos_x,random_HQ_Blue.pos_y)
        self.collapse_neighbours(random_HQ_Blue)

        self.playersHQ[1] = (random_HQ_Blue.pos_x,random_HQ_Blue.pos_y,TILE_HQ_BLUE)

    def draw_tile(self,x,y):
        # draw the chosen cell
        # All needed variables and images are copied inside a object "Map" for the game later on
        # the reason i chose to do this is simple a "Grid" object is a object that contains more logic to create a map 
        # rather then the essential information needed to play the game: 
        # (1) the terrain tile type (int) instead of a object (Cell)
        # (2) the image that gives visual info (feedback) to the user on what the terrain type might be (some are indeed ambiguous)
        if(tileSprites[self.grid[y][x].options[0]][3] == TILESIZE):
            y_blit_offset = 0
            image_cell = SpriteSheet(SPRITESHEET_PATH_TILES).image_at(tileSprites[self.grid[y][x].options[0]])
            image_cell = pygame.transform.scale_by(image_cell,SCALETILE)
        
        elif(tileSprites[self.grid[y][x].options[0]][3] == TILESIZE_32):
            y_blit_offset = -16
            image_cell = SpriteSheet(SPRITESHEET_PATH_TILES).image_at(tileSprites[self.grid[y][x].options[0]],colorkey=-1)
            image_cell = pygame.transform.scale_by(image_cell,SCALETILE)
        
        self.ui_window.blit(image_cell, (x * TILESIZE * SCALETILE,(y_blit_offset * SCALETILE) + y * TILESIZE * SCALETILE))
        self.map.mapTerrain[y][x] = self.grid[y][x].options[0]
        self.map.createMapSurface(image_cell,x * TILESIZE * SCALETILE,(y_blit_offset * SCALETILE) + y * TILESIZE * SCALETILE)
        # update the display
        pygame.display.update()

    def copy_map(self):
        """
        :return returns a Map object containing the mapTerrain and the mapSurface:
        """
        return self.map
    
    def copy_playersHQ(self):
        """
        :return returns a dict of tuples with the player's HQ position:
        """
        return self.playersHQ
    
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
    

    # def get_Lowest_Entropy(self):
    #     lowest_Entropy = len(list(tileRuleset.keys()))
    #     for y in range(self.rows):
    #         for x in range(self.cols):
    #             tile_entropy = self.grid[y][x].entropy
    #             if tile_entropy > 0:
    #                 if tile_entropy < lowest_Entropy:
    #                     lowest_Entropy = tile_entropy
    #     return lowest_Entropy
    
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
        
        # heb hier "typing" toegevoegd omdat zo de IDE automatisch de methods en attributes kan zien
        tile_chosen: Cell = random.choice(tiles_Lowest_Entropy)
        tile_chosen.collapse()

        if tile_chosen.options[0] == TILE_BLANK:
            return -1

        self.draw_tile(tile_chosen.pos_x,tile_chosen.pos_y)
        self.collapse_neighbours(tile_chosen)
        return True
    
    def collapse_neighbours(self,tile_chosen):
        stack = Stack()
        stack.push(tile_chosen)
        while stack.is_empty() == False:
            tile: Cell = stack.pop()
            for direction in list(tile.neighbours.keys()):
                if tile.neighbours[direction].entropy != 0:
                    reduced = tile.neighbours[direction].reduce_options(tile.options,direction)
                    if reduced == True:
                        stack.push(tile.neighbours[direction])
    


