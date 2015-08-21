import os


root_dir = '/home/csdms/wmt/topoflow.1'
cache_dir = os.path.join(root_dir, 'cache')
topoflow_cache_dir = locate_topoflow_cache_dir()
example_dir = os.path.join(cache_dir, topoflow_cache_dir,
                           'topoflow', 'examples', 'Treynor_Iowa')


def locate_topoflow_cache_dir():
    for x in os.listdir(cache_dir):
        if x.startswith('topoflow'):
            return x

