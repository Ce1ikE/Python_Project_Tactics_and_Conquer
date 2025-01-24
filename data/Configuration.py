# Game states helps us with keeping logic divided in our "main" game loop
PLAYING             = "playing"
CONTINUE            = "continue"
CREATING            = "creating_map"
MENU                = "menu"
MENU_HOW_TO_PLAY    = "how_to_play"
HUD_MENU_BUILDING   = "hud_building"
HUD_MENU_UNIT       = "hud_unit"
ATTACK_MODE         = "attack"
MOVE_MODE           = "move"
DEFEND_MODE         = "defend"
CAPTURE             = "capture" 
ANIMATION           = "animation"
QUIT                = "quit"

# --------------------------------------------------------------------------------------------------------------------------------------- #

# Possible players
PLAYER_1 = 0
PLAYER_2 = 1
PLAYER_3 = 2
PLAYER_4 = 3
GAIA     = 100
PLAYERS = {
    PLAYER_1 : "red",
    PLAYER_2 : "blue",
    PLAYER_3 : "yellow",
    PLAYER_4 : "green",
}

# required to easily handle multiple colored units in the "SPRITESHEET_PATH_UNITS" png file
PLAYERS_SPRITESHEET_OFFSET = {
    PLAYER_1 : [0 , 0],
    PLAYER_2 : [389,0],
    PLAYER_3 : [389,568],
    PLAYER_4 : [0,568],
}

PLAYERS_SPRITESHEET_OFFSET_2 = {
    PLAYER_1 : [0 , 0],
    PLAYER_2 : [0,132],
    PLAYER_3 : [0,397],
    PLAYER_4 : [0,264],
}

# Number of players
N_PLAYERS = 2

# framerate
FPS = 40


# World size in tiles
WORLD_X,WORLD_Y = 20 , 20

# Window size in px
WIN_X_PX,WIN_Y_PX = 640 , 640

# Spritesheet tile size in px (original), and upscale factor 
# tile size is unchangable which means the upscale factor must be determined depending on the window size
TILESIZE_8  = 8  # a 8px based tile
TILESIZE    = 16 # default  
TILESIZE_24 = 24 # a 24px based tile 
TILESIZE_32 = 32 # a 32px based tile
TILESIZE_48 = 48 # a 48px based tile
TILESIZE_64 = 64 # a 64px based tile

SCALETILE = int((WIN_Y_PX / 10) / TILESIZE)

# World size in px
WORLD_X_PX = WORLD_X*TILESIZE*SCALETILE
WORLD_Y_PX = WORLD_Y*TILESIZE*SCALETILE

# Window size in tiles     !! Window_size < World_size
WIN_X = int(WIN_X_PX/(SCALETILE*TILESIZE))
WIN_Y = int(WIN_Y_PX/(SCALETILE*TILESIZE))

# Camera position in tiles
CAMERA_X = WORLD_X - WIN_X
CAMERA_Y = WORLD_Y - WIN_Y

# Directions (clockwise)
NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

# Tile + Unit types required to match the unit to terrain
LAND_TYPE       = "land"
WATER_TYPE      = "water"
AIR_TYPE        = "air"
MOUNTAIN_TYPE   = "mountain"

# --------------------------------------------------------------------------------------------------------------------------------------- #
#
#      _______              __      __                 
#     /       \            /  |    /  |                
#     $$$$$$$  | ______   _$$ |_   $$ |____    _______ 
#     $$ |__$$ |/      \ / $$   |  $$      \  /       |
#     $$    $$/ $$$$$$  |$$$$$$/   $$$$$$$  |/$$$$$$$/ 
#     $$$$$$$/  /    $$ |  $$ | __ $$ |  $$ |$$      \ 
#     $$ |     /$$$$$$$ |  $$ |/  |$$ |  $$ | $$$$$$  |
#     $$ |     $$    $$ |  $$  $$/ $$ |  $$ |/     $$/ 
#     $$/       $$$$$$$/    $$$$/  $$/   $$/ $$$$$$$/  
#     
# PATHS ARE DEFINED BASED ON WORKING DIRECTORY
# Path to the spritesheets we use
SPRITESHEET_PATH_TILES               = "./assets/png/GBA_AW_Tiles.png"
 
SPRITESHEET_PATH_CURSOR_1            = "./assets/png/cursor+attack.png"
SPRITESHEET_PATH_CURSOR_2            = "./assets/png/cursor+default.png"
 
SPRITESHEET_PATH_UNITS               = "./assets/png/GBA_AW_Units.png"
 
SPRITESHEET_PATH_HUD                 = "./assets/png/GBA_AW_HUD.png"
SPRITESHEET_PATH_HUD_NEXT_PLAYER     = "./assets/png/icon_next_player.png"
SPRITESHEET_PATH_HUD_PAUSE           = "./assets/png/icon_pause.png"
SPRITESHEET_PATH_HUD_PLAY            = "./assets/png/icon_play.png"
SPRITESHEET_PATH_HUD_ATTACK          = "./assets/png/icon_fire.png"
SPRITESHEET_PATH_HUD_CAPTURE         = "./assets/png/icon_capture.png"
SPRITESHEET_PATH_HUD_DEFEND          = "./assets/png/icon_wait.png"
SPRITESHEET_PATH_HUD_GENERAL_ICONS   = "./assets/png/General_ICON_Sprites.png"
SPRITESHEET_PATH_HUD_UNITS           = "./assets/png/GBA_AW_2_Black_Hole_Rising_Units.png"
 
SPRITESHEET_PATH_CAPTURE_ANIMATION   = "./assets/png/AW_Capture_Sprites.png"
SPRITESHEET_PATH_CAPTURE_ANIMATION_2 = "./assets/png/AW1Sprites.png"

SPRITESHEET_PATH_KEYBOARDS_INPUT_EX  = "./assets/png/Keyboard_Extras.png"
SPRITESHEET_PATH_KEYBOARDS_INPUT_SY  = "./assets/png/Keyboard_Letters_and_Symbols.png"
SPRITESHEET_PATH_KEYBOARDS_INPUT_MO  = "./assets/png/Mouse.png"
 
# Path to fonts 
FONT_PATH_GREYBEARD                  = "./assets/fonts/Greybeard.ttf"
 
# Path to style (json) 
MAIN_MENU_STYLE                      = "./data/Main_Menu_style.json"
MAIN_GAME_STYLE                      = "./data/Tactics_and_Conquer_style.json"

