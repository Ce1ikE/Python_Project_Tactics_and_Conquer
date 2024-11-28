import pygame
import pygame_gui
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Unit:
    def __init__(self,unitData: dict, x,y,team,unitIndex):
        self.movement = unitData.get("movement")
        self.range = unitData.get("range")
        self.defense = unitData.get("defense")
        self.type = unitData.get("type")
        self.damage = unitData.get("base_damage")
        self.X = x
        self.Y = y
        self.team = team
        self.unitIndex = unitIndex
        self.active = True
        self.direction = WEST
        self.health = 10

        # here i process the Unit's spritesheets to get the right size and scale (for example : scale_by => SCALETILE and -1,1)
        # this looks like a lot but needed in order to avoid processing the sprites during the blitting process (which could prove to be cumbersome)
        unitsSprites: list[list] = unitData.get("spritesheet")
        for i in range(0,4):
            unitsSprites[i*3].extend([TILESIZE_24,TILESIZE_24])
            unitsSprites[i*3 + 1].extend([TILESIZE_24,TILESIZE_24])
            unitsSprites[i*3 + 2].extend([TILESIZE_24,TILESIZE_24])
        for i in range(4,8):
            unitsSprites[i*3].extend([TILESIZE,TILESIZE])
            unitsSprites[i*3 + 1].extend([TILESIZE,TILESIZE])
            unitsSprites[i*3 + 2].extend([TILESIZE,TILESIZE])
        # once i have added the correct surface offset i let the SpriteSheet class handle the rest to get the correct SubSurfaces
        # from my Unit's spritesheet (which is a big one (like really big))
        self.Unitspritesheet = SpriteSheet(SPRITESHEET_PATH_UNITS).images_at(unitsSprites,colorkey=-1) 
        # units sprites 3+n 5+n 7+n where n [0;2] must have a pygame.transform.scale_x(-1) applied since they are suppose to represent the other direction
        for n in range(0,4):
            self.Unitspritesheet[3 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)
            self.Unitspritesheet[5 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)
            self.Unitspritesheet[7 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)

        padding = 15
        unitNameSprite = unitData.get("Name")
        nameTag = SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(unitNameSprite,colorkey=-1)

        self.UnitDetails = pygame.Surface((TILESIZE_32 + 2*padding,2*TILESIZE_24))
        self.UnitDetails.set_alpha(128)
        self.UnitDetails.fill((0,0,0))
        # i only need the [IDLE_L_1] image/spritesheet for the unitdetails
        # i want the unit's nametag to be placed i the middle , Top of the unitDetails
        # and the unit's [IDLE_L_1] sprite right beneath it so the nametag will be offset
        # from the left top corner of the unitDetails surface by a padding distance both in the X, Y direction
        # afterwards the sprite of the unit will have a offset of padding + TILESIZE/2 i want the sprite to be placed
        # in the middle of the nameTag => which is 32px in the X direction
        # the unit's sprite must then be offset in the Y direction by padding + TILESIZE => right beneath the name tag
        self.UnitDetails.blit(self.Unitspritesheet[12],(padding + 8,padding + TILESIZE))
        self.UnitDetails.blit(nameTag,(padding,padding))

        # it's easier to first place everything correctly relative
        for i in range(len(self.Unitspritesheet.copy())):
            self.Unitspritesheet[i] = pygame.transform.scale_by(self.Unitspritesheet[i],SCALETILE)
        # self.UnitDetails = pygame.transform.scale_by(self.UnitDetails,SCALETILE)

        self.spritesheetCounter = 0
        self.spritesheetTimer = 0
        self.spritesheetTimeGap = 1000

    # most units and their state have a 16px by 16px ratio (see => SPRITESHEET_PATH_UNITS) 
    # but some states as the UP,RIGHT,DOWN,LEFT have a 24px by 16px ratio wich means it will have to be blitted
    # by a negative "y" y_offset = -8*SCALETILE (see => "Grid" class => method draw_tile) 
    def drawUnit(self,x_offset,y_offset,window_ui: pygame.Surface):
        current_time = pygame.time.get_ticks()
        if current_time - self.spritesheetTimer > self.spritesheetTimeGap:
            self.spritesheetTimer = current_time
            self.spritesheetCounter = (self.spritesheetCounter + 1) % 3

        if self.active:
            window_ui.blit(self.Unitspritesheet[15 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))
        else :
            window_ui.blit(self.Unitspritesheet[21 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))

    def attack(self, enemy: 'Unit'):
        pass

    def die(self):
        pass

    def showTravelZone(self,x_offset,y_offset,window_ui : pygame.Surface):
        movementTile = pygame.Surface((TILESIZE*SCALETILE,TILESIZE*SCALETILE))
        movementTile.set_alpha(128)
        movementTile.fill((255,255,255))
        for x in range(self.movement):
            for y in range(self.movement):
                if (x + y) <= abs(self.movement) and x_offset <= self.X < WIN_X + x_offset and y_offset <= self.Y < WIN_Y + y_offset:
                    movementTile_x = self.X - x_offset + x
                    movementTile_y = self.Y - y_offset + y
                    window_ui.blit(movementTile,(movementTile_x,movementTile_y))

    def getTravelZone(self):
        travelPossibilities = list()
        # movement zone range is from [- movement , movement]
        for x in range(self.movement):
            for y in range(self.movement):
                if abs(x + y) <= self.movement and 0 < self.X + x < WORLD_X and 0 < self.Y + y < WORLD_Y:
                    travelPossibilities.append((self.X + x,self.Y + y))
        return travelPossibilities

    def showAttackZone(self,x_offset,y_offset,window_ui : pygame.Surface):
        attackTile = pygame.Surface((TILESIZE*SCALETILE,TILESIZE*SCALETILE))
        attackTile.set_alpha(128)
        attackTile.fill((255,255,255))
        for x in range(self.range):
            for y in range(self.range):
                if (x + y) <= abs(self.range) and x_offset <= self.X < WIN_X + x_offset and y_offset <= self.Y < WIN_Y + y_offset:
                    attackTile_x = self.X - x_offset + x
                    attackTile_y = self.Y - y_offset + y
                    window_ui.blit(attackTile,(attackTile_x,attackTile_y))

    def getAttackZone(self):
        attackPossibilities = list()
        # attack zone range is from [- range , range]
        for x in range(-self.range,self.range + 1):
            for y in range(-self.range,self.range + 1):
                if abs(x + y) <= self.range and 0 < self.X + x < WORLD_X and 0 < self.Y + y < WORLD_Y:
                    attackPossibilities.append((self.X + x,self.Y + y))
        return attackPossibilities

    def showUnitsDetails(self,window_ui : pygame.Surface):
        padding = 15
        window_ui.blit(self.UnitDetails,(WIN_X_PX - (2*TILESIZE + padding)*SCALETILE,WIN_Y_PX - (3*TILESIZE)*SCALETILE))
   
    def travel(self,x,y):
        print("this function will make the unit travel to {position} coordinates")
        self.active = False
        
