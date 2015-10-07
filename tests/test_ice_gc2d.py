#!/usr/bin/env python
# Nosetests for the TopoFlow GC2D component.

import os
import shutil
from nose.tools import assert_is_not_none, assert_equals, assert_almost_equal
from cmt.components import GC2D as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_ice_valley_glacier.cfg')
var_name = 'glacier_ice__thickness'


def setup_module():
    global component
    component = Component()


def teardown_module():
    pass


def test_irf():
    component.initialize(cfg_file)
    component.update(1.0)  # years
    component.finalize()


def test_get_component_name():
    x = component.get_component_name()
    assert_equals(x, 'TopoFlow_Ice_GC2D_Valley_Glacier')


def test_get_start_time():
    x = component.get_start_time()
    assert_equals(x, 0.0)


def test_get_end_time():
    x = component.get_end_time()
    assert_almost_equal(x, 4.0004)


def test_get_var_type():
    x = component.get_var_type(var_name)
    assert_equals(x, 'float32')


def test_get_var_units():
    x = component.get_var_units(var_name)
    assert_equals(x, 'm')


def test_get_var_itemsize():
    x = component.get_var_itemsize(var_name)
    assert_equals(x, 4)


# The get_var_nbytes method isn't implemented in TopoFlow.
# def test_get_var_nbytes():
#     x = component.get_var_nbytes(var_name)


def test_get_value():
    x = component.get_value(var_name)
    assert_is_not_none(x)


def test_get_var_grid():
    x = component.get_var_grid(var_name)
    assert_equals(x, 0)


def test_get_grid_type():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_type(grid_id)
    assert_equals(x, 'uniform')


def test_get_grid_rank():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_rank(grid_id)
    assert_equals(x, 2)


def test_get_grid_shape():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_shape(grid_id)
    assert_equals(x[0], 44)
    assert_equals(x[1], 29)


def test_get_grid_size():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_size(grid_id)
    assert_equals(x, 44*29)


def test_get_grid_spacing():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_spacing(grid_id)
    assert_equals(x[0], 30.0)
    assert_equals(x[1], 30.0)


def test_get_grid_origin():
    grid_id = component.get_var_grid(var_name)
    x = component.get_grid_origin(grid_id)
    assert_equals(x[0], 4560090.42)
    assert_equals(x[1], 277850.358)
