# Game states helps us with keeping logic in our "main" loop
PLAYING = "playing"
MENU    = "menu"
QUIT    = "quit"

# PATHS ARE DEFINED BASED ON WORKING DIRECTORY
# Path to the spritesheets we use
SPRITESHEET_PATH = "./assets/png/GBA_AW_Tiles.png"
# Path to fonts
FONT_PATH_GREYBEARD = "./assets/fonts/Greybeard.ttf"

# Spritesheet tile size (original), and upscale factor
TILESIZE  = 16
SCALETILE = 1

# World size in tiles
WORLD_X = 40*SCALETILE
WORLD_Y = 30*SCALETILE

# Window size in px
WIN_X = WORLD_X*TILESIZE - TILESIZE*5
WIN_Y = WORLD_Y*TILESIZE - TILESIZE*5

# Directions (clockwise)
NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

# Tile Types
TILE_GRASS      = 0
TILE_WATER      = 1
TILE_FOREST     = 2
TILE_COAST_N    = 3
TILE_COAST_E    = 4
TILE_COAST_S    = 5
TILE_COAST_W    = 6
TILE_COAST_NE   = 7
TILE_COAST_SE   = 8
TILE_COAST_SW   = 9
TILE_COAST_NW   = 10
TILE_MOUNTAIN   = 11
TILE_ROAD_N     = 12
TILE_ROAD_E     = 13
TILE_ROAD_NE    = 14
TILE_ROAD_SE    = 15
TILE_ROAD_SW    = 16
TILE_ROAD_NW    = 17
TILE_WATER_NW   = 18
TILE_WATER_NE   = 19
TILE_WATER_SW   = 20
TILE_WATER_SE   = 21
TILE_FOREST_N   = 22
TILE_FOREST_S   = 23 
TILE_FOREST_W   = 24
TILE_FOREST_E   = 25
TILE_FOREST_NE  = 26
TILE_FOREST_SE  = 27
TILE_FOREST_NW  = 28
TILE_FOREST_SW  = 29
TILE_MOUTAIN_SW = 30
TILE_MOUTAIN_N  = 31
TILE_CITY       = 40
TILE_BLANK      = 100

# Tile Types Array
TileArray = [
TILE_GRASS      ,
TILE_WATER      ,
TILE_FOREST     ,
TILE_COAST_N    ,
TILE_COAST_E    ,
TILE_COAST_S    ,
TILE_COAST_W    ,
TILE_COAST_NE   ,
TILE_COAST_SE   ,
TILE_COAST_SW   ,
TILE_COAST_NW   ,
TILE_MOUNTAIN   ,
TILE_ROAD_N     ,
TILE_ROAD_E     ,
TILE_ROAD_NE    ,
TILE_ROAD_SE    ,
TILE_ROAD_SW    ,
TILE_ROAD_NW    ,
TILE_WATER_NW   ,
TILE_WATER_NE   ,
TILE_WATER_SW   ,
TILE_WATER_SE   ,
TILE_FOREST_N   , 
TILE_FOREST_S   ,  
TILE_FOREST_W   , 
TILE_FOREST_E   , 
TILE_FOREST_NE  , 
TILE_FOREST_SE  , 
TILE_FOREST_NW  , 
TILE_FOREST_SW  ,
TILE_MOUTAIN_SW ,
TILE_MOUTAIN_N  ,
TILE_CITY       ,
TILE_BLANK 
]
 
# Tile Edges
GRASS     = 0
WATER     = 1
FOREST    = 2
MOUNTAIN  = 3
COAST_N   = 4
COAST_E   = 5
COAST_S   = 6
COAST_W   = 7
FOREST_N  = 8
FOREST_E  = 9
FOREST_S  = 10
FOREST_W  = 11
ROAD_N    = 12
ROAD_E    = 13

