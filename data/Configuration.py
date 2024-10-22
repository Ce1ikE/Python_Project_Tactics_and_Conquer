# Game states helps us with keeping logic in our "main" loop
PLAYING = "playing"
MENU    = "menu"
QUIT    = "quit"

# PATHS ARE DEFINED BASED ON WORKING DIRECTORY
# Path to the spritesheets we use
SPRITESHEET_PATH_TILES = "./assets/png/GBA_AW_Tiles.png"
SPRITESHEET_PATH_CURSOR_1 = "./assets/png/cursor+attack.png"
SPRITESHEET_PATH_CURSOR_2 = "./assets/png/cursor+default.png"
SPRITESHEET_PATH_UNITS = "./assets/png/GBA_AW_Units.png"
SPRITESHEET_PATH_HUD_NEXT_PLAYER = "./assets/png/next_player.png"
SPRITESHEET_PATH_HUD_PAUSE = "./assets/png/pause.png"
SPRITESHEET_PATH_HUD_PLAY = "./assets/png/play.png"
# Path to fonts
FONT_PATH_GREYBEARD = "./assets/fonts/Greybeard.ttf"

# Spritesheet tile size (original), and upscale factor
SCALETILE = 4
TILESIZE  = 16

# World size in tiles
WORLD_X = 10
WORLD_Y = 10

# World size in px
WORLD_X_PX = WORLD_X*TILESIZE*SCALETILE
WORLD_Y_PX = WORLD_Y*TILESIZE*SCALETILE

# Window size in px
WIN_X_PX = 640
WIN_Y_PX = 480

# Window size in tiles     !! Window_size < World_size
WIN_X = int(WIN_X_PX/(TILESIZE*SCALETILE))
WIN_Y = int(WIN_Y_PX/(TILESIZE*SCALETILE))

# Camera position in tiles
CAMERA_X = WORLD_X - WIN_X
CAMERA_Y = WORLD_Y - WIN_Y


