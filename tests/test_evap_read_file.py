#!/usr/bin/env python

import os
from cmt.components import EvapReadFile as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_evap_read_file.cfg')


# Fails because June_20_67_2D-ETrate-in.nc is missing
def test_irf():
    component = Component()
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()
