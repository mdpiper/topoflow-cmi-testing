"""Tests for running TopoFlow components in CMI."""
import os


def locate_topoflow(cache_dir):
    for x in os.listdir(cache_dir):
        if x.startswith('topoflow'):
            return x


root_dir = '/home/csdms/wmt/topoflow.1'
cache_dir = os.path.join(root_dir, 'cache')
topoflow_dir = locate_topoflow(cache_dir)
example_dir = os.path.join(cache_dir, topoflow_dir,
                           'topoflow', 'examples', 'Treynor_Iowa')
