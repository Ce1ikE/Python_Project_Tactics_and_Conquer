import pygame
import random
from classes.ClassStack import Stack
from classes.ClassCell import Cell
from classes.ClassMap import Map
from classes.ClassPlayer import Player
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *


# so first what is the "grid" class ? 
# -> Well in order to play this game you need a map.

# Well how do create a map ?
# -> You can use different methods to create a map
# most basic map creation would be a hardcoded one (but that is of course not scalable and you would need a way to store these static maps => en dat wil ik niet doen) 
# Of course we are going to use a algorithm !

# What kind of algorithm ?
# -> There are a lot to choose from but the one i am most familiar with is the "Wave function collapse" algorithm.
# If you know a little bit about physics , more particularly quantum physics , this might ring a bell. However i must tell you
# that this algorithm involves anything but physics (sorry).
# There also many (like many) more variations of this algorithm , some more straightforward , some more optimized
# Other examples:
# => https://dev.to/kavinbharathi/the-fascinating-wave-function-collapse-algorithm-4nc3
# => https://github.com/Coac/wave-function-collapse
# these are all python implementations but this algorithm has been implemented in a lot of different languages:
# => (*) https://github.com/mxgmn/WaveFunctionCollapse
#
#
# "Oskar Stålberg", you might know him (he is the guy that created "Bad North" and "Townscaper")
# i recommend you check him out (he's done a lot more since then), he implemented this functionality in his games to create different maps 
# in his game
# => https://www.tumblr.com/oskarstalberg
#
# Townscaper 
# => https://oskarstalberg.com/Townscaper/
#
# Also there are lot more different kind of algorithms 
# like i watched "Ici Amy Plant" (https://www.youtube.com/@iciamyplant) on Youtube using the "Bruit de Perlin" algorithm
# fascinating video:
# => https://www.youtube.com/watch?v=CY4wxHPVXiQ
# here are some other procedural map generation algorithms
# => https://christianjmills.com/posts/procedural-map-generation-techniques-notes/
# 
# There is actually a nice paper by "Paul C. Merrell" on this which goes in detail on this kinds of algorithms:
# see => https://paulmerrell.org/wp-content/uploads/2021/06/thesis.pdf
# while he didn't called it the WFC he was the firts one describing this kind of algorithm. He named it "Model synthesis"
# it was "Maxim Gumin" who later published an implementation on Github (see link above (*)).

# How did it work out for you ?
# -> Well it was not easy at first because i started out on the wrong foot
# i started coding my tile constraints (the "rules" of the algorithm to follow) based on each possible tile that could be on the left , right , up or down of that tile:
# left      : [x,y,z,...]
# right     : [a,x,z,...]
# up        : [w,b,c,...]
# down      : [x,y,w,...]
# this quickly became a big mess and it is difficult to keep track which tile is connected to which tile
# "The Coding Train" on Youtube also started out this way actually but also realised that makes the algorithm not scalable when more then 20 tiles are involved
# https://www.youtube.com/watch?v=rI_y2GAlQFM     
# The moment you realise that you have to insert the tiles edges and to check for matching tiles that have the matching edge in common in the opposite direction 
# is like magic. Once you establish this concept the understanding of the algorithm clears up.
# my implementation of the algorithm is actually based upon this guy's code however tweaked to my liking
# => https://github.com/CodingQuest2023/Algorithms/tree/main

# the algorithm goes as follows:
# ------------------------------
# (1) initiate EVERY cell in the grid with a all possible tiles in your ruleset
# this means that you assume that at the very beggining any cell can be any tile

# (2) choose a cell with the lowest "entropy" and "collapse" this cell to single tile. 
# This means we simply choose a cell with the fewest possible options and choose a random tile
# out of the options this cell has remaining. This cell will now have this tile as value 

# (3) take the "collapsed" cell's neighbouring cells and reduce the amount of possible options they have 
# based upon the edges the "collapsed" cell now has, in order to constrain the possible options the neigbouring cells have

