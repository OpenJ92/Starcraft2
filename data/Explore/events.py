"""
File: events.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Events(object):
    """Docstring for Events. """
    # Class Attributes
    dct = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        self._replay = replay

    def get_unique(self):
        """TODO: Docstring for get_unique.
        """
        events = self._replay.events
        for data in events:
            if data.name not in self.__class__.dct.keys():
                self.__class__.dct[data.name] = vars(data)