# --------------------------------------------------------------------------------------------------------------------------------------- #
#   
#    ________  __  __                     
#   /        |/  |/  |                    
#   $$$$$$$$/ $$/ $$ |  ______    _______ 
#      $$ |   /  |$$ | /      \  /       |
#      $$ |   $$ |$$ |/$$$$$$  |/$$$$$$$/ 
#      $$ |   $$ |$$ |$$    $$ |$$      \ 
#      $$ |   $$ |$$ |$$$$$$$$/  $$$$$$  |
#      $$ |   $$ |$$ |$$       |/     $$/ 
#      $$/    $$/ $$/  $$$$$$$/ $$$$$$$/  
#   
# Tile Types
TILE_GRASS                = 0
TILE_WATER                = 1
TILE_FOREST               = 2
TILE_COAST_N              = 3
TILE_COAST_E              = 4
TILE_COAST_S              = 5
TILE_COAST_W              = 6
TILE_COAST_NE             = 7
TILE_COAST_SE             = 8
TILE_COAST_SW             = 9
TILE_COAST_NW             = 10
TILE_MOUNTAIN             = 11
TILE_ROAD_N               = 12
TILE_ROAD_E               = 13
TILE_ROAD_NE              = 14
TILE_ROAD_SE              = 15
TILE_ROAD_SW              = 16
TILE_ROAD_NW              = 17
TILE_WATER_NW             = 18
TILE_WATER_NE             = 19
TILE_WATER_SW             = 20
TILE_WATER_SE             = 21
TILE_FOREST_N             = 22
TILE_FOREST_S             = 23 
TILE_FOREST_W             = 24
TILE_FOREST_E             = 25
TILE_FOREST_NE            = 26
TILE_FOREST_SE            = 27
TILE_FOREST_NW            = 28
TILE_FOREST_SW            = 29
TILE_MOUTAIN_SW           = 30
TILE_MOUTAIN_N            = 31
TILE_HQ                   = 50        
TILE_CITY                 = 51
TILE_BARRACKS             = 52
TILE_AIRPORT              = 53
TILE_DOCK                 = 54
TILE_HQ_RED               = 100
TILE_CITY_RED             = 101
TILE_BARRACKS_RED         = 102
TILE_AIRPORT_RED          = 103
TILE_DOCK_RED             = 104
TILE_HQ_BLUE              = 130
TILE_CITY_BLUE            = 131
TILE_BARRACKS_BLUE        = 132
TILE_AIRPORT_BLUE         = 133
TILE_DOCK_BLUE            = 134
TILE_HQ_YELLOW            = 160
TILE_CITY_YELLOW          = 161
TILE_BARRACKS_YELLOW      = 162
TILE_AIRPORT_YELLOW       = 163
TILE_DOCK_YELLOW          = 164
TILE_HQ_GREEN             = 190
TILE_CITY_GREEN           = 191
TILE_BARRACKS_GREEN       = 192
TILE_AIRPORT_GREEN        = 193
TILE_DOCK_GREEN           = 194
TILE_BLANK                = 400

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
TILE_RULESET = {
    TILE_GRASS            : [GRASS, GRASS, GRASS, GRASS],
    TILE_WATER            : [WATER, WATER, WATER, WATER],
    TILE_FOREST           : [FOREST, FOREST, FOREST, FOREST],
    TILE_MOUNTAIN         : [MOUNTAIN, MOUNTAIN, MOUNTAIN, MOUNTAIN],
           
    TILE_COAST_N          : [GRASS, COAST_N, WATER, COAST_N],
    TILE_COAST_E          : [COAST_E, GRASS, COAST_E, WATER],
    TILE_COAST_S          : [WATER, COAST_S, GRASS, COAST_S],
    TILE_COAST_W          : [COAST_W, WATER, COAST_W, GRASS],
           
    TILE_COAST_NE         : [GRASS, GRASS, COAST_E, COAST_N],
    TILE_COAST_SE         : [COAST_E, GRASS, GRASS, COAST_S],
    TILE_COAST_SW         : [COAST_W, COAST_S, GRASS, GRASS],
    TILE_COAST_NW         : [GRASS, COAST_N, COAST_W, GRASS],
           
    TILE_MOUTAIN_SW        : [GRASS, GRASS, MOUNTAIN, MOUNTAIN],
    TILE_MOUTAIN_N         : [MOUNTAIN, GRASS, GRASS, GRASS],
           
    TILE_ROAD_N           : [ROAD_N, FOREST, ROAD_N, FOREST],
    TILE_ROAD_E           : [FOREST, ROAD_E, FOREST, ROAD_E],
    TILE_ROAD_NE          : [ROAD_N, ROAD_E, GRASS, GRASS],
    TILE_ROAD_SE          : [GRASS, ROAD_E, ROAD_N, GRASS],
    TILE_ROAD_SW          : [GRASS, GRASS, ROAD_N, ROAD_E],
    TILE_ROAD_NW          : [ROAD_N, GRASS, GRASS, ROAD_E],
           
    TILE_WATER_NW         : [WATER, COAST_S, COAST_E, WATER],
    TILE_WATER_NE         : [WATER, WATER, COAST_W, COAST_S],
    TILE_WATER_SW         : [COAST_E, COAST_N, WATER, WATER],
    TILE_WATER_SE         : [COAST_W, WATER, WATER, COAST_N],
           
    TILE_FOREST_N         : [FOREST, FOREST_N, GRASS, FOREST_N],
    TILE_FOREST_S         : [GRASS, FOREST_S, FOREST, FOREST_S],
    TILE_FOREST_W         : [FOREST_W, GRASS, FOREST_W, FOREST],
    TILE_FOREST_E         : [FOREST_E, FOREST, FOREST_E, GRASS],
           
    TILE_FOREST_NE        : [FOREST_E, FOREST_N, GRASS, GRASS],
    TILE_FOREST_SE        : [GRASS, FOREST_S, FOREST_E, GRASS],
    TILE_FOREST_NW        : [FOREST_W, GRASS, GRASS, FOREST_N],
    TILE_FOREST_SW        : [GRASS, GRASS, FOREST_E, FOREST_S],

    TILE_HQ               : [GRASS, GRASS, GRASS, GRASS], 
    TILE_CITY             : [GRASS, GRASS, GRASS, GRASS],
    TILE_BARRACKS         : [GRASS,GRASS,GRASS,GRASS], 
    TILE_AIRPORT          : [GRASS,GRASS,GRASS,GRASS], 
    TILE_DOCK             : [WATER,COAST_N,GRASS,COAST_N], 
    
    TILE_HQ_RED           : [GRASS,GRASS,GRASS,GRASS],
    TILE_CITY_RED         : [GRASS,GRASS,GRASS,GRASS],
    TILE_BARRACKS_RED     : [GRASS,GRASS,GRASS,GRASS],
    TILE_AIRPORT_RED      : [GRASS,GRASS,GRASS,GRASS],
    TILE_DOCK_RED         : [WATER,COAST_N,GRASS,COAST_N],

    TILE_HQ_BLUE          : [GRASS,GRASS,GRASS,GRASS],
    TILE_CITY_BLUE        : [GRASS,GRASS,GRASS,GRASS],
    TILE_BARRACKS_BLUE    : [GRASS,GRASS,GRASS,GRASS],
    TILE_AIRPORT_BLUE     : [GRASS,GRASS,GRASS,GRASS],
    TILE_DOCK_BLUE        : [WATER,COAST_N,GRASS,COAST_N],


    TILE_HQ_YELLOW            : [GRASS,GRASS,GRASS,GRASS],
    TILE_CITY_YELLOW          : [GRASS,GRASS,GRASS,GRASS],
    TILE_BARRACKS_YELLOW      : [GRASS,GRASS,GRASS,GRASS],
    TILE_AIRPORT_YELLOW       : [GRASS,GRASS,GRASS,GRASS],
    TILE_DOCK_YELLOW          : [WATER,COAST_N,GRASS,COAST_N],

    TILE_HQ_GREEN             : [GRASS,GRASS,GRASS,GRASS],
    TILE_CITY_GREEN           : [GRASS,GRASS,GRASS,GRASS],
    TILE_BARRACKS_GREEN       : [GRASS,GRASS,GRASS,GRASS],
    TILE_AIRPORT_GREEN        : [GRASS,GRASS,GRASS,GRASS],
    TILE_DOCK_GREEN           : [WATER,COAST_N,GRASS,COAST_N],

    TILE_BLANK            : [TILE_BLANK, TILE_BLANK, TILE_BLANK, TILE_BLANK],
}

