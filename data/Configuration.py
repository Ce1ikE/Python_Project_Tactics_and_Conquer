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
SCALETILE = 2

# World size in tiles
WORLD_X = 40
WORLD_Y = 30

# Window size in px
WIN_X = WORLD_X*TILESIZE
WIN_Y = WORLD_Y*TILESIZE

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
TILE_CITY       = 22
TILE_BLANK      = 100

# Tile Types Array
TileArray = [
TILE_GRASS   ,
TILE_WATER   ,
TILE_FOREST  ,
TILE_COAST_N ,
TILE_COAST_E ,
TILE_COAST_S ,
TILE_COAST_W ,
TILE_COAST_NE,
TILE_COAST_SE,
TILE_COAST_SW,
TILE_COAST_NW,
TILE_MOUNTAIN,
TILE_ROAD_N  ,
TILE_ROAD_E  ,
TILE_ROAD_NE ,
TILE_ROAD_SE ,
TILE_ROAD_SW ,
TILE_ROAD_NW ,
TILE_WATER_NW,
TILE_WATER_NE,
TILE_WATER_SW,
TILE_WATER_SE,
TILE_CITY    ,
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
ROAD_N    = 8
ROAD_E    = 9

# Tile Ruleset
# Dictionary of all tile types and tile edges, on the directions [North, East, South, West]
# tileRuleset = {
#     TILE_GRASS     : {
#         "allowed_neighbors":{
#             NORTH :[TILE_GRASS,TILE_COAST_S,TILE_COAST_SE,TILE_COAST_SW,TILE_FOREST,TILE_MOUNTAIN,TILE_CITY],
#             SOUTH :[TILE_GRASS,TILE_COAST_N,TILE_COAST_NE,TILE_COAST_NW,TILE_FOREST,TILE_MOUNTAIN,TILE_CITY],
#             WEST  :[TILE_GRASS,TILE_COAST_E,TILE_COAST_SE,TILE_COAST_NE,TILE_FOREST,TILE_MOUNTAIN,TILE_CITY],
#             EAST  :[TILE_GRASS,TILE_COAST_W,TILE_COAST_SW,TILE_COAST_NW,TILE_FOREST,TILE_MOUNTAIN,TILE_CITY],
#         }
#     },
#     TILE_WATER     : {
#         "allowed_neighbors":{
#             NORTH :[TILE_WATER,TILE_COAST_N,TILE_WATER_SE,TILE_WATER_SW],
#             SOUTH :[TILE_WATER,TILE_COAST_S,TILE_WATER_NE,TILE_WATER_NW],
#             WEST  :[TILE_WATER,TILE_COAST_W,TILE_WATER_SE,TILE_WATER_NE],
#             EAST  :[TILE_WATER,TILE_COAST_E,TILE_WATER_SW,TILE_WATER_NW],
#         }
#     },
#     TILE_FOREST    : {
#         "allowed_neighbors":{
#             NORTH :[TILE_GRASS,TILE_FOREST,TILE_ROAD_E,TILE_MOUNTAIN],
#             SOUTH :[TILE_GRASS,TILE_FOREST,TILE_ROAD_E,TILE_MOUNTAIN],
#             WEST  :[TILE_GRASS,TILE_FOREST,TILE_ROAD_N,TILE_MOUNTAIN],
#             EAST  :[TILE_GRASS,TILE_FOREST,TILE_ROAD_N,TILE_MOUNTAIN],
#         }
#     },
#     TILE_COAST_N   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_GRASS],
#             SOUTH :[TILE_WATER],
#             WEST  :[TILE_COAST_NW,TILE_COAST_N,TILE_WATER_SW],
#             EAST  :[TILE_COAST_NE,TILE_COAST_N,TILE_WATER_SE],
#         }
#     },
#     TILE_COAST_E   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_NE,TILE_COAST_E,TILE_WATER_NW],
#             SOUTH :[TILE_COAST_SE,TILE_COAST_E,TILE_WATER_SW],
#             WEST  :[TILE_WATER],
#             EAST  :[TILE_GRASS],
#         }
#     },
#     TILE_COAST_S   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_WATER],
#             SOUTH :[TILE_GRASS],
#             WEST  :[TILE_COAST_S,TILE_COAST_SW,TILE_WATER_NW],
#             EAST  :[TILE_COAST_S,TILE_COAST_SE,TILE_WATER_NE],
#         }
#     },
#     TILE_COAST_W   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_W,TILE_COAST_NW,TILE_WATER_NE],
#             SOUTH :[TILE_COAST_W,TILE_COAST_SW,TILE_WATER_SE],
#             WEST  :[TILE_GRASS],
#             EAST  :[TILE_WATER],
#         }
#     },
#     TILE_COAST_NE  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_GRASS],
#             SOUTH :[TILE_COAST_E,TILE_WATER_SW],
#             WEST  :[TILE_COAST_N,TILE_WATER_SW],
#             EAST  :[TILE_GRASS],
#         }
#     },
#     TILE_COAST_SE  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_E,TILE_WATER_NW],
#             SOUTH :[TILE_GRASS],
#             WEST  :[TILE_COAST_S,TILE_WATER_NW],
#             EAST  :[TILE_GRASS],
#         }
#     },
#     TILE_COAST_SW  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_W,TILE_WATER_NE],
#             SOUTH :[TILE_GRASS],
#             WEST  :[TILE_GRASS],
#             EAST  :[TILE_COAST_S,TILE_WATER_NE],
#         }
#     },
#     TILE_COAST_NW  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_GRASS],
#             SOUTH :[TILE_COAST_W,TILE_WATER_SE],
#             WEST  :[TILE_GRASS],
#             EAST  :[TILE_COAST_N,TILE_WATER_SE],
#         }
#     },
#     TILE_MOUNTAIN  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_MOUNTAIN,TILE_GRASS,TILE_FOREST],
#             SOUTH :[TILE_MOUNTAIN,TILE_GRASS,TILE_FOREST],
#             WEST  :[TILE_MOUNTAIN,TILE_GRASS,TILE_FOREST],
#             EAST  :[TILE_MOUNTAIN,TILE_GRASS,TILE_FOREST],
#         }
#     },
#     TILE_ROAD_N    : {
#         "allowed_neighbors":{
#             NORTH :[TILE_ROAD_N,TILE_ROAD_NE,TILE_ROAD_NW,TILE_CITY],
#             SOUTH :[TILE_ROAD_N,TILE_COAST_SE,TILE_COAST_SW,TILE_CITY],
#             WEST  :[TILE_FOREST,TILE_GRASS],
#             EAST  :[TILE_FOREST,TILE_GRASS],
#         }
#     },
#     TILE_ROAD_E    : {
#         "allowed_neighbors":{
#             NORTH :[TILE_FOREST,TILE_GRASS],
#             SOUTH :[TILE_FOREST,TILE_GRASS],
#             WEST  :[TILE_ROAD_E,TILE_ROAD_SW,TILE_ROAD_NW,TILE_CITY],
#             EAST  :[TILE_ROAD_E,TILE_ROAD_SE,TILE_ROAD_NE,TILE_CITY],
#         }
#     },
#     TILE_ROAD_NE   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_FOREST],
#             SOUTH :[TILE_ROAD_N],
#             WEST  :[TILE_ROAD_E],
#             EAST  :[TILE_FOREST],
#         }
#     },
#     TILE_ROAD_SE   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_ROAD_N],
#             SOUTH :[TILE_FOREST],
#             WEST  :[TILE_ROAD_E],
#             EAST  :[TILE_FOREST],
#         }
#     },
#     TILE_ROAD_SW   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_ROAD_N],
#             SOUTH :[TILE_FOREST],
#             WEST  :[TILE_FOREST],
#             EAST  :[TILE_ROAD_E],
#         }
#     },
#     TILE_ROAD_NW   : {
#         "allowed_neighbors":{
#             NORTH :[TILE_FOREST],
#             SOUTH :[TILE_ROAD_N],
#             WEST  :[TILE_FOREST],
#             EAST  :[TILE_ROAD_E],
#         }
#     },
#     TILE_WATER_NW  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_WATER],
#             SOUTH :[TILE_COAST_E,TILE_COAST_SE],
#             WEST  :[TILE_WATER],
#             EAST  :[TILE_COAST_S,TILE_COAST_SE],
#         }
#     },
#     TILE_WATER_NE  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_WATER],
#             SOUTH :[TILE_COAST_W,TILE_COAST_SW],
#             WEST  :[TILE_COAST_S,TILE_COAST_SW],
#             EAST  :[TILE_WATER],
#         }
#     },
#     TILE_WATER_SW  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_E,TILE_COAST_NE],
#             SOUTH :[TILE_WATER],
#             WEST  :[TILE_WATER],
#             EAST  :[TILE_COAST_N,TILE_COAST_NE],
#         }
#     },
#     TILE_WATER_SE  : {
#         "allowed_neighbors":{
#             NORTH :[TILE_COAST_W,TILE_COAST_NW],
#             SOUTH :[TILE_WATER],
#             WEST  :[TILE_COAST_N,TILE_COAST_NW],
#             EAST  :[TILE_WATER],
#         }
#     },
#     TILE_CITY      : {
#         "allowed_neighbors":{
#             NORTH :[TILE_ROAD_E,TILE_GRASS],
#             SOUTH :[TILE_ROAD_E,TILE_GRASS],
#             WEST  :[TILE_ROAD_N,TILE_GRASS],
#             EAST  :[TILE_ROAD_N,TILE_GRASS],
#         }
#     },
#     TILE_BLANK     : {
#         "allowed_neighbors":{
#             NORTH :TileArray,
#             SOUTH :TileArray,
#             WEST  :TileArray,
#             EAST  :TileArray,
#         }
#     },
# }

tileRuleset = {
    TILE_GRASS     : {
            NORTH :[GRASS],
            SOUTH :[GRASS],
            WEST  :[GRASS],
            EAST  :[GRASS],
    },
    TILE_WATER     : {
            NORTH :[TILE_WATER],
            SOUTH :[TILE_WATER],
            WEST  :[TILE_WATER],
            EAST  :[TILE_WATER],
    },
    TILE_FOREST    : {
            NORTH :[GRASS,FOREST],
            SOUTH :[GRASS,FOREST],
            WEST  :[GRASS,FOREST],
            EAST  :[GRASS,FOREST],
    },
    TILE_COAST_N   : {
            NORTH :[GRASS],
            SOUTH :[WATER],
            WEST  :[COAST_N],
            EAST  :[COAST_N],
    },
    TILE_COAST_E   : {
            NORTH :[COAST_E],
            SOUTH :[COAST_E],
            WEST  :[WATER],
            EAST  :[GRASS],
    },
    TILE_COAST_S   : {
            NORTH :[WATER],
            SOUTH :[GRASS],
            WEST  :[COAST_S],
            EAST  :[COAST_S],
    },
    TILE_COAST_W   : {
            NORTH :[COAST_W],
            SOUTH :[COAST_W],
            WEST  :[GRASS],
            EAST  :[WATER],
    },
    TILE_COAST_NE  : {
            NORTH :[GRASS],
            SOUTH :[COAST_E],
            WEST  :[COAST_N],
            EAST  :[GRASS],
    },
    TILE_COAST_SE  : {
            NORTH :[COAST_E],
            SOUTH :[GRASS],
            WEST  :[COAST_S],
            EAST  :[GRASS],
    },
    TILE_COAST_SW  : {
            NORTH :[COAST_W],
            SOUTH :[GRASS],
            WEST  :[GRASS],
            EAST  :[COAST_S],
    },
    TILE_COAST_NW  : {
            NORTH :[GRASS],
            SOUTH :[COAST_W],
            WEST  :[GRASS],
            EAST  :[COAST_N],
    },
    TILE_MOUNTAIN  : {
            NORTH :[MOUNTAIN,FOREST,GRASS],
            SOUTH :[MOUNTAIN,FOREST,GRASS],
            WEST  :[MOUNTAIN,FOREST,GRASS],
            EAST  :[MOUNTAIN,FOREST,GRASS],
    },
    TILE_ROAD_N    : {
            NORTH :[ROAD_N],
            SOUTH :[ROAD_N],
            WEST  :[FOREST,GRASS,MOUNTAIN],
            EAST  :[FOREST,GRASS,MOUNTAIN],
    },
    TILE_ROAD_E    : {
            NORTH :[FOREST,GRASS,MOUNTAIN],
            SOUTH :[FOREST,GRASS,MOUNTAIN],
            WEST  :[ROAD_E],
            EAST  :[ROAD_E],
    },
    TILE_ROAD_NE   : {
            NORTH :[GRASS,FOREST,MOUNTAIN],
            SOUTH :[ROAD_N],
            WEST  :[ROAD_E],
            EAST  :[GRASS,FOREST,MOUNTAIN],
    },
    TILE_ROAD_SE   : {
            NORTH :[ROAD_N],
            SOUTH :[GRASS,FOREST,MOUNTAIN],
            WEST  :[ROAD_E],
            EAST  :[GRASS,FOREST,MOUNTAIN],
    },
    TILE_ROAD_SW   : {
            NORTH :[ROAD_N],
            SOUTH :[GRASS,FOREST,MOUNTAIN],
            WEST  :[GRASS,FOREST,MOUNTAIN],
            EAST  :[ROAD_E],
    },
    TILE_ROAD_NW   : {
            NORTH :[GRASS,FOREST,MOUNTAIN],
            SOUTH :[ROAD_N],
            WEST  :[GRASS,FOREST,MOUNTAIN],
            EAST  :[ROAD_E],
    },
    TILE_WATER_NW  : {
            NORTH :[WATER],
            SOUTH :[COAST_S],
            WEST  :[WATER],
            EAST  :[COAST_E],
    },
    TILE_WATER_NE  : {
            NORTH :[WATER],
            SOUTH :[COAST_W],
            WEST  :[COAST_S],
            EAST  :[WATER],
    },
    TILE_WATER_SW  : {
            NORTH :[COAST_E],
            SOUTH :[WATER],
            WEST  :[WATER],
            EAST  :[COAST_N],
    },
    TILE_WATER_SE  : {
            NORTH :[COAST_W],
            SOUTH :[WATER],
            WEST  :[COAST_N],
            EAST  :[WATER],
    },
    TILE_CITY      : {
            NORTH :[TILE_ROAD_E,TILE_GRASS],
            SOUTH :[TILE_ROAD_E,TILE_GRASS],
            WEST  :[TILE_ROAD_N,TILE_GRASS],
            EAST  :[TILE_ROAD_N,TILE_GRASS],
    },
    TILE_BLANK     : {
            NORTH :[100],
            SOUTH :[100],
            WEST  :[100],
            EAST  :[100],
    },
}


# Tile Weight
# Dictionary of all tile probability
tileWeights = {
    TILE_GRASS      : 15,
    TILE_WATER      : 10,
    TILE_FOREST     : 10,
    TILE_COAST_N    : 5,
    TILE_COAST_E    : 5,
    TILE_COAST_S    : 5,
    TILE_COAST_W    : 5,
    TILE_COAST_NE   : 5,
    TILE_COAST_SE   : 5,
    TILE_COAST_SW   : 5,
    TILE_COAST_NW   : 5,
    TILE_MOUNTAIN   : 10,
    TILE_ROAD_N     : 0,
    TILE_ROAD_E     : 0,
    TILE_ROAD_NE    : 0,
    TILE_ROAD_SE    : 0,
    TILE_ROAD_SW    : 0,
    TILE_ROAD_NW    : 0,
    TILE_WATER_NW   : 5,
    TILE_WATER_NE   : 5,
    TILE_WATER_SW   : 5,
    TILE_WATER_SE   : 5,
    TILE_CITY       : 0,
    TILE_BLANK      : 0,
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
    TILE_CITY       : [87,1244,TILESIZE,TILESIZE*2],
    TILE_BLANK      : [223,81,TILESIZE,TILESIZE]
}