# Tile Ruleset
# Dictionary of all tile types and tile edges, on the directions [North, East, South, West]
tileRuleset = {
    TILE_GRASS     : [GRASS, GRASS, GRASS, GRASS],
    TILE_WATER     : [WATER, WATER, WATER, WATER],
    TILE_FOREST    : [FOREST, FOREST, FOREST, FOREST],
    TILE_MOUNTAIN  : [MOUNTAIN, MOUNTAIN, MOUNTAIN, MOUNTAIN],
    
    TILE_COAST_N   : [GRASS, COAST_N, WATER, COAST_N],
    TILE_COAST_E   : [COAST_E, GRASS, COAST_E, WATER],
    TILE_COAST_S   : [WATER, COAST_S, GRASS, COAST_S],
    TILE_COAST_W   : [COAST_W, WATER, COAST_W, GRASS],
    
    TILE_COAST_NE  : [GRASS, GRASS, COAST_E, COAST_N],
    TILE_COAST_SE  : [COAST_E, GRASS, GRASS, COAST_S],
    TILE_COAST_SW  : [COAST_W, COAST_S, GRASS, GRASS],
    TILE_COAST_NW  : [GRASS, COAST_N, COAST_W, GRASS],
    
    TILE_MOUTAIN_SW : [GRASS, GRASS, MOUNTAIN, MOUNTAIN],
    TILE_MOUTAIN_N  : [MOUNTAIN, GRASS, GRASS, GRASS],
    
    TILE_ROAD_N    : [ROAD_N, FOREST, ROAD_N, FOREST],
    TILE_ROAD_E    : [FOREST, ROAD_E, FOREST, ROAD_E],
    TILE_ROAD_NE   : [ROAD_N, ROAD_E, GRASS, GRASS],
    TILE_ROAD_SE   : [GRASS, ROAD_E, ROAD_N, GRASS],
    TILE_ROAD_SW   : [GRASS, GRASS, ROAD_N, ROAD_E],
    TILE_ROAD_NW   : [ROAD_N, GRASS, GRASS, ROAD_E],
    
    TILE_WATER_NW  : [WATER, COAST_S, COAST_E, WATER],
    TILE_WATER_NE  : [WATER, WATER, COAST_W, COAST_S],
    TILE_WATER_SW  : [COAST_E, COAST_N, WATER, WATER],
    TILE_WATER_SE  : [COAST_W, WATER, WATER, COAST_N],
    
    TILE_FOREST_N  : [FOREST, FOREST_N, GRASS, FOREST_N],
    TILE_FOREST_S  : [GRASS, FOREST_S, FOREST, FOREST_S],
    TILE_FOREST_W  : [FOREST_W, GRASS, FOREST_W, FOREST],
    TILE_FOREST_E  : [FOREST_E, FOREST, FOREST_E, GRASS],
    
    TILE_FOREST_NE : [FOREST_E, FOREST_N, GRASS, GRASS],
    TILE_FOREST_SE : [GRASS, FOREST_S, FOREST_E, GRASS],
    TILE_FOREST_NW : [FOREST_W, GRASS, GRASS, FOREST_N],
    TILE_FOREST_SW : [GRASS, GRASS, FOREST_E, FOREST_S],
    
    TILE_CITY      : [TILE_ROAD_E, TILE_ROAD_N, TILE_ROAD_E, TILE_ROAD_N],
    TILE_BLANK     : [TILE_BLANK, TILE_BLANK, TILE_BLANK, TILE_BLANK],
}




# Tile Weight
# Dictionary of all tile probability
# tileWeights = {
#     TILE_GRASS      : 20,
#     TILE_WATER      : 10,
#     TILE_FOREST     : 15,
#     TILE_COAST_N    : 3,
#     TILE_COAST_E    : 3,
#     TILE_COAST_S    : 3,
#     TILE_COAST_W    : 3,
#     TILE_COAST_NE   : 3,
#     TILE_COAST_SE   : 3,
#     TILE_COAST_SW   : 3,
#     TILE_COAST_NW   : 3,
#     TILE_MOUNTAIN   : 3,
#     TILE_ROAD_N     : 1,
#     TILE_ROAD_E     : 1,
#     TILE_ROAD_NE    : 1,
#     TILE_ROAD_SE    : 1,
#     TILE_ROAD_SW    : 1,
#     TILE_ROAD_NW    : 1,
#     TILE_WATER_NW   : 3,
#     TILE_WATER_NE   : 3,
#     TILE_WATER_SW   : 3,
#     TILE_WATER_SE   : 3,
#     TILE_FOREST_N   : 5, 
#     TILE_FOREST_S   : 5,  
#     TILE_FOREST_W   : 5, 
#     TILE_FOREST_E   : 5, 
#     TILE_FOREST_NE  : 5, 
#     TILE_FOREST_SE  : 5, 
#     TILE_FOREST_NW  : 5, 
#     TILE_FOREST_SW  : 5, 
#     TILE_MOUTAIN_SW : 3,
#     TILE_MOUTAIN_N  : 3,
#     TILE_CITY       : 5,
#     TILE_BLANK      : 1,
# }