# (4) repeat step (3) until no cell's options can constrained. This step is called "propagation"

# (5) check if all cells have only 1 option remaining. 
# If not repeat step (2), (3), (4) and (5)
# If all cells are "collapsed" the map has been generated

# !! NOTE: for step (2) steps it might be you start out with a empty grid (no seeds planted) 
# which means that any cell can be has the same "entropy" and so the same amount of chance to be "collapsed"

# there are definitly pro and cons using this algorithm
# what I would consider a pro is that it is easy to set up for someone as my with little to no game developement at all
# and it's very easy to understand
# a con would be that it's actually very expensive computational-wise. With that i mean that because of the fact you can run 
# into a contradiction and because it is difficult to see when this contradiction has occured or when the "seed" of the contradiction occured
# you are obliged to restart the whole generation. furthermore the "propagation" fase is also very expensive because evry iteration you need to go over your
# map array which isn't a problem for small maps and small project like this one. But think about this in a 3D world.(think minecraft !!)
# To generate a 3D mesh you need to increase your number of "cells" (i guess polygons in 3D) by the number of layers you would like to have.
# the paper i have linked by "Paul C. Merrell" talks about this in section 4.8.2
# and so this doesn't fit a scenario where you need a real-life update every single time you get further into the map
# also if the number of possible tiles increase and the dimensions increase as well this algorithm doesn't become as effecient as others out there
# ENJOY the "grid" class 

