"""
File: active_units.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Active_Units():
    """Docstring for Active_Units. """
    # Class Attributes
    dct = {}
    dct_ = {}

    def __init__(self, replay):
        """TODO: to be defined.
        :replay: TODO
        """
        self._replay = replay
    
    # We need to consider how to combine the following two functions into a singular
    # dictionary whose exterior keys are "key_sets" and "type_names" with mappings to
    # the both sub dictionaryies. inside key sets, we have a unique numeric ID and a 
    # prototype dictioary with keys and value type information. Inside type_names, we have
    # keys that match the numeric ids in the previous subdictionary and a list of the objects
    # which subscribe to that form. We then seek to construct a python snippet which transforms
    # these prototypical dictionaryies into class definitions and psql class definitions.
    def get_unique(self):
        """TODO: Docstring for get_unique.
        """
        objects = self._replay.active_units.values()

        for data in objects:
            if data.name not in self.__class__.dct.keys():
                self.__class__.dct[data.name] = {key: type(data) for key, data in vars(data).items()}

    def get_unique_key_set(self):
        """TODO: Docstring for get_unique_key_set.
        """
        self.get_unique()
        unique_objects = self.__class__.dct
        for key, data in unique_objects.items():
            if data.keys() not in self.__class__.dct_:
                self.__class__.dct_[data.keys()] = key
            else:
                self.__class__.dct_[data.keys()] += key

