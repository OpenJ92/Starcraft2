"""
File: unit.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Unit(object):

    """Docstring for Unit. """

    def __init__(self, _id, str_id, name, title, race, minerals, vespene, supply, is_building, is_worker, is_army):
        """TODO: to be defined.

        :_id: TODO
        :str_id: TODO
        :name: TODO
        :title: TODO
        :race: TODO
        :minerals: TODO
        :vespene: TODO
        :supply: TODO
        :is_building: TODO
        :is_worker: TODO
        :is_army: TODO

        """
        self.__id = _id
        self._str_id = str_id
        self._name = name
        self._title = title
        self._race = race
        self._minerals = minerals
        self._vespene = vespene
        self._supply = supply
        self._is_building = is_building
        self._is_worker = is_worker
        self._is_army = is_army
        
