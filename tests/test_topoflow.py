# Nosetests for the TopoFlow SnowDegreeDay component.

import os
import shutil
from nose.tools import assert_is_not_none, assert_equals
from cmt.components import TopoFlow as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_topoflow.cfg')
print example_dir
var_name = 'basin_outlet_water_x-section__mean_depth'


def setup_module():
    global component
    component = Component()


def teardown_module():
    pass


def test_irf():
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()


