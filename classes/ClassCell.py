import random
import sys
from data.Configuration import *

class Cell:
    def __init__(self,tile_options,x,y):
        self.options = tile_options  # List of possible tile options
        self.entropy = len(tile_options)  # Entropy is the number of possible options
        self.pos_x = x
        self.pos_y = y

    def collapse(self):
        if not self.is_collapsed():
            weights = [TILE_ATTRIBUTES[option][0] for option in self.options]
            self.options = random.choices(self.options,weights=weights,k=1)  # Choose one option
            self.entropy = 0

    def add_neighbours(self,neighbours):
        self.neighbours = neighbours

    def reduce_options(self,neighbours_allowed,direction):
        is_reduced = False
        if self.entropy > 0:
            edges = []
            for i in neighbours_allowed:
                edges.append(TILE_RULESET[i][direction])

            if direction == NORTH: opposite_direction = SOUTH
            if direction == SOUTH: opposite_direction = NORTH
            if direction == WEST : opposite_direction = EAST
            if direction == EAST : opposite_direction = WEST

            for option in self.options.copy():
                if TILE_RULESET[option][opposite_direction] not in edges:
                    self.options.remove(option)
                    is_reduced = True
            self.entropy = len(self.options)
        return is_reduced

    def is_collapsed(self):
        return self.entropy == 0
