# Cell

Track one tile candidate during wave-function-collapse generation.

## Public methods

### ```__init__(self, tile_options, x, y)```



### ```collapse(self)```

Collapse the cell to one weighted random tile option.

### ```add_neighbours(self, neighbours)```

Attach neighbouring cells used during propagation.

### ```reduce_options(self, neighbours_allowed, direction)```

Remove options that violate the allowed neighbour edges.

### ```is_collapsed(self)```

Return True when the cell has exactly one option left.