# Dictionary of all tiles containing:
# [ TILE_WEIGHT, TILE_TYPE, TILE_COST, TILE_DEFENSE]
TILE_ATTRIBUTES = {
    TILE_GRASS                : [ 150    ,LAND_TYPE      ,1 ,1],
    TILE_WATER                : [ 5      ,WATER_TYPE     ,2 ,2],
    TILE_FOREST               : [ 3      ,LAND_TYPE      ,4 ,4],
    TILE_COAST_N              : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_E              : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_S              : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_W              : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_NE             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_SE             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_SW             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_COAST_NW             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_MOUNTAIN             : [ 3      ,MOUNTAIN_TYPE  ,1 ,1],
    TILE_ROAD_N               : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_ROAD_E               : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_ROAD_NE              : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_ROAD_SE              : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_ROAD_SW              : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_ROAD_NW              : [ 0      ,LAND_TYPE      ,1 ,1],
    TILE_WATER_NW             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_WATER_NE             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_WATER_SW             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_WATER_SE             : [ 3      ,LAND_TYPE      ,1 ,1],
    TILE_FOREST_N             : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_S             : [ 4      ,LAND_TYPE      ,3 ,3], 
    TILE_FOREST_W             : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_E             : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_NE            : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_SE            : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_NW            : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_FOREST_SW            : [ 4      ,LAND_TYPE      ,3 ,3],
    TILE_MOUTAIN_SW           : [ 0      ,MOUNTAIN_TYPE  ,5 ,5],
    TILE_MOUTAIN_N            : [ 0      ,MOUNTAIN_TYPE  ,5 ,5],
    TILE_HQ                   : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_CITY                 : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BARRACKS             : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_AIRPORT              : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_DOCK                 : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_HQ_RED               : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_CITY_RED             : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BARRACKS_RED         : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_AIRPORT_RED          : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_DOCK_RED             : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_HQ_BLUE              : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_CITY_BLUE            : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BARRACKS_BLUE        : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_AIRPORT_BLUE         : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_DOCK_BLUE            : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_HQ_YELLOW            : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_CITY_YELLOW          : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BARRACKS_YELLOW      : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_AIRPORT_YELLOW       : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_DOCK_YELLOW          : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_HQ_GREEN             : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_CITY_GREEN           : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BARRACKS_GREEN       : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_AIRPORT_GREEN        : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_DOCK_GREEN           : [ 0      ,LAND_TYPE      ,5 ,5],
    TILE_BLANK                : [ 0      ,None           ,0 ,0],
}

# Tile Spritesheets -> Tile coordinates (coord_x,coord_y,TILESIZE,TILESIZE)
# Dictionary of all tile coordinates in the SPRITESHEET_PATH_TILES
tileSprites = {
    TILE_GRASS            : [3,14,TILESIZE,TILESIZE],
    TILE_WATER            : [20,129,TILESIZE,TILESIZE],
    TILE_FOREST           : [20,48,TILESIZE,TILESIZE],
    TILE_COAST_N          : [224,129,TILESIZE,TILESIZE],
    TILE_COAST_E          : [241,146,TILESIZE,TILESIZE],
    TILE_COAST_S          : [224,163,TILESIZE,TILESIZE],
    TILE_COAST_W          : [207,146,TILESIZE,TILESIZE],
    TILE_COAST_NE         : [241,129,TILESIZE,TILESIZE],
    TILE_COAST_SE         : [241,163,TILESIZE,TILESIZE],
    TILE_COAST_SW         : [207,163,TILESIZE,TILESIZE],
    TILE_COAST_NW         : [207,129,TILESIZE,TILESIZE],
    TILE_MOUNTAIN         : [105,31,TILESIZE,TILESIZE],
    TILE_ROAD_N           : [173,65,TILESIZE,TILESIZE],
    TILE_ROAD_E           : [156,65,TILESIZE,TILESIZE],
    TILE_ROAD_NE          : [156,48,TILESIZE,TILESIZE],
    TILE_ROAD_SE          : [156,14,TILESIZE,TILESIZE],
    TILE_ROAD_SW          : [190,14,TILESIZE,TILESIZE],
    TILE_ROAD_NW          : [190,48,TILESIZE,TILESIZE],
    TILE_WATER_NW         : [156,82,TILESIZE,TILESIZE],
    TILE_WATER_NE         : [190,82,TILESIZE,TILESIZE],
    TILE_WATER_SW         : [173,82,TILESIZE,TILESIZE],
    TILE_WATER_SE         : [207,82,TILESIZE,TILESIZE],
    TILE_FOREST_N         : [20,65,TILESIZE,TILESIZE], 
    TILE_FOREST_S         : [20,31,TILESIZE,TILESIZE],  
    TILE_FOREST_W         : [37,48,TILESIZE,TILESIZE], 
    TILE_FOREST_E         : [3,48,TILESIZE,TILESIZE], 
    TILE_FOREST_NE        : [3,65,TILESIZE,TILESIZE], 
    TILE_FOREST_SE        : [3,31,TILESIZE,TILESIZE], 
    TILE_FOREST_NW        : [37,65,TILESIZE,TILESIZE], 
    TILE_FOREST_SW        : [37,31,TILESIZE,TILESIZE],
    TILE_MOUTAIN_SW       : [88,14,TILESIZE,TILESIZE],
    TILE_MOUTAIN_N        : [88,31,TILESIZE,TILESIZE],
    TILE_HQ               : [3,1212,TILESIZE,TILESIZE_32],
    TILE_CITY             : [88,1212,TILESIZE,TILESIZE_32],
    TILE_BARRACKS         : [105,1212,TILESIZE,TILESIZE_32], 
    TILE_AIRPORT          : [122,1212,TILESIZE,TILESIZE_32], 
    TILE_DOCK             : [139,1212,TILESIZE,TILESIZE_32], 
    TILE_HQ_RED           : [3,1034,TILESIZE,TILESIZE_32],
    TILE_CITY_RED         : [88,1034,TILESIZE,TILESIZE_32],
    TILE_BARRACKS_RED     : [105,1034,TILESIZE,TILESIZE_32],
    TILE_AIRPORT_RED      : [122,1034,TILESIZE,TILESIZE_32],
    TILE_DOCK_RED         : [139,1034,TILESIZE,TILESIZE_32],
    TILE_HQ_BLUE          : [20,1067,TILESIZE,TILESIZE_32],
    TILE_CITY_BLUE        : [88,1067,TILESIZE,TILESIZE_32],
    TILE_BARRACKS_BLUE    : [105,1067,TILESIZE,TILESIZE_32],
    TILE_AIRPORT_BLUE     : [122,1067,TILESIZE,TILESIZE_32],
    TILE_DOCK_BLUE        : [139,1067,TILESIZE,TILESIZE_32],
    TILE_HQ_YELLOW        : [37,1100,TILESIZE,TILESIZE_32],
    TILE_CITY_YELLOW      : [88,1100,TILESIZE,TILESIZE_32],
    TILE_BARRACKS_YELLOW  : [105,1100,TILESIZE,TILESIZE_32],
    TILE_AIRPORT_YELLOW   : [122,1100,TILESIZE,TILESIZE_32],
    TILE_DOCK_YELLOW      : [139,1100,TILESIZE,TILESIZE_32],
    TILE_HQ_GREEN         : [54,1133,TILESIZE,TILESIZE_32],
    TILE_CITY_GREEN       : [88,1133,TILESIZE,TILESIZE_32],
    TILE_BARRACKS_GREEN   : [105,1133,TILESIZE,TILESIZE_32],
    TILE_AIRPORT_GREEN    : [122,1133,TILESIZE,TILESIZE_32],
    TILE_DOCK_GREEN       : [139,1133,TILESIZE,TILESIZE_32],
    TILE_BLANK            : [224,82,TILESIZE,TILESIZE],
}