# Calculations :
# tilesize              = 16
# win_x_px,win_y_px     = 640 , 320
# scaletile             = s
# world_x,world_y       = w_x , w_y
# win_x,win_y           = w_x - c_x , w_x - c_y
# camera_x,camera_y     = c_x , c_y
# world_x_px,world_y_px = 16*w_x*s , 16*w_y*s  

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
tileWeights = {
    TILE_GRASS      : 150,
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

tileDefense = {
    TILE_GRASS      : 1,
    TILE_WATER      : 2,
    TILE_FOREST     : 4,
    TILE_COAST_N    : 1,
    TILE_COAST_E    : 1,
    TILE_COAST_S    : 1,
    TILE_COAST_W    : 1,
    TILE_COAST_NE   : 1,
    TILE_COAST_SE   : 1,
    TILE_COAST_SW   : 1,
    TILE_COAST_NW   : 1,
    TILE_MOUNTAIN   : 1,
    TILE_ROAD_N     : 1,
    TILE_ROAD_E     : 1,
    TILE_ROAD_NE    : 1,
    TILE_ROAD_SE    : 1,
    TILE_ROAD_SW    : 1,
    TILE_ROAD_NW    : 1,
    TILE_WATER_NW   : 1,
    TILE_WATER_NE   : 1,
    TILE_WATER_SW   : 1,
    TILE_WATER_SE   : 1,
    TILE_FOREST_S   : 3,  
    TILE_FOREST_W   : 3, 
    TILE_FOREST_E   : 3, 
    TILE_FOREST_N   : 3, 
    TILE_FOREST_NE  : 3, 
    TILE_FOREST_SE  : 3, 
    TILE_FOREST_NW  : 3, 
    TILE_FOREST_SW  : 3, 
    TILE_MOUTAIN_SW : 5,
    TILE_MOUTAIN_N  : 5,
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

# All cursor sprites
CursorSprites = [
    [    
    [0,0,37,41],
    [38,0,38,41],
    [76,0,38,41],
    [114,0,38,41]
    ],
    [    
    [0,0,32,32],
    [33,0,32,32],
    [65,0,32,32],
    [97,0,32,32]
    ],
]


# All units types
INFANTRY                = 0
HEAVY_INFANTRY          = 1
TANK                    = 2
MEDIUM_TANK             = 3
HEAVY_TANK              = 4
ARTILLERY               = 5
HEAVY_ARTILLERY         = 6
AA_TANK                 = 7
APC                     = 8
SUBMARINE               = 9 
DESTROYER               = 10    
LANDER                  = 11
CARRIER                 = 12
TRANSPORT_HELICOPTER    = 13 
COMBAT_HELICOPTER       = 14
FIGHTER_JET             = 15
BOMBER                  = 16

# [
# [Left_1]  ,[Left_2]   ,[Left_3],
# [DOWN_1]  ,[DOWN_2]   ,[DOWN_3],
# [UP_1]    ,[UP_2]     ,[UP_3],
# [RIGHT_1] ,[RIGHT_2]  ,[RIGHT_3],
# [IDLE_1]  ,[IDLE_2]   ,[IDLE_3],
# [UNA_1]   ,[UNA_2]    ,[UNA_3]
# ]
unitSprites = {
    INFANTRY                : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]
    ], 
    HEAVY_INFANTRY          : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]    
    ], 
    TANK                    : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[] 
    ], 
    MEDIUM_TANK             : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    HEAVY_TANK              : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    ARTILLERY               : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    HEAVY_ARTILLERY         : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    AA_TANK                 : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    APC                     : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    SUBMARINE               : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],  
    DESTROYER               : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],    
    LANDER                  : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],
    CARRIER                 : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],
    TRANSPORT_HELICOPTER    : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ], 
    COMBAT_HELICOPTER       : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],
    FIGHTER_JET             : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],
    BOMBER                  : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[]         
    ],
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
    "type": LAND_TYPE,
    "spritesheet":unitSprites[INFANTRY]
}
HEAVY_INFANTRY = {
    "Name": "heavy infantry",
    "movement": 2,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[HEAVY_INFANTRY]
}
TANK = {
    "Name": "tank",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[TANK]
}
MEDIUM_TANK = {
    "Name": "medium tank",
    "movement": 5,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[MEDIUM_TANK]
}
HEAVY_TANK = {
    "Name": "heavy tank",
    "movement": 6,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[HEAVY_TANK]
}
ARTILLERY = {
    "Name": "artillery",
    "movement": 5,
    "range": [2,3],
    "defense": LOW_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[ARTILLERY]
}
HEAVY_ARTILLERY = {
    "Name": "heavy artillery",
    "movement": 5,
    "range": [3,4,5],
    "defense": LOW_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[HEAVY_ARTILLERY]
}
AA_TANK = {
    "Name": "AA tank",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[AA_TANK]
}
APC = {
    "Name": "APC",
    "movement": 6,
    "range": 0,
    "defense": MEDIUM_ARMOR,
    "type": LAND_TYPE,
    "spritesheet":unitSprites[APC]
}
SUBMARINE = {
    "Name": "submarine",
    "movement": 5,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": WATER_TYPE,
    "spritesheet":unitSprites[SUBMARINE]
}
DESTROYER = {
    "Name": "destroyer",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": WATER_TYPE,
    "spritesheet":unitSprites[DESTROYER]
}
LANDER = {
    "Name": "lander",
    "movement": 6,
    "range": 0,
    "defense": LOW_ARMOR,
    "type": WATER_TYPE,
    "spritesheet":unitSprites[LANDER]
}
CARRIER = {
    "Name": "carrier",
    "movement": 5,
    "range": [3,4,5,6],
    "defense": HIGH_ARMOR,
    "type": WATER_TYPE,
    "spritesheet":unitSprites[CARRIER]
}
TRANSPORT_HELICOPTER = {
    "Name": "transport helicopter",
    "movement": 6,
    "range": 0,
    "defense": LOW_ARMOR,
    "type": AIR_TYPE,
    "spritesheet":unitSprites[TRANSPORT_HELICOPTER]
}
COMBAT_HELICOPTER = {
    "Name": "combat helicopter",
    "movement": 6,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": AIR_TYPE,
    "spritesheet":unitSprites[COMBAT_HELICOPTER]
}
FIGHTER_JET = {
    "Name": "fighter jet",
    "movement": 9,
    "range": 1,
    "defense": HIGH_ARMOR,
    "type": AIR_TYPE,
    "spritesheet":unitSprites[FIGHTER_JET]
}
BOMBER = {
    "Name": "bomber",
    "movement": 7,
    "range": 1,
    "defense": MEDIUM_ARMOR,
    "type": AIR_TYPE,
    "spritesheet":unitSprites[BOMBER]
}

