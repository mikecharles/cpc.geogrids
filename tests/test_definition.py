from pytest import raises
from cpc.geogrids.definition import list_builtin_geogrids, GeoGrid, GeoGridError
import numpy as np


def test_create_geogrid():
    """Ensure the GeoGrid object can be created"""
    for builtin_geogrid in list_builtin_geogrids():
        GeoGrid(builtin_geogrid)


def test_exception_raised_for_unsupported_grid():
    """Ensure an exception is raised for an unsupported units"""
    with raises(GeoGridError):
        GeoGrid('unsupported')


def test_exception_raised_for_no_grid_name():
    """Ensure an exception is raised for an unsupported units"""
    with raises(GeoGridError):
        GeoGrid()


def test_create_custom_geogrid():
    """Ensure a custom Grid object can be created"""
    GeoGrid(ll_corner=(0, 0), ur_corner=(90, 90), res=1)


def test_print_returns_something(capfd):
    """Ensure the print_info() functions returns a non-empty string"""
    for builtin_geogrid in list_builtin_geogrids():
        print(GeoGrid(builtin_geogrid))
        out, err = capfd.readouterr()
        assert out


def test_data_fits():
    """Tests the is_correct_grid() function"""
    # Should get False returned if the number of points is incorrect
    test_grid = GeoGrid('1deg-global')
    bad_y = test_grid.num_y - 1
    bad_x = test_grid.num_x - 1
    test_array = np.random.rand(bad_y, bad_x)
    assert test_grid.data_fits(test_array) == False
    # Should raise a GridError if the data isn't a NumPy array
    test_grid = GeoGrid('1deg-global')
    with raises(GeoGridError):
        test_grid.data_fits(1)
