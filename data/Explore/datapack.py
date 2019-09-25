"""
File: datapack.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

from Explore.Base import Base

class Data_Pack(Base):
    """Docstring for Data_Pack. """
    # Class Attributes
    dct = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        Base.__init__(self)
        self._replay = replay

    def construct_dct(self):
        """TODO: Docstring for get_unique.
        """
        abilities = [*self._replay.datapack.abilities.values()]
        units = [*self._replay.datapack.units.values()]
        objects = abilities + units
        self.dct_object(self.__class__.dct, objects)