# All cursor sprites
CURSOR_SPRITES = [
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

# unit info sprites
unitsRemaining = {
    1 : [556,1233,TILESIZE_8,TILESIZE_8],
    2 : [565,1233,TILESIZE_8,TILESIZE_8],
    3 : [574,1233,TILESIZE_8,TILESIZE_8],
    4 : [583,1233,TILESIZE_8,TILESIZE_8],
    5 : [592,1233,TILESIZE_8,TILESIZE_8],
    6 : [601,1233,TILESIZE_8,TILESIZE_8],
    7 : [610,1233,TILESIZE_8,TILESIZE_8],
    8 : [619,1233,TILESIZE_8,TILESIZE_8],
    9 : [628,1233,TILESIZE_8,TILESIZE_8],
}

# Potenial Captures
POTENIAL_CAPTURES = [
    TILE_HQ              ,
    TILE_CITY            ,                 
    TILE_BARRACKS        ,             
    TILE_AIRPORT         ,              
    TILE_DOCK            ,                 
    TILE_HQ_RED          ,               
    TILE_CITY_RED        ,             
    TILE_BARRACKS_RED    ,         
    TILE_AIRPORT_RED     ,          
    TILE_DOCK_RED        ,             
    TILE_HQ_BLUE         ,              
    TILE_CITY_BLUE       ,            
    TILE_BARRACKS_BLUE   ,        
    TILE_AIRPORT_BLUE    ,         
    TILE_DOCK_BLUE       ,
    TILE_CITY_YELLOW     ,
    TILE_BARRACKS_YELLOW ,
    TILE_AIRPORT_YELLOW  ,
    TILE_DOCK_YELLOW     ,
    TILE_HQ_GREEN        ,
    TILE_CITY_GREEN      ,
    TILE_BARRACKS_GREEN  ,
    TILE_AIRPORT_GREEN   ,
    TILE_DOCK_GREEN      ,           
]

WINNING_CAPTURES = [
    TILE_HQ_RED,
    TILE_HQ_BLUE,
    TILE_HQ_YELLOW,
    TILE_HQ_GREEN,
]

CAPTURE_MATRIX = {
    PLAYER_1 : {
        TILE_HQ :     TILE_HQ_RED,
        TILE_CITY :   TILE_CITY_RED,
        TILE_BARRACKS : TILE_BARRACKS_RED,
        TILE_AIRPORT : TILE_AIRPORT_RED,
    },
    PLAYER_2 :{
        TILE_HQ :     TILE_HQ_BLUE,
        TILE_CITY :   TILE_CITY_BLUE,
        TILE_BARRACKS : TILE_BARRACKS_BLUE,
        TILE_AIRPORT : TILE_AIRPORT_BLUE,
    },
    PLAYER_3 :{
        TILE_HQ :     TILE_HQ_YELLOW,
        TILE_CITY :   TILE_CITY_YELLOW,
        TILE_BARRACKS : TILE_BARRACKS_YELLOW,
        TILE_AIRPORT : TILE_AIRPORT_YELLOW,
    },
    PLAYER_4 :{
        TILE_HQ :     TILE_HQ_GREEN,
        TILE_CITY :   TILE_CITY_GREEN,
        TILE_BARRACKS : TILE_BARRACKS_GREEN,
        TILE_AIRPORT : TILE_AIRPORT_GREEN,
    },
}


# Potenial Training Units 
POTENIAL_TRAINING = [
    TILE_HQ_RED         ,
    TILE_BARRACKS_RED   ,         
    TILE_AIRPORT_RED    ,          
    TILE_DOCK_RED       ,             
    TILE_HQ_BLUE        , 
    TILE_BARRACKS_BLUE  ,        
    TILE_AIRPORT_BLUE   ,         
    TILE_DOCK_BLUE      ,
    TILE_BARRACKS_YELLOW,
    TILE_AIRPORT_YELLOW ,
    TILE_DOCK_YELLOW    ,
    TILE_HQ_GREEN       ,
    TILE_BARRACKS_GREEN ,
    TILE_AIRPORT_GREEN  ,
    TILE_DOCK_GREEN     , 
]

# --------------------------------------------------------------------------------------------------------------------------------------- #
#     
#      __    __            __    __              
#     /  |  /  |          /  |  /  |             
#     $$ |  $$ | _______  $$/  _$$ |_    _______ 
#     $$ |  $$ |/       \ /  |/ $$   |  /       |
#     $$ |  $$ |$$$$$$$  |$$ |$$$$$$/  /$$$$$$$/ 
#     $$ |  $$ |$$ |  $$ |$$ |  $$ | __$$      \ 
#     $$ \__$$ |$$ |  $$ |$$ |  $$ |/  |$$$$$$  |
#     $$    $$/ $$ |  $$ |$$ |  $$  $$//     $$/ 
#      $$$$$$/  $$/   $$/ $$/    $$$$/ $$$$$$$/  
#     
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

# Armor types
LOW_ARMOR = 1
MEDIUM_ARMOR = 3
HIGH_ARMOR = 5

CAPTURE_AVAILABLE_ICON   = "captureAvailableIcon"
CAPTURE_UNAVAILABLE_ICON = "captureUnavailableIcon"

UNIT_ICONS = {
    PLAYER_1 : {
        CAPTURE_AVAILABLE_ICON   : [529,1233,8,8],
        CAPTURE_UNAVAILABLE_ICON : [401,1233,8,8]
    },
    PLAYER_2 : {
        CAPTURE_AVAILABLE_ICON   : [529,1242,8,8],
        CAPTURE_UNAVAILABLE_ICON : [401,1242,8,8]
    },
    PLAYER_3 : {
        CAPTURE_AVAILABLE_ICON   : [529,1260,8,8],
        CAPTURE_UNAVAILABLE_ICON : [401,1260,8,8]
    },
    PLAYER_4 : {
        CAPTURE_AVAILABLE_ICON   : [529,1251,8,8],
        CAPTURE_UNAVAILABLE_ICON : [401,1251,8,8]
    },
}

# get remaing numbers by :
# 556 + n*9,1233
# with n in [ 0 , 9 [ 
UNIT_REMAINING_ICONS = [556,1233,8,8]

UNITS_CAN_CAPTURE = [
    INFANTRY,
    HEAVY_INFANTRY
]

# All units cost
UNITS_COST = {
    INFANTRY                : 1000,
    HEAVY_INFANTRY          : 3000,
    TANK                    : 7000,
    MEDIUM_TANK             : 16000,
    HEAVY_TANK              : 22000,
    ARTILLERY               : 6000,
    HEAVY_ARTILLERY         : 15000,
    AA_TANK                 : 8000,
    APC                     : 5000,
    SUBMARINE               : 20000, 
    DESTROYER               : 18000,     
    LANDER                  : 12000, 
    CARRIER                 : 28000, 
    TRANSPORT_HELICOPTER    : 5000,  
    COMBAT_HELICOPTER       : 9000, 
    FIGHTER_JET             : 20000, 
    BOMBER                  : 22000, 
}

UNITS_NAMES = {
    INFANTRY                : "Infantry",
    HEAVY_INFANTRY          : "Mech",
    TANK                    : "Tank",
    MEDIUM_TANK             : "Md Tank",
    HEAVY_TANK              : "Hvy Tank",
    ARTILLERY               : "Artly",
    HEAVY_ARTILLERY         : "Hvy Artly",
    AA_TANK                 : "A-Air",
    APC                     : "APC",
    SUBMARINE               : "Sub", 
    DESTROYER               : "Destroyer",     
    LANDER                  : "Lander", 
    CARRIER                 : "Carrier", 
    TRANSPORT_HELICOPTER    : "T-Heli",  
    COMBAT_HELICOPTER       : "B-Heli", 
    FIGHTER_JET             : "Fghtr", 
    BOMBER                  : "Bomber", 
}

# to get the following sprites for different teams i offset the origin coordinates by the
# coordinates found in "PLAYERS_SPRITESHEET_OFFSET" (look at top of file)
# example: 
# --------
# => old_coord = [ O_x , O_y , TILESIZE , TILESIZE ]
# => O_dx = PLAYERS_SPRITESHEET_OFFSET[PLAYER_2][0] (Blue player) 
# => O_dy = PLAYERS_SPRITESHEET_OFFSET[PLAYER_2][1] 
# => new_coord = [ O_x + O_dx , O_y + O_dy , TILESIZE , TILESIZE ]
# 
# [
# [LEFT_1]      ,[LEFT_2]       ,[LEFT_3]   ,
# [DOWN_1]      ,[DOWN_2]       ,[DOWN_3]   ,
# [UP_1]        ,[UP_2]         ,[UP_3]     ,
# [RIGHT_1]     ,[RIGHT_2]      ,[RIGHT_3]  ,
# [IDLE_L_1]    ,[IDLE_L_2]     ,[IDLE_L_3] ,
# [IDLE_R_1]    ,[IDLE_R_2]     ,[IDLE_R_3] ,
# [UNA_L_1]     ,[UNA_L_2]      ,[UNA_L_3]  ,
# [UNA_R_1]     ,[UNA_R_2]      ,[UNA_R_3]  ,
# ]
UNITS_SPRITES = {
    INFANTRY                : [
        [56,104,TILESIZE_24,TILESIZE_24],   [81,104,TILESIZE_24,TILESIZE_24],   [106,104,TILESIZE_24,TILESIZE_24], # 16x24
        [56,129,TILESIZE_24,TILESIZE_24],   [81,129,TILESIZE_24,TILESIZE_24],   [106,129,TILESIZE_24,TILESIZE_24], # 16x24
        [56,154,TILESIZE_24,TILESIZE_24],   [81,154,TILESIZE_24,TILESIZE_24],   [106,154,TILESIZE_24,TILESIZE_24], # 16x24
        [56,104,TILESIZE_24,TILESIZE_24],   [81,104,TILESIZE_24,TILESIZE_24],   [106,104,TILESIZE_24,TILESIZE_24], # 16x24 # must apply a pygame.transform.scale_x(-1)
        [3,104,TILESIZE,TILESIZE],          [20,104,TILESIZE,TILESIZE],         [37,104,TILESIZE,TILESIZE], # 16x16
        [3,104,TILESIZE,TILESIZE],          [20,104,TILESIZE,TILESIZE],         [37,104,TILESIZE,TILESIZE], # 16x16 # must apply a pygame.transform.scale_x(-1)
        [339,104,TILESIZE,TILESIZE],        [356,104,TILESIZE,TILESIZE],        [373,104,TILESIZE,TILESIZE], # 16x16 
        [339,104,TILESIZE,TILESIZE],        [356,104,TILESIZE,TILESIZE],        [373,104,TILESIZE,TILESIZE], # 16x16 # must apply a pygame.transform.scale_x(-1)
    ], 
    HEAVY_INFANTRY          : [
        [133,104,TILESIZE_24,TILESIZE_24],  [158,104,TILESIZE_24,TILESIZE_24],  [183,104,TILESIZE_24,TILESIZE_24],
        [133,129,TILESIZE_24,TILESIZE_24],  [158,129,TILESIZE_24,TILESIZE_24],  [183,129,TILESIZE_24,TILESIZE_24],
        [133,154,TILESIZE_24,TILESIZE_24],  [158,154,TILESIZE_24,TILESIZE_24],  [183,154,TILESIZE_24,TILESIZE_24],
        [133,104,TILESIZE_24,TILESIZE_24],  [158,104,TILESIZE_24,TILESIZE_24],  [183,104,TILESIZE_24,TILESIZE_24],
        [3,199,TILESIZE,TILESIZE],          [20,199,TILESIZE,TILESIZE],         [37,199,TILESIZE,TILESIZE], # 16x16
        [3,199,TILESIZE,TILESIZE],          [20,199,TILESIZE,TILESIZE],         [37,199,TILESIZE,TILESIZE],
        [339,199,TILESIZE,TILESIZE],        [356,199,TILESIZE,TILESIZE],        [373,199,TILESIZE,TILESIZE],  
        [339,199,TILESIZE,TILESIZE],        [356,199,TILESIZE,TILESIZE],        [373,199,TILESIZE,TILESIZE],  
    ], 
    TANK                    : [
        [133,489,TILESIZE_24,TILESIZE_24],  [158,489,TILESIZE_24,TILESIZE_24],  [183,489,TILESIZE_24,TILESIZE_24],
        [133,514,TILESIZE_24,TILESIZE_24],  [158,514,TILESIZE_24,TILESIZE_24],  [183,514,TILESIZE_24,TILESIZE_24],
        [133,539,TILESIZE_24,TILESIZE_24],  [158,539,TILESIZE_24,TILESIZE_24],  [183,539,TILESIZE_24,TILESIZE_24],
        [133,489,TILESIZE_24,TILESIZE_24],  [133,489,TILESIZE_24,TILESIZE_24],  [133,489,TILESIZE_24,TILESIZE_24],
        [3,313,TILESIZE,TILESIZE],          [20,313,TILESIZE,TILESIZE],         [37,313,TILESIZE,TILESIZE], # 16x16
        [3,313,TILESIZE,TILESIZE],          [20,313,TILESIZE,TILESIZE],         [37,313,TILESIZE,TILESIZE],
        [339,313,TILESIZE,TILESIZE],        [356,313,TILESIZE,TILESIZE],        [373,313,TILESIZE,TILESIZE],  
        [339,313,TILESIZE,TILESIZE],        [356,313,TILESIZE,TILESIZE],        [373,313,TILESIZE,TILESIZE],
    ], 
    MEDIUM_TANK             : [
        [56,566,TILESIZE_24,TILESIZE_24],   [81,566,TILESIZE_24,TILESIZE_24],   [106,566,TILESIZE_24,TILESIZE_24],
        [56,591,TILESIZE_24,TILESIZE_24],   [81,591,TILESIZE_24,TILESIZE_24],   [106,566,TILESIZE_24,TILESIZE_24],  
        [56,616,TILESIZE_24,TILESIZE_24],   [81,616,TILESIZE_24,TILESIZE_24],   [106,616,TILESIZE_24,TILESIZE_24],
        [56,566,TILESIZE_24,TILESIZE_24],   [81,566,TILESIZE_24,TILESIZE_24],   [106,566,TILESIZE_24,TILESIZE_24],
        [3,332,TILESIZE,TILESIZE],          [20,332,TILESIZE,TILESIZE],         [37,332,TILESIZE,TILESIZE], # 16x16
        [3,332,TILESIZE,TILESIZE],          [20,332,TILESIZE,TILESIZE],         [37,332,TILESIZE,TILESIZE],
        [339,332,TILESIZE,TILESIZE],        [356,332,TILESIZE,TILESIZE],        [373,332,TILESIZE,TILESIZE],
        [339,332,TILESIZE,TILESIZE],        [356,332,TILESIZE,TILESIZE],        [373,332,TILESIZE,TILESIZE],         
    ], 
    HEAVY_TANK              : [
        [133,566,TILESIZE_24,TILESIZE_24],  [158,566,TILESIZE_24,TILESIZE_24],  [183,566,TILESIZE_24,TILESIZE_24],
        [133,591,TILESIZE_24,TILESIZE_24],  [158,591,TILESIZE_24,TILESIZE_24],  [183,591,TILESIZE_24,TILESIZE_24],
        [133,616,TILESIZE_24,TILESIZE_24],  [158,616,TILESIZE_24,TILESIZE_24],  [183,616,TILESIZE_24,TILESIZE_24],
        [133,566,TILESIZE_24,TILESIZE_24],  [158,566,TILESIZE_24,TILESIZE_24],  [183,566,TILESIZE_24,TILESIZE_24],
        [3,351,TILESIZE,TILESIZE],          [20,351,TILESIZE,TILESIZE],         [37,351,TILESIZE,TILESIZE], # 16x16
        [3,351,TILESIZE,TILESIZE],          [20,351,TILESIZE,TILESIZE],         [37,351,TILESIZE,TILESIZE],
        [339,351,TILESIZE,TILESIZE],        [356,351,TILESIZE,TILESIZE],        [373,351,TILESIZE,TILESIZE],
        [339,351,TILESIZE,TILESIZE],        [356,351,TILESIZE,TILESIZE],        [373,351,TILESIZE,TILESIZE],
    ], 
    ARTILLERY               : [
        [210,335,TILESIZE_24,TILESIZE_24],  [235,335,TILESIZE_24,TILESIZE_24],  [260,335,TILESIZE_24,TILESIZE_24],
        [210,360,TILESIZE_24,TILESIZE_24],  [235,360,TILESIZE_24,TILESIZE_24],  [260,360,TILESIZE_24,TILESIZE_24],
        [210,385,TILESIZE_24,TILESIZE_24],  [235,385,TILESIZE_24,TILESIZE_24],  [260,385,TILESIZE_24,TILESIZE_24],
        [210,335,TILESIZE_24,TILESIZE_24],  [235,335,TILESIZE_24,TILESIZE_24],  [260,335,TILESIZE_24,TILESIZE_24],
        [3,408,TILESIZE,TILESIZE],          [20,408,TILESIZE,TILESIZE],         [37,408,TILESIZE,TILESIZE], # 16x16
        [3,408,TILESIZE,TILESIZE],          [20,408,TILESIZE,TILESIZE],         [37,408,TILESIZE,TILESIZE],
        [339,408,TILESIZE,TILESIZE],        [356,408,TILESIZE,TILESIZE],        [373,408,TILESIZE,TILESIZE],
        [339,408,TILESIZE,TILESIZE],        [356,408,TILESIZE,TILESIZE],        [373,408,TILESIZE,TILESIZE],
    ], 
    HEAVY_ARTILLERY         : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ], 
    AA_TANK                 : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ], 
    APC                     : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],           
    ], 
    SUBMARINE               : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],           
    ],  
    DESTROYER               : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],           
    ],    
    LANDER                  : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ],
    CARRIER                 : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ],
    TRANSPORT_HELICOPTER    : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ], 
    COMBAT_HELICOPTER       : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ],
    FIGHTER_JET             : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ],
    BOMBER                  : [
        [],[],[],
        [],[],[],
        [],[],[],
        [],[],[],  
        [],[],[], # 16x16
        [],[],[],
        [],[],[],
        [],[],[],          
    ],
}

