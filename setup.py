from classes.ClassUnit import unit
import pygame
import pygame_gui
import sys
from classes.ClassGrid import Grid
from classes.ClassMenu import Menu

from data.Configuration import *
#Game().createMap()

team1 = unit(INFANTRY,0,0,1)
team2 = unit(INFANTRY,1,0,2)

team1.attack(team2)
