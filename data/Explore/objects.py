"""
File: objects.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

from Explore.Base import Base

class Objects(Base):
    """Docstring for Objects. """
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
        objects = self._replay.objects.values()
        self.dct_object(self.__class__.dct, objects)
        
