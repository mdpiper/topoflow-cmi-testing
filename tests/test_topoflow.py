# Nosetests for the TopoFlow SnowDegreeDay component.

import os
import shutil
from nose.tools import assert_is_not_none, assert_equals
from cmt.components import TopoFlow as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_topoflow.cfg')
print example_dir
var_name = 'channel_water_x-section__domain_max_of_volume_flow_rate'


def setup_module():
    global component
    component = Component()


def teardown_module():
    pass


def test_irf():
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()

def test_get_component_name():
    x = component.get_component_name()
    assert_equals(x, 'TopoFlow_Driver')

def test_get_start_time():
    x = component.get_start_time()
    assert_equals(x, 0.0)

def test_get_end_time():
    x = component.get_end_time()
    assert_equals(x, 30000.0)

def test_get_var_type():
    x = component.get_var_type(var_name)
    assert_equals(x, 'float64')

def test_get_var_units():
    x = component.get_var_units(var_name)
    assert_equals(x, 'm3 s-1')

def test_get_var_itemsize():
    x = component.get_var_itemsize(var_name)
    assert_equals(x, 8)

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