# the base damage matrix :
# see => https://awbw.fandom.com/wiki/Damage_Formula
# however i do it a bit differently because i don't have every single statistic implemented
# in python :


#  baseDamage = unitsBaseDamage[ defendingUnit , AttackingUnit ] /100
#  luck       = random.randint(1,9) / 100
#  HP_unit    = healthAttackingUnit / 10

#  tileDef    = tileDefense[ tileType ] / 10 => lookup in map at position (U_x,U_y)
#  HP_enemy   = healthDefendingUnit / 10
#  

# damageDone  = ((baseDamage + luck) * HP_unit ) * (1 - tileDef)

#  healthDefendingUnit not 0 and DefendingUnit ranges AttackingUnit
#       repeat but swap


UNITS_BASE_DAMAGE = [
#   (01)   (02)  (03)  (04)  (05)  (06)  (07)  (08)  (09)  (10)  (11)  (12)  (13)  (14)  (15)  (16)  (17) => attacking unit
    [55,   65,   70,   75,   105,  125,  90,   95,   105,  None, None, None, None, 75,   None, 110,  None], #(01) Infantry
    [45,   55,   65,   70,   95,   115,  85,   90,   105,  None, None, None, None, 75,   None, 110,  None], #(02) Heavy Infantry (Mech)
    [12,   85,   35,   85,   105,  125,  80,   90,   60,   None, None, None, None, 55,   None, 105,  None], #(03) Tank
    [5,    55,   55,   85,   105,  70,   85,   70,   25,   None, None, None, None, 55,   None, 105,  None], #(04) Medium Tank
    [1,    15,   15,   55,   75,   45,   55,   40,   5,    None, None, None, None, 25,   None, 105,  None], #(05) Heavy Tank (Neotank)
    [14,   75,   45,   75,   125,  125,  90,   90,   50,   None, None, None, None, 105,  None, 90,   None], #(06) Artillery
    [15,   70,   45,   70,   115,  125,  80,   85,   45,   None, None, None, None, 65,   None, 85,   None], #(07) Heavy Artillery (Rockets)
    [25,   65,   85,   85,   115,  75,   85,   45,   55,   None, None, None, None, 120,  120,  65,   None], #(08) Anti-Air Tank
    [26,   85,   28,   85,   105,  80,   80,   55,   50,   None, None, None, None, 65,   None, 105,  None], #(09) APC
    [None, None, None, None, None, None, None, None, None, 55,   120,  None, None, None, None, None, None], #(10) Submarine
    [None, None, None, None, None, None, None, None, None, 90,   65,   85,   None, 100,  None, None, 95],   #(11) Destroyer (Cruiser)
    [None, None, None, None, None, None, None, None, None, 95,   95,   95,   95,   95,   None, None, None], #(12) Lander
    [None, None, None, None, None, None, None, None, None, 105,  105,  None, 95,   None, None, None, 95],   #(13) Carrier (Battleship)
    [None, 9,    None, None, None, None, None, None, None, None, None, None, None, 100,  55,   None, None], #(14) Transport Helicopter
    [30,   35,   35,   35,   45,   85,   75,   65,   55,   None, None, None, None, None, None, 65,   100],  #(15) Combat Helicopter (B-Copter)
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 55,   65,   55,   100],  #(16) Fighter Jet
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 75,   None, 100,  None]  #(17) Bomber
]