tileWeights = {
    TILE_GRASS      : 60,
    TILE_WATER      : 5,
    TILE_FOREST     : 3,
    TILE_COAST_N    : 3,
    TILE_COAST_E    : 3,
    TILE_COAST_S    : 3,
    TILE_COAST_W    : 3,
    TILE_COAST_NE   : 3,
    TILE_COAST_SE   : 3,
    TILE_COAST_SW   : 3,
    TILE_COAST_NW   : 3,
    TILE_MOUNTAIN   : 3,
    TILE_ROAD_N     : 0,
    TILE_ROAD_E     : 0,
    TILE_ROAD_NE    : 0,
    TILE_ROAD_SE    : 0,
    TILE_ROAD_SW    : 0,
    TILE_ROAD_NW    : 0,
    TILE_WATER_NW   : 3,
    TILE_WATER_NE   : 3,
    TILE_WATER_SW   : 3,
    TILE_WATER_SE   : 3,
    TILE_FOREST_N   : 4, 
    TILE_FOREST_S   : 4,  
    TILE_FOREST_W   : 4, 
    TILE_FOREST_E   : 4, 
    TILE_FOREST_NE  : 4, 
    TILE_FOREST_SE  : 4, 
    TILE_FOREST_NW  : 4, 
    TILE_FOREST_SW  : 4, 
    TILE_MOUTAIN_SW : 0,
    TILE_MOUTAIN_N  : 0,
    TILE_CITY       : 10,
    TILE_BLANK      : 1,
}


# Tile Spritesheet aka Tile coordinates (coord_x,coord_y,TILESIZE,TILESIZE)
# Dictionary of all tile coordinates on the SPRITESHEET_PATH
tileSprites = {
    TILE_GRASS      : [2,13,TILESIZE,TILESIZE],
    TILE_WATER      : [19,128,TILESIZE,TILESIZE],
    TILE_FOREST     : [19,13,TILESIZE,TILESIZE],
    TILE_COAST_N    : [223,128,TILESIZE,TILESIZE],
    TILE_COAST_E    : [240,145,TILESIZE,TILESIZE],
    TILE_COAST_S    : [223,162,TILESIZE,TILESIZE],
    TILE_COAST_W    : [206,145,TILESIZE,TILESIZE],
    TILE_COAST_NE   : [240,128,TILESIZE,TILESIZE],
    TILE_COAST_SE   : [240,162,TILESIZE,TILESIZE],
    TILE_COAST_SW   : [206,162,TILESIZE,TILESIZE],
    TILE_COAST_NW   : [206,128,TILESIZE,TILESIZE],
    TILE_MOUNTAIN   : [70,13,TILESIZE,TILESIZE],
    TILE_ROAD_N     : [172,64,TILESIZE,TILESIZE],
    TILE_ROAD_E     : [155,64,TILESIZE,TILESIZE],
    TILE_ROAD_NE    : [155,47,TILESIZE,TILESIZE],
    TILE_ROAD_SE    : [155,13,TILESIZE,TILESIZE],
    TILE_ROAD_SW    : [189,13,TILESIZE,TILESIZE],
    TILE_ROAD_NW    : [189,47,TILESIZE,TILESIZE],
    TILE_WATER_NW   : [155,81,TILESIZE,TILESIZE],
    TILE_WATER_NE   : [189,81,TILESIZE,TILESIZE],
    TILE_WATER_SW   : [172,81,TILESIZE,TILESIZE],
    TILE_WATER_SE   : [206,81,TILESIZE,TILESIZE],
    TILE_BLANK      : [223,81,TILESIZE,TILESIZE]
}
# Units stats and data in dictionaries
LOW_ARMOR = 1
MEDIUM_ARMOR = 3
HIGH_ARMOR = 5
LAND_TYPE = "land"
WATER_TYPE = "water"
AIR_TYPE = "air"


