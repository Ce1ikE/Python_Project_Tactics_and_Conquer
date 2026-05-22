# Cursor

Track and draw the active cursor for map navigation.

## Public methods

### ```__init__(self, x, y)```



### ```drawCursor(self, ui_window)```

Draw the regular cursor animation.

### ```drawAttackCursor(self, ui_window)```

Draw the attack cursor animation.

### ```setPosition(self, camera_x, camera_y, coordinates, keyPress)```

Move the cursor one step through a linear coordinate list.

### ```cyclePosition(self, camera_x, camera_y, coordinates, keyPress)```

Jump the cursor to the next coordinate matching a direction key.

### ```UpdatePosition(self, camera_x, camera_y, keyPress)```