UNITS_NAME_TAGS = {
    INFANTRY                : [392,1567,TILESIZE_32,TILESIZE],
    HEAVY_INFANTRY          : [425,1567,TILESIZE_32,TILESIZE],
    TANK                    : [460,1567,TILESIZE_32,TILESIZE],
    MEDIUM_TANK             : [493,1567,TILESIZE_32,TILESIZE],
    HEAVY_TANK              : [559,1567,TILESIZE_32,TILESIZE],
    ARTILLERY               : [658,1567,TILESIZE_32,TILESIZE],
    HEAVY_ARTILLERY         : [691,1567,TILESIZE_32,TILESIZE],
    AA_TANK                 : [625,1567,TILESIZE_32,TILESIZE],
    APC                     : [592,1567,TILESIZE_32,TILESIZE],
    SUBMARINE               : [625,1586,TILESIZE_32,TILESIZE], 
    DESTROYER               : [526,1586,TILESIZE_32,TILESIZE],    
    LANDER                  : [592,1586,TILESIZE_32,TILESIZE],
    CARRIER                 : [559,1586,TILESIZE_32,TILESIZE],
    TRANSPORT_HELICOPTER    : [491,1586,TILESIZE_32,TILESIZE], 
    COMBAT_HELICOPTER       : [458,1586,TILESIZE_32,TILESIZE],
    FIGHTER_JET             : [392,1586,TILESIZE_32,TILESIZE],
    BOMBER                  : [425,1586,TILESIZE_32,TILESIZE],
}

# same as "unitSprites" to get the following sprites for different teams i offset the origin coordinates by the
# coordinates found in "PLAYERS_SPRITESHEET_OFFSET_2" (look at top of file)
# example: 
# --------
# => old_coord = [ O_x , O_y , TILESIZE , TILESIZE ]
# => O_dx = PLAYERS_SPRITESHEET_OFFSET[PLAYER_2][0] (Blue player) 
# => O_dy = PLAYERS_SPRITESHEET_OFFSET[PLAYER_2][1] 
# => new_coord = [ O_x + O_dx , O_y + O_dy , TILESIZE , TILESIZE ]
# HUD units sprites
UNITS_HUD_SPRITES = {
    INFANTRY                : [2,1,TILESIZE_64,TILESIZE_64 - 1], # TILESIZE_64 - 1 because this spritesheet is very annoying  
    HEAVY_INFANTRY          : [69,1,TILESIZE_64,TILESIZE_64 - 1],
    TANK                    : [203,1,TILESIZE_64,TILESIZE_64 - 1],
    MEDIUM_TANK             : [270,1,TILESIZE_64,TILESIZE_64 - 1],
    HEAVY_TANK              : [337,1,TILESIZE_64,TILESIZE_64 - 1],
    ARTILLERY               : [538,1,TILESIZE_64,TILESIZE_64 - 1],
    HEAVY_ARTILLERY         : [],
    AA_TANK                 : [],
    APC                     : [],
    SUBMARINE               : [], 
    DESTROYER               : [],    
    LANDER                  : [],
    CARRIER                 : [],
    TRANSPORT_HELICOPTER    : [], 
    COMBAT_HELICOPTER       : [],
    FIGHTER_JET             : [],
    BOMBER                  : [],
}

UNITS_RANGE = {
    INFANTRY                : 1,
    HEAVY_INFANTRY          : 1,
    TANK                    : 1,
    MEDIUM_TANK             : 1,
    HEAVY_TANK              : 1,
    ARTILLERY               : [2,3],
    HEAVY_ARTILLERY         : [2,3,5],
    AA_TANK                 : 1,
    APC                     : 0,
    SUBMARINE               : 1, 
    DESTROYER               : 1,    
    LANDER                  : 0,
    CARRIER                 : [3,4,5,6],
    TRANSPORT_HELICOPTER    : 0, 
    COMBAT_HELICOPTER       : 1,
    FIGHTER_JET             : 1,
    BOMBER                  : 1,
}

