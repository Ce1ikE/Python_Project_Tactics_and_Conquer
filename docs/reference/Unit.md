# Unit

Represent a combat unit with movement, attack, and capture logic.

## Public methods

### ```__init__(self, unitData, x, y, team, unitID)```



### ```drawUnit(self, x_offset, y_offset, window_ui, unitDetailsSprites_Numbers, unitDetailsSprites_Captures)```



### ```capture(self)```



### ```attack(self, defender_unit, tile_type)```



### ```travel(self, x, y)```



### ```die(self)```



### ```showTravelZone(self, x_offset, y_offset, window_ui, zoneCoord)```



### ```getTravelZone(self, map)```



### ```showAttackZone(self, x_offset, y_offset, window_ui, zoneCoord)```



### ```getAttackZone(self, players)```



### ```showUnitsDetails(self, window_ui, time_delta)```


