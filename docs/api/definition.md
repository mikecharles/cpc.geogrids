---
layout: default
title: cpc.geogrids.definition module
type: apidoc
---
        
# cpc.geogrids.definition Module
> Defines a GeoGrid object. Grid objects store certain properties of a gridded dataset (lat/lon grid
> corners, resolution, etc.), and can simplify defining a grid when calling utilities such as
> interpolation routines, plotting, etc.



## Data
- `builtin_geogrids = {'2deg-conus': {'ll_...` 

## Functions

### <span class="function">list_builtin_geogrids()</span> 



## cpc.geogrids.definition.Geogrid Objects



### <span class="function">\__init__(self, name=None, ll_corner=None, ur_corner=None, res=None, type='latlon')</span> 



### <span class="function">\__repr__(self)</span> 



### <span class="function">data_fits(self, data)</span> 

> Determines if the specified data fits this Geogrid
> 
> #### Parameters
> 
> - data - *array_like* - data to verify
> 
> #### Returns
> 
> - *boolean* - whether the data fits this Geogrid
> 
> #### Exceptions
> 
> - *GeogridError* - raised if data is not a valid NumPy array
> 
> #### Examples
> 
>     >>> import numpy as np
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> data = np.random.random((grid.num_y, grid.num_x))
>     >>> data.shape
>     (181, 360)
>     >>> grid.data_fits(data)
>     True
>     >>> data = np.random.random((grid.num_y + 1, grid.num_x + 1))
>     >>> data.shape
>     (182, 361)
>     >>> grid.data_fits(data)
>     False



### <span class="function">latlon_to_1d_index(self, latlons)</span> 

> Returns the 1-dimensional index of the grid point, from this Geogrid, that is located at
> the specified lat/lon position
> 
> For example, you may have a 1-dimensional data array on a `1deg-global` Geogrid, and you
> want to know the index corresponding to 50 deg lat, -80 deg lon.
> 
> #### Parameters
> 
> - latlons - *tuple of floats* or *list of tuples of floats* - lat/lon of grid point(s)
> 
> #### Returns
> 
> - *int* or *None* - array index containing the given gridpoint(s) index(es), or -1 if no gridpoint matches the
> given lat/lon value
> 
> #### Examples
> 
> Get the index of a 1deg-global grid at 50 deg lat, -80 deg lon
> 
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> grid.latlon_to_1d_index((50, -80))
>     [50820]
> 
> Get the index of 1deg-global grid at several lat/lon points
> 
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> grid.latlon_to_1d_index([(0, 0), (20, 40), (50, -80)])
>     [90, 7350, 50820]



## cpc.geogrids.definition.Grid Objects



### <span class="function">\__init__(self, name=None, ll_corner=None, ur_corner=None, res=None, type='latlon')</span> 



### <span class="function">\__repr__(self)</span> 



### <span class="function">data_fits(self, data)</span> 

> Determines if the specified data fits this Geogrid
> 
> #### Parameters
> 
> - data - *array_like* - data to verify
> 
> #### Returns
> 
> - *boolean* - whether the data fits this Geogrid
> 
> #### Exceptions
> 
> - *GeogridError* - raised if data is not a valid NumPy array
> 
> #### Examples
> 
>     >>> import numpy as np
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> data = np.random.random((grid.num_y, grid.num_x))
>     >>> data.shape
>     (181, 360)
>     >>> grid.data_fits(data)
>     True
>     >>> data = np.random.random((grid.num_y + 1, grid.num_x + 1))
>     >>> data.shape
>     (182, 361)
>     >>> grid.data_fits(data)
>     False



### <span class="function">latlon_to_1d_index(self, latlons)</span> 

> Returns the 1-dimensional index of the grid point, from this Geogrid, that is located at
> the specified lat/lon position
> 
> For example, you may have a 1-dimensional data array on a `1deg-global` Geogrid, and you
> want to know the index corresponding to 50 deg lat, -80 deg lon.
> 
> #### Parameters
> 
> - latlons - *tuple of floats* or *list of tuples of floats* - lat/lon of grid point(s)
> 
> #### Returns
> 
> - *int* or *None* - array index containing the given gridpoint(s) index(es), or -1 if no gridpoint matches the
> given lat/lon value
> 
> #### Examples
> 
> Get the index of a 1deg-global grid at 50 deg lat, -80 deg lon
> 
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> grid.latlon_to_1d_index((50, -80))
>     [50820]
> 
> Get the index of 1deg-global grid at several lat/lon points
> 
>     >>> from cpc.geogrids import Geogrid
>     >>> grid = Geogrid('1deg-global')
>     >>> grid.latlon_to_1d_index([(0, 0), (20, 40), (50, -80)])
>     [90, 7350, 50820]