UNITS_MOVEMENT = {
    INFANTRY                : 3,
    HEAVY_INFANTRY          : 2,
    TANK                    : 6,
    MEDIUM_TANK             : 5,
    HEAVY_TANK              : 6,
    ARTILLERY               : 5,
    HEAVY_ARTILLERY         : 5,
    AA_TANK                 : 6,
    APC                     : 6,
    SUBMARINE               : 5, 
    DESTROYER               : 6,    
    LANDER                  : 6,
    CARRIER                 : 5,
    TRANSPORT_HELICOPTER    : 6, 
    COMBAT_HELICOPTER       : 6,
    FIGHTER_JET             : 9,
    BOMBER                  : 7,
}

# Units stats and data in dictionaries to have easily access to all required information
UNITS_DATA = {
    INFANTRY : {
        "unitType"      : INFANTRY,
        "name"          : UNITS_NAME_TAGS[INFANTRY],
        "movement"      : UNITS_MOVEMENT[INFANTRY],
        "range"         : UNITS_RANGE[INFANTRY],
        "defense"       : LOW_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[INFANTRY],
        "base_damage"   : UNITS_BASE_DAMAGE[INFANTRY], 
    },
    HEAVY_INFANTRY : {
        "unitType"      : HEAVY_INFANTRY,
        "name"          : UNITS_NAME_TAGS[HEAVY_INFANTRY],
        "movement"      : UNITS_MOVEMENT[HEAVY_INFANTRY],
        "range"         : UNITS_RANGE[HEAVY_INFANTRY],
        "defense"       : MEDIUM_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[HEAVY_INFANTRY],
        "base_damage"   : UNITS_BASE_DAMAGE[HEAVY_INFANTRY], 
    },
    TANK : {
        "unitType"      : TANK,
        "name"          : UNITS_NAME_TAGS[TANK],
        "movement"      : UNITS_MOVEMENT[TANK],
        "range"         : UNITS_RANGE[TANK],
        "defense"       : MEDIUM_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[TANK],
        "base_damage"   : UNITS_BASE_DAMAGE[TANK], 
    },
    MEDIUM_TANK : {
        "unitType"      : MEDIUM_TANK,
        "name"          : UNITS_NAME_TAGS[MEDIUM_TANK],
        "movement"      : UNITS_MOVEMENT[MEDIUM_TANK],
        "range"         : UNITS_RANGE[MEDIUM_TANK],
        "defense"       : HIGH_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[MEDIUM_TANK],
        "base_damage"   : UNITS_BASE_DAMAGE[MEDIUM_TANK], 
    },
    HEAVY_TANK : {
        "unitType"      : HEAVY_TANK,
        "name"          : UNITS_NAME_TAGS[HEAVY_TANK],
        "movement"      : UNITS_MOVEMENT[HEAVY_TANK],
        "range"         : UNITS_RANGE[HEAVY_TANK],
        "defense"       : HIGH_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[HEAVY_TANK],
        "base_damage"   : UNITS_BASE_DAMAGE[HEAVY_TANK], 
    },
    ARTILLERY : {
        "unitType"      : ARTILLERY,
        "name"          : UNITS_NAME_TAGS[ARTILLERY],
        "movement"      : UNITS_MOVEMENT[ARTILLERY],
        "range"         : UNITS_RANGE[ARTILLERY],
        "defense"       : LOW_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[ARTILLERY],
        "base_damage"   : UNITS_BASE_DAMAGE[ARTILLERY], 
    },
    HEAVY_ARTILLERY : {
        "unitType"      : HEAVY_ARTILLERY,
        "name"          : UNITS_NAME_TAGS[HEAVY_ARTILLERY],
        "movement"      : UNITS_MOVEMENT[HEAVY_ARTILLERY],
        "range"         : UNITS_RANGE[HEAVY_ARTILLERY],
        "defense"       : LOW_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[HEAVY_ARTILLERY],
        "base_damage"   : UNITS_BASE_DAMAGE[HEAVY_ARTILLERY], 
    },
    AA_TANK : {
        "unitType"      : AA_TANK,
        "name"          : UNITS_NAME_TAGS[AA_TANK],
        "movement"      : UNITS_MOVEMENT[AA_TANK],
        "range"         : UNITS_RANGE[AA_TANK],
        "defense"       : MEDIUM_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[AA_TANK],
        "base_damage"   : UNITS_BASE_DAMAGE[AA_TANK], 
    },
    APC : {
        "unitType"      : APC,
        "name"          : UNITS_NAME_TAGS[APC],
        "movement"      : UNITS_MOVEMENT[APC],
        "range"         : UNITS_RANGE[APC],
        "defense"       : MEDIUM_ARMOR,
        "type"          : LAND_TYPE,
        "spritesheet"   : UNITS_SPRITES[APC],
        "base_damage"   : UNITS_BASE_DAMAGE[APC], 
    },
    SUBMARINE : {
        "unitType"      : SUBMARINE,
        "name"          : UNITS_NAME_TAGS[SUBMARINE],
        "movement"      : UNITS_MOVEMENT[SUBMARINE],
        "range"         : UNITS_RANGE[SUBMARINE],
        "defense"       : MEDIUM_ARMOR,
        "type"          : WATER_TYPE,
        "spritesheet"   : UNITS_SPRITES[SUBMARINE],
        "base_damage"   : UNITS_BASE_DAMAGE[SUBMARINE], 
    },
    DESTROYER : {
        "unitType"      : DESTROYER,
        "name"          : UNITS_NAME_TAGS[DESTROYER],
        "movement"      : UNITS_MOVEMENT[DESTROYER],
        "range"         : UNITS_RANGE[DESTROYER],
        "defense"       : MEDIUM_ARMOR,
        "type"          : WATER_TYPE,
        "spritesheet"   : UNITS_SPRITES[DESTROYER],
        "base_damage"   : UNITS_BASE_DAMAGE[DESTROYER], 
    },
    LANDER : {
        "unitType"      : LANDER,
        "name"          : UNITS_NAME_TAGS[LANDER],
        "movement"      : UNITS_MOVEMENT[LANDER],
        "range"         : UNITS_RANGE[LANDER],
        "defense"       : LOW_ARMOR,
        "type"          : WATER_TYPE,
        "spritesheet"   : UNITS_SPRITES[LANDER],
        "base_damage"   : UNITS_BASE_DAMAGE[LANDER], 
    },
    CARRIER : {
        "unitType"      : CARRIER,
        "name"          : UNITS_NAME_TAGS[CARRIER],
        "movement"      : UNITS_MOVEMENT[CARRIER],
        "range"         : UNITS_RANGE[CARRIER],
        "defense"       : HIGH_ARMOR,
        "type"          : WATER_TYPE,
        "spritesheet"   : UNITS_SPRITES[CARRIER],
        "base_damage"   : UNITS_BASE_DAMAGE[CARRIER], 
    },
    TRANSPORT_HELICOPTER : {
        "unitType"      : TRANSPORT_HELICOPTER,
        "name"          : UNITS_NAME_TAGS[TRANSPORT_HELICOPTER],
        "movement"      : UNITS_MOVEMENT[TRANSPORT_HELICOPTER],
        "range"         : UNITS_RANGE[TRANSPORT_HELICOPTER],
        "defense"       : LOW_ARMOR,
        "type"          : AIR_TYPE,
        "spritesheet"   : UNITS_SPRITES[TRANSPORT_HELICOPTER],
        "base_damage"   : UNITS_BASE_DAMAGE[TRANSPORT_HELICOPTER], 
    },
    COMBAT_HELICOPTER : {
        "unitType"      : COMBAT_HELICOPTER,
        "name"          : UNITS_NAME_TAGS[COMBAT_HELICOPTER],
        "movement"      : UNITS_MOVEMENT[COMBAT_HELICOPTER],
        "range"         : UNITS_RANGE[COMBAT_HELICOPTER],
        "defense"       : MEDIUM_ARMOR,
        "type"          : AIR_TYPE,
        "spritesheet"   : UNITS_SPRITES[COMBAT_HELICOPTER],
        "base_damage"   : UNITS_BASE_DAMAGE[COMBAT_HELICOPTER], 
    },
    FIGHTER_JET : {
        "unitType"      : FIGHTER_JET,
        "name"          : UNITS_NAME_TAGS[FIGHTER_JET],
        "movement"      : UNITS_MOVEMENT[FIGHTER_JET],
        "range"         : UNITS_RANGE[FIGHTER_JET],
        "defense"       : HIGH_ARMOR,
        "type"          : AIR_TYPE,
        "spritesheet"   : UNITS_SPRITES[FIGHTER_JET],
        "base_damage"   : UNITS_BASE_DAMAGE[FIGHTER_JET], 
    },
    BOMBER : {
        "unitType"      : BOMBER,
        "name"          : UNITS_NAME_TAGS[BOMBER],
        "movement"      : UNITS_MOVEMENT[BOMBER],
        "range"         : UNITS_RANGE[BOMBER],
        "defense"       : MEDIUM_ARMOR,
        "type"          : AIR_TYPE,
        "spritesheet"   : UNITS_SPRITES[BOMBER],
        "base_damage"   : UNITS_BASE_DAMAGE[BOMBER], 
    },
}

