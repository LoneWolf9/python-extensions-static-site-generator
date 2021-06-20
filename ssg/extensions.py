import importlib, sys

from pathlib import Path

def load_module(self, directory, name):
    sys.path.insert(0, directory)
    