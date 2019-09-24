"""
File: datapack.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Data_Pack():
    """Docstring for Data_Pack. """
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
        abilities = [*self._replay.datapack.abilities.values()]
        units = [*self._replay.datapack.units.values()]
        objects = abilities + units
        for data in objects:
            if data.name not in self.__class__.dct.keys():
                self.__class__.dct[data.name] = vars(data)

