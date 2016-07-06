"""
Defines a GeoGrid object. Grid objects store certain properties of a gridded dataset (lat/lon grid
corners, resolution, etc.), and can simplify defining a grid when calling utilities such as
interpolation routines, plotting, etc.
"""


# Built-ins
import reprlib

# Third-party
import numpy as np

# This package
from cpc.geogrids.exceptions import GeoGridError


# Create reprlib
r = reprlib.Repr()
r.maxlist = 4  # max elements displayed for lists
r.maxstring = 50  # max characters displayed for strings

# Create dict of all built-in GeoGrids
builtin_geogrids = {
    '1deg-global': {
        'll_corner': (-90, 0),
        'ur_corner': (90, 359),
        'res': 1,
        'type': 'latlon'
    },
    '2deg-global': {
        'll_corner': (-90, 0),
        'ur_corner': (90, 358),
        'res': 2,
        'type': 'latlon'
    },
    '2.5deg-global': {
        'll_corner': (-90, 0),
        'ur_corner': (90, 357.5),
        'res': 2.5,
        'type': 'latlon'
    },
    '2deg-conus': {
        'll_corner': (20, 230),
        'ur_corner': (56, 300),
        'res': 2,
        'type': 'latlon'
    },
    '1/6th-deg-global': {
        'll_corner': (-89.9167, 0.0833),
        'ur_corner': (89.9167, 359.9167),
        'res': 1/6,
        'type': 'latlon'
    },
    '0.5-deg-global-center-aligned': {
        'll_corner': (-89.75, 0.25),
        'ur_corner': (89.75, 359.75),
        'res': 0.5,
        'type': 'latlon'
    },
    '0.5-deg-global-edge-aligned': {
        'll_corner': (-90, 0),
        'ur_corner': (90, 359.5),
        'res': 0.5,
        'type': 'latlon'
    },
}


def list_builtin_geogrids():
    return list(builtin_geogrids.keys())


class GeoGrid:
    """
    GeoGrid object storing attributes of a geo grid.

    A GeoGrid object can either be created by providing the name of the grid, or by providing the
    other attributes listed below

    Attributes
    ----------

    - name (String)
        - Name of the grid
    - ll_corner (tuple of floats)
        - Lower-left corner of the grid, formatted as (lat, lon)
    - ur_corner (tuple of floats)
        - Upper-right corner of the grid, formatted as (lat, lon)
    - res (float)
        - Resolution of the grid (in km if `type="even"`, in degrees if `type="latlon"`)
    - type (str)
        - Grid type. Possible values are:
            - latlon (Latlon grid)
            - equal (Equally-spaced square grid)
    """

    def __init__(self, name=None, ll_corner=None, ur_corner=None, res=None, type='latlon'):

        # ------------------------------------------------------------------------------------------
        # Document attributes
        #
        self.name = None
        '''Grid name'''
        self.ll_corner = ll_corner
        '''Lower-left corner of grid (lon, lat)'''
        self.ur_corner = ur_corner
        '''Upper-right corner of grid (lon, lat)'''
        self.res = res
        '''Grid resolution'''
        self.type = type
        '''Grid type (currently only latlon is supported)'''

        # ------------------------------------------------------------------------------------------
        # Create the GeoGrid
        #
        # Built-in
        if name in builtin_geogrids:
            self.name = name
            self.ll_corner = builtin_geogrids[name]['ll_corner']
            self.ur_corner = builtin_geogrids[name]['ur_corner']
            self.res = builtin_geogrids[name]['res']
            self.type = builtin_geogrids[name]['type']
        # Custom
        else:
            # User didn't provide everything necessary to create a custom GeoGrid
            if not all([self.ll_corner, self.ur_corner, self.res]):
                raise GeoGridError('You must either supply the name of a built-in Grid, or an '
                                   'll_corner, ur_corner, and res to create a custom Grid')
            # Create a custom GeoGrid
            else:
                self.name = 'custom'
                self.ll_corner = ll_corner
                self.ur_corner = ur_corner
                self.res = res
                self.type = type

        # ------------------------------------------------------------------------------------------
        # Calculate additional attributes
        #
        self.num_y = int(((self.ur_corner[0] - self.ll_corner[0]) / self.res) + 1)
        '''Number of points in the y-direction'''
        self.num_x = int(((self.ur_corner[1] - self.ll_corner[1]) / self.res) + 1)
        '''Number of points in the x-direction'''
        self.lats = np.arange(self.ll_corner[0], self.ur_corner[0] + 0.00000001, self.res).tolist()
        '''List of latitude values at which grid points are found'''
        self.lons = np.arange(self.ll_corner[1], self.ur_corner[1] + 0.00000001, self.res).tolist()
        '''List of longitude values at which grid points are found'''

    def __repr__(self):
        details = ''
        for key, val in sorted(vars(self).items()):
            details += eval(r.repr('- {}: {}\n'.format(key, val)))
        return 'GeoGrid:\n{}'.format(details)

Grid = GeoGrid

if __name__ == '__main__':
    from cpc.geogrids.definition import GeoGrid

    grid = GeoGrid(ll_corner=(20, 30), ur_corner=(60, 90), res=2)

    print(grid)
