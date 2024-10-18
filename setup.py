from classes.ClassUnit import unit
import pygame
import pygame_gui
import sys
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu
from classes.ClassGame import Game
from pytmx.util_pygame import load_pygame
from data.Configuration import *
Game().createMap()

# test = unit(INFANTRY,[0,0])
# print(test)