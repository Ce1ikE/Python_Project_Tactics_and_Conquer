import random
import sys
from data.Configuration import *

class Cell:
    def __init__(self, tile_options):
        self.options = tile_options  # List of possible tile options
        self.collapsed = False  # Whether the cell has collapsed
        self.entropy = len(tile_options)  # Entropy is the number of possible options
    
    def collapse(self):
        if not self.collapsed:
            if len(self.options) > 0:
                weights = [tileWeights[option] for option in self.options]
                self.options = random.choices(self.options,weights=weights,k=1)  # Choose one option
            else:
                self.options = [TILE_BLANK]
            self.collapsed = True
            self.entropy = 0

    def reduce_options(self, valid_options,x,y):
        self.options = [opt for opt in self.options if opt in valid_options]
        self.entropy = len(self.options)  # Update entropy
        if self.entropy == 1:
            self.collapse()

    def is_collapsed(self):
        return self.collapsed
