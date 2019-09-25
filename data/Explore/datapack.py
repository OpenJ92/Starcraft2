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
    units = {}
    abilities = {}
    unq_dct_U = {}
    unq_dct_A = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        Base.__init__(self)
        self._replay = replay

    def construct_dct(self):
        """TODO: Docstring for get_unique.
        """
        units = [*self._replay.datapack.units.values()]
        abilities = [*self._replay.datapack.abilities.values()]
        objects = abilities + units

        self.dct_object(self.__class__.units, units)
        self.dct_object(self.__class__.abilities, abilities)

        self.unq_dct_(self.__class__.units, self.__class__.unq_dct_U)
        self.unq_dct_(self.__class__.abilities, self.__class__.unq_dct_A)
