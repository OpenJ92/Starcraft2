"""
File: active_units.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

from Explore.Base import Base

class Active_Units(Base):
    """Docstring for Active_Units. """
    # Class Attributes
    dct = {}
    unq_dct = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        Base.__init__(self)
        self._replay = replay

    def construct_dct(self):
        """TODO: Docstring for get_unique.
        """
        objects = self._replay.active_units.values()
        self.dct_object(self.__class__.dct, objects)
        self.unq_dct_(self.__class__.dct, self.__class__.unq_dct)


