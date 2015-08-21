#!/usr/bin/env python

import os
from cmt.components import SatZoneDarcyLayers
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_satzone_darcy_layers.cfg')

def test_irf():
    component = SatZoneDarcyLayers()
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()
