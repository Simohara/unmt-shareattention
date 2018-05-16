from collections import namedtuple
import json


def load_config(path):
    """Loads the configuration.

    Args:
        path: Path to configuration file.
    """
    to_tuple = lambda d: namedtuple('X', d.keys())(*d.values())
    with open(path, 'r') as f:
        config = json.loads(f.read(), object_hook=to_tuple)
    return config

if __name__ == '__main__':
    pass