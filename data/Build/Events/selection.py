"""
File: selection.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Selection(object):

    """Docstring for Selection. """

    def __init__(self, pid, player, frame, second, is_local, name, control_group, bank, subgroup_index, mask_type, mask_data, new_unit_types, new_unit_ids, new_unit_info, new_units, objects):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :control_group: TODO
        :bank: TODO
        :subgroup_index: TODO
        :mask_type: TODO
        :mask_data: TODO
        :new_unit_types: TODO
        :new_unit_ids: TODO
        :new_unit_info: TODO
        :new_units: TODO
        :objects: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._control_group = control_group
        self._bank = bank
        self._subgroup_index = subgroup_index
        self._mask_type = mask_type
        self._mask_data = mask_data
        self._new_unit_types = new_unit_types
        self._new_unit_ids = new_unit_ids
        self._new_unit_info = new_unit_info
        self._new_units = new_units
        self._objects = objects
        

