"""
File: explore.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""
from os import listdir
from random import sample

from sc2reader import load_replay

from Explore.objects import Objects
from Explore.events import Events
from Explore.datapack import Data_Pack
from Explore.active_units import Active_Units
from Explore.tracker_events import Tracker_Events

class Explore(object):

    """Docstring for Explore. """

    def __init__(self, directory, method, samples=25, load_level=4):
        """TODO: to be defined.
        :directory: TODO
        :samples: TODO
        :load_level: TODO
        """
        self._directory = directory
        self._method = method
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

if __name__ == "__main__":
    path = "3.10.0.49716" 
    path_ = "3.11.0.51149" 
    replay = load_replay(f"{path}/{listdir(path)[8]}", load_level=4)
    AU = Active_Units(replay)
    DPack = Data_Pack(replay)
    E = Events(replay)
    O = Objects(replay)
    TE = Tracker_Events(replay)
