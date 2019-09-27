"""
File: datapack.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

import json
from os import listdir
from re import match

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
        """TODO: Docstring for construct_dct.
        """
        units = [*self._replay.datapack.units.values()]
        abilities = [*self._replay.datapack.abilities.values()]
        objects = abilities + units

        self.dct_object(self.__class__.units, units)
        self.dct_object(self.__class__.abilities, abilities)

        self.unq_dct_(self.__class__.units, self.__class__.unq_dct_U)
        self.unq_dct_(self.__class__.abilities, self.__class__.unq_dct_A)

    def construct_json(self,):
        """TODO: Docstring for construct_json.
        :returns: TODO
        """
        if not self.__class__.units and self.__class__.abilities:
            self.construct_dct()
        
        dir_ = self._replay.versions[1:-1]
        __import__('pdb').set_trace()
        if not dir_ in listdir():
            for _dir in ["Ability, Unit"]:
                #with open(f"{_dir}/{dir_}/{dir_}.json") as doc:
                #    pass
                # if this replay's version does not exists
                # in the ability or unit directory , then make
                # that directory
                pass
            pass 
