import pygame
import pygame_gui
import random
import copy
from classes.ClassMap import Map  
from classes.ClassSpritesheet import SpriteSheet
from data.Configuration import *

class Unit:
    def __init__(self,unitData: dict,x,y,team,unitID):
        
        self.movement: int = unitData.get("movement")
        self.range: int = unitData.get("range")
        self.defense: int = unitData.get("defense")
        self.unitType = unitData.get("unitType")
        self.type: int = unitData.get("type")
        self.damage: list = unitData.get("base_damage")
        
        self.unitID = unitID
        self.X = x
        self.Y = y        
        self.team: int = team
        self.active = True
        self.isCapturing = False
        self.capturedBuildingHealth = 20
        self.direction = WEST
        self.health = 10

        # here i process the Unit's spritesheets to get the right size and scale (for example : scale_by => SCALETILE and -1,1)
        # this looks like a lot, but required/needed in order to avoid processing the sprites during the blitting process (which could prove to be cumbersome)
        unitsSprites: list[list] = copy.deepcopy(unitData.get("spritesheet"))
        
        for i in range(0,12):
            # the first 12 [0 ; 12[ coodinates are 24px based tile/sprite
            unitsSprites[i][0] = unitsSprites[i][0] + PLAYERS_SPRITESHEET_OFFSET[self.team][0]
            unitsSprites[i][1] = unitsSprites[i][1] + PLAYERS_SPRITESHEET_OFFSET[self.team][1]
            # the next 12 [12 ; 24[ coordinates are a 16px based tile/sprite
            unitsSprites[i + 12][0] = unitsSprites[i + 12][0] + PLAYERS_SPRITESHEET_OFFSET[self.team][0]
            unitsSprites[i + 12][1] = unitsSprites[i + 12][1] + PLAYERS_SPRITESHEET_OFFSET[self.team][1]
        

        # once i have added the correct surface offset i let the SpriteSheet class handle the rest to get the correct SubSurfaces
        # from my Unit's spritesheet (which is a big one (like really big))
        self.Unitspritesheet = SpriteSheet(SPRITESHEET_PATH_UNITS).images_at(unitsSprites,colorkey=-1) 
        # units sprites 3+n 5+n 7+n where n [0;2] must have a pygame.transform.scale_x(-1) applied since they are suppose to represent the other direction
        for n in range(0,4):
            self.Unitspritesheet[3 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)
            self.Unitspritesheet[5 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)
            self.Unitspritesheet[7 + n] = pygame.transform.flip(self.Unitspritesheet[3 + n],True,False)

        panel_width = 150
        panel_height = 200
        nameTag_width = 80
        image_width = 50
        healthTag_width = 25

        self.unitManager = pygame_gui.UIManager((WIN_X_PX,WIN_Y_PX),theme_path="./data/Tactics_and_Conquer_style.json")
        self.unitPanel_el = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((WIN_X_PX - panel_width,WIN_Y_PX - panel_height),(panel_width,panel_height)),
            manager=self.unitManager,
            object_id=pygame_gui.core.ObjectID(object_id="#HUD_unitPanel")
        )
        
        unitNameSprite = unitData.get("name")
        nameTag = SpriteSheet(SPRITESHEET_PATH_UNITS).image_at(unitNameSprite,colorkey=-1)
        self.unitImage = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(((panel_width - image_width)/2,nameTag_width/2),(image_width,image_width)),
            manager=self.unitManager,
            container=self.unitPanel_el,
            image_surface=pygame.transform.scale_by(self.Unitspritesheet[12],image_width/SCALETILE)
        )
        self.unitLabel = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(((panel_width - nameTag_width)/2,20),(nameTag_width,nameTag_width/2)),
            manager=self.unitManager,
            container=self.unitPanel_el,
            image_surface=pygame.transform.scale_by(nameTag,nameTag_width/SCALETILE)
        )
        
        healthTag = SpriteSheet(SPRITESHEET_PATH_HUD_GENERAL_ICONS).image_at([163,133,14,14],colorkey=-1)
        self.unitHealthTag = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(((panel_width - nameTag_width)/2 - healthTag_width,panel_height - image_width),(healthTag_width,healthTag_width)),
            manager=self.unitManager,
            container=self.unitPanel_el,
            image_surface=pygame.transform.scale_by(healthTag,healthTag_width/SCALETILE)
        )

        self.unitHealthImage = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(((panel_width - nameTag_width)/2 + healthTag_width,panel_height - image_width),(healthTag_width,healthTag_width)),
            manager=self.unitManager,
            container=self.unitPanel_el,
            image_surface=pygame.transform.scale_by(healthTag,healthTag_width/SCALETILE)
        )

        for i in range(len(self.Unitspritesheet.copy())):
            self.Unitspritesheet[i] = pygame.transform.scale_by(self.Unitspritesheet[i],SCALETILE)

        self.spritesheetCounter = 0
        self.spritesheetTimer = 0
        self.captureTimer = 0
        self.captureCounter = 0

    def drawUnit(self,x_offset,y_offset,window_ui: pygame.Surface,unitDetailsSprites_Numbers: dict,unitDetailsSprites_Captures: dict):
        # most units and their state have a 16px by 16px ratio (see => SPRITESHEET_PATH_UNITS) 
        # but some states as the UP,RIGHT,DOWN,LEFT have a 24px by 16px ratio wich means it will have to be blitted
        # by a negative "y" y_offset = -8*SCALETILE (see => "Grid" class => method draw_tile) 

        # what happens here is actually quite simple but might seem weird at first. To begin with "Pygame" has a internal clock that keeps
        # track of time in milliseconds since the game started. With that time you can set a 'time window' which will decide the time between 
        # each fram here denoted by "self.spritesheetTimeGap" , so what you want to do afterwards is calculate the time difference between 
        # the current time and the last time you "blitted" (displayed) a image to the "window" (window_ui)
        # if this difference exceeds the time gap => ] spritesheetTimeGap ; +inf [ then we are allowed to display the next frame
        current_time = pygame.time.get_ticks()
        spritesheetTimeGap = 1000
        if current_time - self.spritesheetTimer > spritesheetTimeGap:
            self.spritesheetTimer = current_time
            self.spritesheetCounter = (self.spritesheetCounter + 1) % 3
        # for more information on how i calculate offsets to blit a "Unit" or "Building" to the "window" see "Schema_Python_Game.png"
        
        if self.active and self.direction == WEST:
            window_ui.blit(self.Unitspritesheet[12 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))
       
        elif self.active and self.direction == EAST:
            window_ui.blit(self.Unitspritesheet[15 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))
       
        elif not self.active and self.direction == WEST:
            window_ui.blit(self.Unitspritesheet[18 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))

        elif not self.active and self.direction == EAST:
            window_ui.blit(self.Unitspritesheet[21 + self.spritesheetCounter],((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE))
       

        if self.health <= 9:
            window_ui.blit(
                unitDetailsSprites_Numbers.get("unitNumbers")[int(self.health) - 1],
                ((self.X - x_offset)*SCALETILE*TILESIZE + 8*SCALETILE,(self.Y - y_offset)*SCALETILE*TILESIZE + 8*SCALETILE)
            )
        
        if self.isCapturing is True and self.active is True:
            window_ui.blit(
                unitDetailsSprites_Captures[CAPTURE_AVAILABLE_ICON],
                ((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE + 8*SCALETILE)
            )
        elif self.isCapturing is True and self.active is False:
            window_ui.blit(
                unitDetailsSprites_Captures[CAPTURE_UNAVAILABLE_ICON],
                ((self.X - x_offset)*SCALETILE*TILESIZE,(self.Y - y_offset)*SCALETILE*TILESIZE + 8*SCALETILE)
            )

    def capture(self):
        self.capturedBuildingHealth -= self.health
        self.active = False

    def attack(self, defender_unit: 'Unit', tile_type):
         # base damage from the matrix 
         # see unitsBaseDamage matrix in "Configuration.py" along with the pseudo implementation
        base_damage = UNITS_BASE_DAMAGE[defender_unit.unitType][self.unitType]
        if base_damage is None:
            return 0

        base_damage /= 100
        luck = random.randint(1, 9) / 100
        hp_multiplier = self.health / 10

        # default to 0 if terrain is invalid
        tile_defense = TILE_ATTRIBUTES.get(tile_type,0)[3] / 10  
        damage_done = ((base_damage + luck) * hp_multiplier) * (1 - tile_defense)

        damage_done = damage_done*10
        defender_unit.health -= damage_done

        print(f"unit deals {damage_done} of damage\nHealth Enemy: {defender_unit.health}")


    def travel(self,x,y):
        if self.active:
            if self.X <= x:
                self.direction = EAST
            elif self.X > x:
                self.direction = WEST

            self.X = x
            self.Y = y
            # once a unit has "traveled" to it's new location we set the state of the unit to "False"
            # at the end of a player's turn all the units in this player's list are set back to the "True" state
            self.active = False

    # no implementation neccessary once Unit is popped from player's dictionary no references exists
    # and element is deleted
    def die(self):
        pass

    # for more information on Attack- and Travelzones see "Schema_Python_Game.png"
    def showTravelZone(self,x_offset,y_offset,window_ui : pygame.Surface,zoneCoord: list[tuple]):
        movementTile = pygame.Surface((TILESIZE*SCALETILE,TILESIZE*SCALETILE),pygame.SRCALPHA)
        movementTile.fill((25,25,25,125))
        for coordinate in zoneCoord:
            x = coordinate[0]
            y = coordinate[1]
            if (x_offset <= x < x_offset + WIN_X) and (y_offset <= y < y_offset + WIN_Y):
                movementTile_x = x - x_offset
                movementTile_y = y - y_offset
                window_ui.blit(movementTile,(movementTile_x*TILESIZE*SCALETILE,movementTile_y*TILESIZE*SCALETILE))

    def getTravelZone(self,map: Map):
        travelPossibilities = list()
        # movement zone range is from [- movement , movement]
        # for more details see => "Schema_Python_Game.png" 
        # I only allow the unit to travel to tiles where the tileType matches the units type
        for x in range(-self.movement,self.movement + 1):
            for y in range(-self.movement,self.movement + 1):
                if ((abs(x) + abs(y)) <= self.movement) and (0 <= self.X + x < WORLD_X) and (0 <= self.Y + y < WORLD_Y):
                    terrainType = TILE_ATTRIBUTES[map.mapTerrain[self.Y + y][self.X + x]][1]
                    if (self.type == terrainType):
                        travelPossibilities.append((self.X + x,self.Y + y))
        return travelPossibilities

    def showAttackZone(self,x_offset,y_offset,window_ui : pygame.Surface,zoneCoord: list[tuple]):
        attackTile = pygame.Surface((TILESIZE*SCALETILE,TILESIZE*SCALETILE),pygame.SRCALPHA)
        attackTile.fill((200,10,10,125))

        for coordinate in zoneCoord:
            x = coordinate[0]
            y = coordinate[1]
            if (x_offset <= x < x_offset + WIN_X) and (y_offset <= y < y_offset + WIN_Y):
                attackTile_x = x - x_offset
                attackTile_y = y - y_offset
                window_ui.blit(attackTile,(attackTile_x*TILESIZE*SCALETILE,attackTile_y*TILESIZE*SCALETILE))

    def getAttackZone(self,players):
        attackPossibilities = list()
        pssibilities = list()
        # attack zone range is from [- range , range]
        # for more details see => "Schema_Python_Game.png" 

        for ranges in [self.range]:
            for x in range(-ranges,ranges + 1):
                for y in range(-ranges,ranges + 1):
                    if ((abs(x) + abs(y)) <= ranges) and (0 <= self.X + x < WORLD_X) and (0 <= self.Y + y < WORLD_Y):
                        pssibilities.append((self.X + x,self.Y + y))

        for possibility in pssibilities.copy():
            for player in players:
                result = player.playerUnitsMap[possibility[1]][possibility[0]]
                if result is not False:
                    attackPossibilities.append(possibility)
        
        return attackPossibilities

    def showUnitsDetails(self,window_ui : pygame.Surface,time_delta: float):
        self.unitManager.draw_ui(window_ui)
        self.unitManager.update(time_delta)
   
                



        