class Grid:
    def __init__(self, width: int, height: int,ui_window,playerList: list[Player],map: Map):
        self.playerList: list[Player] = playerList
        self.cols: int = width
        self.rows: int = height
        self.ui_window: pygame.Surface = ui_window
        self.map: Map = map
        self.buildingListSprites = list()
        
        # Each cell is initialized with the tile "ruleset" (all possible tiles) and it's neigbouring tiles
        self.grid = [[Cell(list(TILE_RULESET.keys()),x,y) for x in range(width)] for y in range(height)]


        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.grid[y][x]
                cell.neighbours = self.get_neighbours(x,y)

        self.plant_seeds()

    # when you "plant seeds" you're just hard coding or performing a other algorithm 
    # to predefine certain cells before hand 
    def plant_seeds(self):
        self.place_hq()
        self.place_cities()

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
        
        # blit to window
        self.ui_window.blit(image_cell, (x * TILESIZE * SCALETILE,(y_blit_offset * SCALETILE) + y * TILESIZE * SCALETILE))
        # update the display
        pygame.display.update()

        
        # every single tile's image/sprite generated by the WFC algorithm is copied to a big pygame surface which is our world
        self.map.createMapSurface(image_cell,x * TILESIZE * SCALETILE,(y_blit_offset * SCALETILE) + y * TILESIZE * SCALETILE)

        # the terrain type as well is copied inside the Map object for later use
        if self.grid[y][x].options[0] in [TILE_HQ_RED, TILE_HQ_BLUE,TILE_HQ_YELLOW,TILE_HQ_GREEN]:
            self.map.mapTerrain[y][x] = TILE_HQ
        else :
            self.map.mapTerrain[y][x] = self.grid[y][x].options[0]

        if self.grid[y][x].options[0] in POTENIAL_CAPTURES:
            self.buildingListSprites.append((image_cell,x * TILESIZE * SCALETILE,(y_blit_offset * SCALETILE) + y * TILESIZE * SCALETILE))

    def validate_map(self):

        for y in range(self.rows):
            for x in range(self.cols):
                if self.map.mapTerrain[y][x] == TILE_BLANK:
                    return False
        
        # the reason to reblit the builf-dings is due to their size which 32px by 16px
        # a normal tile is 16px by 16px which means it could (highly probable) that other tiles have "corrupted" (blitted over)
        # the buildings tiles
        for sprite in self.buildingListSprites:
            self.map.createMapSurface(sprite[0],sprite[1],sprite[2])
            # update the display
            pygame.display.update()
        
        return True

    def place_hq(self):
        hq_tiles = [TILE_HQ_RED, TILE_HQ_BLUE,TILE_HQ_YELLOW,TILE_HQ_GREEN]
        positions = []

        hq_placed = False

        # randomly select valid positions for each HQ
        # well.. not really random
        for player in range(N_PLAYERS):
            hq_placed = False
            while hq_placed is False :
                x = random.randint(1, self.cols - 2)
                y = random.randint(1, self.rows - 2)
                if not any((x, y) in pos for pos in positions):
                    positions.append((x, y))
                    self.playerList[player].addBuilding(hq_tiles[player],x,y)
                    self.grid[y][x].options = [hq_tiles[player]]
                    self.grid[y][x].entropy = 0
                    self.draw_tile(x, y)
                    self.collapse_neighbours(self.grid[y][x])
                    hq_placed  = True
                    self.place_barracks(x,y)
                

    def place_cities(self):
        num_cities = 10
        cities_placed = 0
        while cities_placed < num_cities:
            x = random.randint(2, self.cols - 3)
            y = random.randint(2, self.rows - 3)
            # a cell is collapsed when onle ONE options remains
            # because we are in the initial state of the program
            if not self.grid[y][x].is_collapsed():
                self.grid[y][x].options = [TILE_CITY]
                self.grid[y][x].entropy = 0
                self.draw_tile(x, y)
                self.collapse_neighbours(self.grid[y][x])
                cities_placed += 1
            
    
    def place_barracks(self,x_HQ,y_HQ):
        hq_barracks_spacing = 4
        barracks_placed = 0
        while barracks_placed < 2:
            # place barracks next to HQ
            bx = x_HQ + random.randint(-hq_barracks_spacing, hq_barracks_spacing)  
            by = y_HQ + random.randint(-hq_barracks_spacing, hq_barracks_spacing)
            if 0 <= bx < self.cols - 1 and 0 <= by < self.rows - 1:
                if not self.grid[by][bx].is_collapsed():

                    self.grid[by][bx].options = [TILE_BARRACKS]
                    self.grid[by][bx].entropy = 0
                    self.draw_tile(bx, by)
                    self.collapse_neighbours(self.grid[by][bx])
                    barracks_placed += 1

    
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
    
    def get_Tiles_Lowest_Entropy(self):
        lowest_Entropy = len(list(TILE_RULESET.keys()))
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
            return 0
        
        # heb hier "typing" toegevoegd omdat zo de IDE automatisch de methods en attributes kan zien
        tile_chosen: Cell = random.choice(tiles_Lowest_Entropy)
        tile_chosen.collapse()

        if tile_chosen.options[0] == TILE_BLANK:
            return -1

        self.draw_tile(tile_chosen.pos_x,tile_chosen.pos_y)
        self.collapse_neighbours(tile_chosen)
        return 1
    
    def collapse_neighbours(self,tile_chosen):

        # the reason you would like to have a stack is when you through the Cells recursively 
        # you need a way to backtrack in your propagation
        # example:
        # cell "A" was "collapsed" which means that ALL this cell's neighbouring cell's options need to be reduced (or at least try it could be that all possibilities are valid) 
        # so when you choose a neigbouring cell to reduce it's options you need to check again if that cell's , let's call it "B" , neighbouring cells also need to be reduced
        # and so on.
        # So you and up whith a chain of cells until you find a cell "Z" that can't be reduced
        # afterwards you can take this cell of the stack and check the previous cell's remaining neighbours
        # A -> B -> ... -> N_(x)
        # A -> B -> ... -> N_(x - 1)
        # until no more remains
        # A -> B -> ... -> N_(x - k)
        # A -> B
        # A
        # 0 == empty stack
        stack = Stack()
        stack.push(tile_chosen)
        while stack.is_empty() == False:
            tile: Cell = stack.pop()
            for direction in list(tile.neighbours.keys()):
                if tile.neighbours[direction].entropy != 0:
                    reduced = tile.neighbours[direction].reduce_options(tile.options,direction)
                    if reduced == True:
                        stack.push(tile.neighbours[direction])
    


