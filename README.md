Geospatial Grids (GeoGrids)
===========================

[![Build Status](https://travis-ci.org/noaa-nws-cpc/cpc.geogrids.svg?branch=master)](https://travis-ci.org/noaa-nws-cpc/cpc.geogrids)

What is a GeoGrid?
------------------

The purpose of this package is to create and manipulate GeoGrid objects. A GeoGrid object stores
information about a geospatial grid, such as the resolution, lat/lon values of each grid point, etc.

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
