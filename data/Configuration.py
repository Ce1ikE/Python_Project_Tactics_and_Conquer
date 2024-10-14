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
ROAD_S    = 10
ROAD_W    = 11

# Tile Ruleset
# Dictionary of all tile types and tile edges, on the directions [North, East, South, West]
tileRuleset = {
    TILE_GRASS     : {
        "allowed_neighbors":{
            NORTH :[TILE_GRASS,TILE_COAST_S,TILE_COAST_SE,TILE_COAST_SW,TILE_FOREST,TILE_MOUNTAIN],
            SOUTH :[TILE_GRASS,TILE_COAST_N,TILE_COAST_NE,TILE_COAST_NW,TILE_FOREST,TILE_MOUNTAIN],
            WEST  :[TILE_GRASS,TILE_COAST_E,TILE_COAST_SE,TILE_COAST_NE,TILE_FOREST,TILE_MOUNTAIN],
            EAST  :[TILE_GRASS,TILE_COAST_W,TILE_COAST_SW,TILE_COAST_NW,TILE_FOREST,TILE_MOUNTAIN],
        }
    },
    TILE_WATER     : {
        "allowed_neighbors":{
            NORTH :[TILE_WATER,TILE_COAST_N,TILE_WATER_SE,TILE_WATER_SW],
            SOUTH :[TILE_WATER,TILE_COAST_S,TILE_WATER_NE,TILE_WATER_NW],
            WEST  :[TILE_WATER,TILE_COAST_W,TILE_WATER_SE,TILE_WATER_NE],
            EAST  :[TILE_WATER,TILE_COAST_E,TILE_WATER_SW,TILE_WATER_NW],
        }
    },
    TILE_FOREST    : {
        "allowed_neighbors":{
            NORTH :[TILE_GRASS,TILE_FOREST,TILE_ROAD_E],
            SOUTH :[TILE_GRASS,TILE_FOREST,TILE_ROAD_E],
            WEST  :[TILE_GRASS,TILE_FOREST,TILE_ROAD_N],
            EAST  :[TILE_GRASS,TILE_FOREST,TILE_ROAD_N],
        }
    },
    TILE_COAST_N   : {
        "allowed_neighbors":{
            NORTH :[TILE_GRASS],
            SOUTH :[TILE_WATER],
            WEST  :[TILE_COAST_NW,TILE_COAST_N,TILE_WATER_SW],
            EAST  :[TILE_COAST_NE,TILE_COAST_N,TILE_WATER_SE],
        }
    },
    TILE_COAST_E   : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_NE,TILE_COAST_E,TILE_WATER_NW],
            SOUTH :[TILE_COAST_SE,TILE_COAST_E,TILE_WATER_SW],
            WEST  :[TILE_WATER],
            EAST  :[TILE_GRASS],
        }
    },
    TILE_COAST_S   : {
        "allowed_neighbors":{
            NORTH :[TILE_WATER],
            SOUTH :[TILE_GRASS],
            WEST  :[TILE_COAST_S,TILE_COAST_SE,TILE_WATER_NW],
            EAST  :[TILE_COAST_S,TILE_COAST_SW,TILE_WATER_NE],
        }
    },
    TILE_COAST_W   : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_W,TILE_COAST_NW,TILE_WATER_NE],
            SOUTH :[TILE_COAST_W,TILE_COAST_SW,TILE_WATER_SE],
            WEST  :[TILE_GRASS],
            EAST  :[TILE_WATER],
        }
    },
    TILE_COAST_NE  : {
        "allowed_neighbors":{
            NORTH :[TILE_GRASS],
            SOUTH :[TILE_COAST_E],
            WEST  :[TILE_COAST_N],
            EAST  :[TILE_GRASS],
        }
    },
    TILE_COAST_SE  : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_E],
            SOUTH :[TILE_GRASS],
            WEST  :[TILE_COAST_S],
            EAST  :[TILE_GRASS],
        }
    },
    TILE_COAST_SW  : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_W],
            SOUTH :[TILE_GRASS],
            WEST  :[TILE_GRASS],
            EAST  :[TILE_COAST_S],
        }
    },
    TILE_COAST_NW  : {
        "allowed_neighbors":{
            NORTH :[TILE_GRASS],
            SOUTH :[TILE_GRASS],
            WEST  :[TILE_COAST_N],
            EAST  :[TILE_COAST_W],
        }
    },
    TILE_MOUNTAIN  : {
        "allowed_neighbors":{
            NORTH :[TILE_MOUNTAIN,TILE_GRASS],
            SOUTH :[TILE_MOUNTAIN,TILE_GRASS],
            WEST  :[TILE_MOUNTAIN,TILE_GRASS],
            EAST  :[TILE_MOUNTAIN,TILE_GRASS],
        }
    },
    TILE_ROAD_N    : {
        "allowed_neighbors":{
            NORTH :[TILE_ROAD_N,TILE_ROAD_NE,TILE_ROAD_NW],
            SOUTH :[TILE_ROAD_N,TILE_COAST_SE,TILE_COAST_SW],
            WEST  :[TILE_FOREST],
            EAST  :[TILE_FOREST],
        }
    },
    TILE_ROAD_E    : {
        "allowed_neighbors":{
            NORTH :[TILE_FOREST],
            SOUTH :[TILE_FOREST],
            WEST  :[TILE_ROAD_E,TILE_ROAD_SW,TILE_ROAD_NW],
            EAST  :[TILE_ROAD_E,TILE_ROAD_SE,TILE_ROAD_NE],
        }
    },
    TILE_ROAD_NE   : {
        "allowed_neighbors":{
            NORTH :[TILE_FOREST],
            SOUTH :[TILE_ROAD_N],
            WEST  :[TILE_ROAD_E],
            EAST  :[TILE_FOREST],
        }
    },
    TILE_ROAD_SE   : {
        "allowed_neighbors":{
            NORTH :[TILE_ROAD_N],
            SOUTH :[TILE_FOREST],
            WEST  :[TILE_ROAD_E],
            EAST  :[TILE_FOREST],
        }
    },
    TILE_ROAD_SW   : {
        "allowed_neighbors":{
            NORTH :[TILE_ROAD_N],
            SOUTH :[TILE_FOREST],
            WEST  :[TILE_FOREST],
            EAST  :[TILE_ROAD_E],
        }
    },
    TILE_ROAD_NW   : {
        "allowed_neighbors":{
            NORTH :[TILE_FOREST],
            SOUTH :[TILE_ROAD_N],
            WEST  :[TILE_FOREST],
            EAST  :[TILE_ROAD_E],
        }
    },
    TILE_WATER_NW  : {
        "allowed_neighbors":{
            NORTH :[TILE_WATER],
            SOUTH :[TILE_COAST_E],
            WEST  :[TILE_WATER],
            EAST  :[TILE_COAST_S],
        }
    },
    TILE_WATER_NE  : {
        "allowed_neighbors":{
            NORTH :[TILE_WATER],
            SOUTH :[TILE_COAST_W],
            WEST  :[TILE_COAST_S],
            EAST  :[TILE_WATER],
        }
    },
    TILE_WATER_SW  : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_E],
            SOUTH :[TILE_WATER],
            WEST  :[TILE_WATER],
            EAST  :[TILE_COAST_N],
        }
    },
    TILE_WATER_SE  : {
        "allowed_neighbors":{
            NORTH :[TILE_COAST_W],
            SOUTH :[TILE_WATER],
            WEST  :[TILE_COAST_N],
            EAST  :[TILE_WATER],
        }
    },
    TILE_BLANK     : {
        "allowed_neighbors":{
            NORTH :TileArray,
            SOUTH :TileArray,
            WEST  :TileArray,
            EAST  :TileArray,
        }
    },
}

# Tile Weight
# Dictionary of all tile probability
tileWeights = {
    TILE_GRASS      : 15,
    TILE_WATER      : 0,
    TILE_FOREST     : 15,
    TILE_COAST_N    : 0,
    TILE_COAST_E    : 0,
    TILE_COAST_S    : 0,
    TILE_COAST_W    : 0,
    TILE_COAST_NE   : 0,
    TILE_COAST_SE   : 0,
    TILE_COAST_SW   : 0,
    TILE_COAST_NW   : 0,
    TILE_MOUNTAIN   : 15,
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
    TILE_BLANK      : [223,81,TILESIZE,TILESIZE]
}