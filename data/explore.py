"""
File: explore.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""
from os import listdir
from random import sample

import sc2reader
from sc2reader import load_replay
from sc2reader.engine.plugins import APMTracker, SelectionTracker
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(SelectionTracker())

from Explore.objects import Objects
from Explore.events import Events
from Explore.datapack import Data_Pack
from Explore.active_units import Active_Units
from Explore.tracker_events import Tracker_Events

class Explore(object):

    """Docstring for Explore. """

    def __init__(self, directory, cls, samples=25, load_level=4):
        """TODO: to be defined.
        :directory: TODO
        :samples: TODO
        :load_level: TODO
        """
        self._directory = directory
        self._cls = cls
        self._samples = samples
        self._load_level = load_level
        self._replays = self._load_replays()

    def _load_replays(self):
        """load in replay objects for use with ./Explore/*.py
        :returns: TODO
        """
        replays = []
        files_ = sample(listdir(self._directory), self._samples)
        for file_ in files_:
            replay = load_replay(f"{self._directory}/{file_}", load_level=self._load_level)
            replays.append(replay)
        return replays

    def exp_cls(self):
        """TODO: Docstring for exp_cls.
        :returns: TODO
        """
        for replay in self._replays:
            self._cls(replay).construct_dct()

if __name__ == "__main__":
    from re import match
    import os

    dirs = [dir_ for dir_ in os.listdir() if match(r"(\d+\.){3}\d+", dir_)]
    
    Oexplore = Explore(dirs[-1], Objects, samples=1)
    Eexplore = Explore(dirs[-1], Events, samples=1)
    Dexplore = Explore(dirs[-1], Data_Pack, samples=1)
    Aexplore = Explore(dirs[-1], Active_Units, samples=1)
    TEexplore = Explore(dirs[-1], Tracker_Events, samples=1)
