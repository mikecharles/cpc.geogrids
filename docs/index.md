Geospatial Grids (GeoGrids)
===========================

What is a GeoGrid?
------------------

The purpose of this package is to create and manipulate GeoGrid objects. A GeoGrid object stores
information about a geospatial grid, such as the resolution, lat/lon values of each grid point, etc.

What do I need a GeoGrid for?
-----------------------------

GeoGrids make it easier to work with geospatial data in Python. While there are many [existing geospatial Python packages](https://github.com/SpatialPython/spatial_python/blob/master/packages.md), I wanted to make a very simple one that would allow me to work with the same grids across different applications. Here at CPC, and many other places, we use the same set of grids everywhere (1-degree global, 0.5-degree global, etc.). Why not define that grid once and be done with it?

GeoGrids are utilized by several other CPC packages, including the [GeoPlot](/cpc.geoplot) package.

How do I create a GeoGrid?
--------------------------

GeoGrids can be created in one of 2 ways, by name (referencing one of several built-in GeoGrids), or by creating a custom GeoGrid.

### Using a built-in grid

Built-in grids include:

- 1deg-global
- 2deg-global
- 2.5deg-global
- 2deg-conus
- 1/6th-deg-global
- 0.5-deg-global-center-aligned
- 0.5deg-global-edge-aligned

For a list of all built-in GeoGrids, call the `list_builtin_geogrids()` function:

```python
from cpc.geogrids.definition import list_builtin_geogrids
print(list_builtin_geogrids())
```

You can create a GeoGrid using a built-in definition like this:

```python
from cpc.geogrids.definition import GeoGrid
grid = GeoGrid('1deg-global')
print(grid)
```

### Creating a custom grid

You can create a custom grid by passing the following arguments when instantiating the GeoGrid:

- `ll_corner` - lower-left corner of the grid, formatted as (lat, lon)
- `ur_corner` - upper-right corner of the grid, formatted as (lat, lon)
- `res` - resolution of the grid (in km if `type="even"`, in degrees if `type="latlon"`)
- `type` - grid type ('latlon' [default] or 'equal')

For example:

```python
from cpc.geogrids.definition import GeoGrid
grid = GeoGrid(ll_corner=(20, 30), ur_corner=(60, 90), res=2)
```

How do I manipulate data on GeoGrids?
-------------------------------------

The `cpc.geogrids` packages comes with several functions to manipulate data residing on GeoGrids, such as interpolating between GeoGrids, smoothing GeoGrids, and filling in data points near the border of a mask (eg. coastal values). These functions are documented below.

### Interpolating data

The `interpolate()` function can interpolate an array of data from one GeoGrid to another.

    interpolate(orig_data, orig_grid, new_grid)

    Interpolates data from one GeoGrid to another.

    Parameters
    ----------

    - orig_data - *array_like* - array of original data
    - orig_grid - *GeoGrid* - original GeoGrid
    - new_grid - *GeoGrid* - new GeoGrid

    Returns
    -------

    - new_data - *array_like* - a data array on the desired GeoGrid.

    Examples
    --------

    Interpolate gridded temperature obs from 2 degrees (CONUS) to 1 degree global

```python
#!/usr/bin/env python
>>> # Import packages
>>> import numpy as np
>>> from cpc.geogrids.definition import GeoGrid
>>> from cpc.geogrids.manipulation import interpolate
>>> # Create original and new GeoGrids
>>> orig_grid = GeoGrid('1deg-global')
>>> new_grid = GeoGrid('2deg-global')
>>> # Generate random data on the original GeoGrid
>>> A = np.random.rand(orig_grid.num_y, orig_grid.num_x)
>>> # Interpolate data to the new GeoGrid
>>> B = interpolate(A, orig_grid, new_grid)
>>> # Print shapes of data before and after
>>> print(A.shape)
(181, 360)
>>> print(B.shape)
(91, 180)
```