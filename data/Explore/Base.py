"""
File: Base.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description:    
"""

from collections import OrderedDict

class Base(object):

    """Docstring for Base. """

    def __init__(self):
        """TODO: to be defined. """
        pass

    def dct_object(self, dct, objects):
        """TODO: Docstring for dct_object.
        :dct: TODO
        :objects: TODO
        :returns: TODO
        """
        for data_ in objects:
            if data_.name not in dct.keys():
                dct_temp = {}
                for key, data in vars(data_).items():
                    if isinstance(data, OrderedDict):
                        dct_temp[key] = {i:j for i, j  in data.items()}
                    elif isinstance(data, dict):
                        dct_temp[key] = {i:j for i, j  in data.items()}
                    elif isinstance(data, list):
                        dct_temp[key] = [sub for sub in data]
                    else:
                        dct_temp[key] = data
                dct_temp["object"] = data_
                dct[data_.name] = dct_temp

    def unq_dct_(self, dct, unq_dct_):
        """TODO: Docstring for unq_dct.
        :dct: TODO
        :returns: TODO
        """
        for data_ in dct.values():
            if data_.keys() not in unq_dct_.values():
                unq_dct_[data_['object'].__class__] = data_.keys()
