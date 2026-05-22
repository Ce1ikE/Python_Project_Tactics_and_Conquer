# Map

Store the rendered world surface and visible terrain metadata.

## Public methods

### ```__init__(self)```



### ```createMapSurface(self, image, x, y)```

Copy a rendered tile into the cached world surface.

### ```drawHUDMap(self, x_offset, y_offset, ui_window)```

Draw the map with a contrast overlay for HUD states.

### ```drawMap(self, x_offset, y_offset, ui_window)```

Draw the visible world slice without the HUD overlay.