INFANTRY = {
    "Name": "infantry",
    "movement": 3,
    "range": 1,
    "defense": LOW_ARMOR,
    "type": LAND_TYPE
}
HEAVY_INFANTRY = {
    "Name": "heavy infantry",
    "movement": 2,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE
}
TANK = {
    "Name": "tank",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE
}
MEDIUM_TANK = {
    "Name": "medium tank",
    "movement": 5,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": LAND_TYPE
}
HEAVY_TANK = {
    "Name": "heavy tank",
    "movement": 6,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": LAND_TYPE
}
ARTILLERY = {
    "Name": "artillery",
    "movement": 5,
    "range": [2,3],
    "defense": LOW_ARMOR,
    "type": LAND_TYPE
}
HEAVY_ARTILLERY = {
    "Name": "heavy artillery",
    "movement": 5,
    "range": [3,4,5],
    "defense": LOW_ARMOR,
    "type": LAND_TYPE
}
AA_TANK = {
    "Name": "AA tank",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE
}
APC = {
    "Name": "APC",
    "movement": 6,
    "range": 0,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE
}
SUBMARINE = {
    "Name": "submarine",
    "movement": 5,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": WATER_TYPE
}
DESTROYER = {
    "Name": "destroyer",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": WATER_TYPE
}
LANDER = {
    "Name": "lander",
    "movement": 6,
    "range": 0,
    "defense": LOW_ARMOR,
    "type": WATER_TYPE
}
CARRIER = {
    "Name": "carrier",
    "movement": 5,
    "range": [3,4,5,6],
    "defense": HIGH_ARMOR,
    "type": WATER_TYPE
}
TRANSPORT_HELICOPTER = {
    "Name": "transport helicopter",
    "movement": 6,
    "range": 0,
    "defense": LOW_ARMOR,
    "type": AIR_TYPE
}
COMBAT_HELICOPTER = {
    "Name": "combat helicopter",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": AIR_TYPE
}
FIGHTER_JET = {
    "Name": "fighter jet",
    "movement": 9,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": AIR_TYPE
}
BOMBER = {
    "Name": "bomber",
    "movement": 7,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": AIR_TYPE
}

    TILE_GRASS      : [3,14,TILESIZE,TILESIZE],
    TILE_WATER      : [20,129,TILESIZE,TILESIZE],
    TILE_FOREST     : [20,48,TILESIZE,TILESIZE],
    TILE_COAST_N    : [224,129,TILESIZE,TILESIZE],
    TILE_COAST_E    : [241,146,TILESIZE,TILESIZE],
    TILE_COAST_S    : [224,163,TILESIZE,TILESIZE],
    TILE_COAST_W    : [207,146,TILESIZE,TILESIZE],
    TILE_COAST_NE   : [241,129,TILESIZE,TILESIZE],
    TILE_COAST_SE   : [241,163,TILESIZE,TILESIZE],
    TILE_COAST_SW   : [207,163,TILESIZE,TILESIZE],
    TILE_COAST_NW   : [207,129,TILESIZE,TILESIZE],
    TILE_MOUNTAIN   : [105,31,TILESIZE,TILESIZE],
    TILE_ROAD_N     : [173,65,TILESIZE,TILESIZE],
    TILE_ROAD_E     : [156,65,TILESIZE,TILESIZE],
    TILE_ROAD_NE    : [156,48,TILESIZE,TILESIZE],
    TILE_ROAD_SE    : [156,14,TILESIZE,TILESIZE],
    TILE_ROAD_SW    : [190,14,TILESIZE,TILESIZE],
    TILE_ROAD_NW    : [190,48,TILESIZE,TILESIZE],
    TILE_WATER_NW   : [156,82,TILESIZE,TILESIZE],
    TILE_WATER_NE   : [190,82,TILESIZE,TILESIZE],
    TILE_WATER_SW   : [173,82,TILESIZE,TILESIZE],
    TILE_WATER_SE   : [207,82,TILESIZE,TILESIZE],
    TILE_FOREST_N   : [20,65,TILESIZE,TILESIZE], 
    TILE_FOREST_S   : [20,31,TILESIZE,TILESIZE],  
    TILE_FOREST_W   : [37,48,TILESIZE,TILESIZE], 
    TILE_FOREST_E   : [3,48,TILESIZE,TILESIZE], 
    TILE_FOREST_NE  : [3,65,TILESIZE,TILESIZE], 
    TILE_FOREST_SE  : [3,31,TILESIZE,TILESIZE], 
    TILE_FOREST_NW  : [37,65,TILESIZE,TILESIZE], 
    TILE_FOREST_SW  : [37,31,TILESIZE,TILESIZE],
    TILE_MOUTAIN_SW : [88,14,TILESIZE,TILESIZE],
    TILE_MOUTAIN_N  : [88,31,TILESIZE,TILESIZE],
    TILE_CITY       : [88,1245,TILESIZE,TILESIZE*2],
    TILE_BLANK      : [224,82,TILESIZE,TILESIZE]
}
