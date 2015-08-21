#!/usr/bin/env python

import os
from cmt.components import ChannelsKinWave as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_channels_kinematic_wave.cfg')


def test_irf():
    component = Component()
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()