# --------------------------------------------------------------------------------------------------------------------------------------- #
#     __       __  __                     
#    /  \     /  |/  |                    
#    $$  \   /$$ |$$/   _______   _______ 
#    $$$  \ /$$$ |/  | /       | /       |
#    $$$$  /$$$$ |$$ |/$$$$$$$/ /$$$$$$$/ 
#    $$ $$ $$/$$ |$$ |$$      \ $$ |      
#    $$ |$$$/ $$ |$$ | $$$$$$  |$$ \_____ 
#    $$ | $/  $$ |$$ |/     $$/ $$       |
#    $$/      $$/ $$/ $$$$$$$/   $$$$$$$/ 


CAPTURE_PANEL    = [205,398,TILESIZE_64,TILESIZE_64]
CAPTURE_COMPLETE = [271,398,TILESIZE_64,TILESIZE_32]
CAPTURE_UNIT = 1
# get all numbers by :
# CAPTURE_ANIMATION_NUMBERS[n][ x + (n-1)*10, y] 
# with n  in [ 0 ; 11 [
CAPTURE_ANIMATION_NUMBERS = [205,468,8,8]


# animations are:
# (1) the Unit_state_1      during the animation
# (2) the Unit_state_2      during the animation
# (3) the Unit_state_3      during the animation
# (4) the Unit_state_4      during the animation
# (5) the Unit_state_5      during the animation
# (6) the HQ                during the animation
# (7) the CITY              during the animation
# (8) the BARRACKS          during the animation
CAPTURE_ANIMATIONS = [
    [1,13,TILESIZE,TILESIZE_24],
    [18,13,TILESIZE,TILESIZE_24],
    [35,13,TILESIZE,TILESIZE_24],
    [54,13,TILESIZE,TILESIZE_24],           
    [35,148,TILESIZE_32,TILESIZE_64],               
    [205,148,TILESIZE_32,TILESIZE_48],                 
    [205,198,TILESIZE_32,TILESIZE_48],
]



# offsets are:
# (1) the Unit      during the animation
# (2) the HQ        during the animation
# (3) the CITY      during the animation
# (4) the BARRACKS  during the animation
CAPTURE_ANIMATION_PLAYER = {
    PLAYER_1 : {
        CAPTURE_UNIT : [
            [913,1448,TILESIZE,TILESIZE_32],
            [930,1448,TILESIZE,TILESIZE_32],
            [947,1448,TILESIZE,TILESIZE_32],
            [964,1448,TILESIZE,TILESIZE_32],
            [981,1448,TILESIZE,TILESIZE_32],
        ],
        TILE_HQ_RED :       [35,148,TILESIZE_32,TILESIZE_64],
        TILE_CITY_RED :     [239,148,TILESIZE_32,TILESIZE_48],
        TILE_BARRACKS_RED : [239,198,TILESIZE_32,TILESIZE_48],
    },
    PLAYER_2 : {
        CAPTURE_UNIT : [
            [1002,1448,TILESIZE,TILESIZE_32],
            [1019,1448,TILESIZE,TILESIZE_32],
            [1036,1448,TILESIZE,TILESIZE_32],
            [1053,1448,TILESIZE,TILESIZE_32],
            [1070,1448,TILESIZE,TILESIZE_32],
        ],
        TILE_HQ_BLUE :          [35,148,TILESIZE_32,TILESIZE_64],
        TILE_CITY_BLUE :        [239,148,TILESIZE_32,TILESIZE_48],
        TILE_BARRACKS_BLUE :    [239,198,TILESIZE_32,TILESIZE_48],
    },
    PLAYER_3 : {
        CAPTURE_UNIT : [
            [1002,1481,TILESIZE,TILESIZE_32],
            [1019,1481,TILESIZE,TILESIZE_32],
            [1036,1481,TILESIZE,TILESIZE_32],
            [1053,1481,TILESIZE,TILESIZE_32],
            [1070,1481,TILESIZE,TILESIZE_32],
        ],
        TILE_HQ_YELLOW :        [35,148,TILESIZE_32,TILESIZE_64],
        TILE_CITY_YELLOW :      [239,148,TILESIZE_32,TILESIZE_48],
        TILE_BARRACKS_YELLOW :  [239,198,TILESIZE_32,TILESIZE_48],
    },
    PLAYER_4 : {
        CAPTURE_UNIT : [
            [913,1481,TILESIZE,TILESIZE_32],
            [930,1481,TILESIZE,TILESIZE_32],
            [947,1481,TILESIZE,TILESIZE_32],
            [964,1481,TILESIZE,TILESIZE_32],
            [981,1481,TILESIZE,TILESIZE_32],
        ],
        TILE_HQ_GREEN :         [35,148,TILESIZE_32,TILESIZE_64],
        TILE_CITY_GREEN :       [239,148,TILESIZE_32,TILESIZE_48],
        TILE_BARRACKS_GREEN :   [239,198,TILESIZE_32,TILESIZE_48],
    },
    GAIA : {
        TILE_HQ :       [35,148,TILESIZE_32,TILESIZE_64],
        TILE_CITY :     [205,148,TILESIZE_32,TILESIZE_48],
        TILE_BARRACKS : [205,198,TILESIZE_32,TILESIZE_48],
    }
}


# Destruction animations
LAND_UNIT_DESTRUCTION =[
    [447,1370,TILESIZE_32,TILESIZE_32],
    [480,1370,TILESIZE_32,TILESIZE_32],
    [513,1370,TILESIZE_32,TILESIZE_32],
    [546,1370,TILESIZE_32,TILESIZE_32],
    [579,1370,TILESIZE_32,TILESIZE_32],
    [612,1370,TILESIZE_32,TILESIZE_32],
    [645,1370,TILESIZE_32,TILESIZE_32],
    [678,1370,TILESIZE_32,TILESIZE_32],
    [711,1370,TILESIZE_32,TILESIZE_32],
]


# Keyboards sprites

ESC_K           = 1
ENTER_K         = 2
ARROW_UP_K      = 3
ARROW_DOWN_K    = 4
ARROW_LEFT_K    = 5
ARROW_RIGHT_K   = 6
MOUSE_K         = 7

ESC_K           = [37,1,22,14]
ENTER_K         = [95,17,32,15]
ARROW_UP_K      = [0,0,16,16]
ARROW_DOWN_K    = [16,0,16,16]
ARROW_LEFT_K    = [32,0,16,16]
ARROW_RIGHT_K   = [48,0,16,16]
MOUSE_K         = [310,349,157,231]

