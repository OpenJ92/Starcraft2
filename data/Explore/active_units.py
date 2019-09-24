"""
File: active_units.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

from collections import OrderedDict

class Active_Units():
    """Docstring for Active_Units. """
    # Class Attributes
    dct = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        self._replay = replay

    def construct_dct(self):
        """TODO: Docstring for get_unique.
        """
        objects = self._replay.active_units.values()

        for data_ in objects:
            if data_.name not in self.__class__.dct.keys():
                dct_temp = {}
                for key, data in vars(data_).items():
                    if isinstance(data, OrderedDict):
                        dct_temp[key] = {type(i):type(j) for i, j  in data.items()}
                    elif isinstance(data, dict):
                        dct_temp[key] = {type(i):type(j) for i, j  in data.items()}
                    elif isinstance(data, list):
                        dct_temp[key] = [type(sub) for sub in data]
                    else:
                        dct_temp[key] = type(data)

                self.__class__.dct[data_.name] = dct_temp
