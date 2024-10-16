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
tileWeights = {
    TILE_GRASS      : 15,
    TILE_WATER      : 10,
    TILE_FOREST     : 15,
    TILE_COAST_N    : 3,
    TILE_COAST_E    : 3,
    TILE_COAST_S    : 3,
    TILE_COAST_W    : 3,
    TILE_COAST_NE   : 3,
    TILE_COAST_SE   : 3,
    TILE_COAST_SW   : 3,
    TILE_COAST_NW   : 3,
    TILE_MOUNTAIN   : 3,
    TILE_ROAD_N     : 1,
    TILE_ROAD_E     : 1,
    TILE_ROAD_NE    : 1,
    TILE_ROAD_SE    : 1,
    TILE_ROAD_SW    : 1,
    TILE_ROAD_NW    : 1,
    TILE_WATER_NW   : 3,
    TILE_WATER_NE   : 3,
    TILE_WATER_SW   : 3,
    TILE_WATER_SE   : 3,
    TILE_FOREST_N   : 5, 
    TILE_FOREST_S   : 5,  
    TILE_FOREST_W   : 5, 
    TILE_FOREST_E   : 5, 
    TILE_FOREST_NE  : 5, 
    TILE_FOREST_SE  : 5, 
    TILE_FOREST_NW  : 5, 
    TILE_FOREST_SW  : 5, 
    TILE_MOUTAIN_SW : 3,
    TILE_MOUTAIN_N  : 3,
    TILE_CITY       : 5,
    TILE_BLANK      : 1,
}
# Tile Spritesheet aka Tile coordinates (coord_x,coord_y,TILESIZE,TILESIZE)
# Dictionary of all tile coordinates on the SPRITESHEET_PATH
tileSprites = {
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