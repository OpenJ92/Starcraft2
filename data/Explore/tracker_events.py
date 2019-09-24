"""
File: tracker_events.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description:
"""

class Tracker_Events(object):

    """Docstring for Tracker_Events. """

    # Class Attributes
    dct = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        self._replay = replay
        
    def get_unique(self):
        """TODO: Docstring for get_unique.
        :returns: TODO
        """

        objects = self._replay.tracker_events

        for data in objects:
            if data.name not in self.__class__.dct.keys():
                self.__class__.dct[data.name] = {key: type(data) for key, data in vars(data).items()}
