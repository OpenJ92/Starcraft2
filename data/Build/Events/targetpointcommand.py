"""
File: targetpointcommand.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class TargetPointCommand(object):

    """Docstring for TargetPointCommand. """

    def __init__(self, pid, player, frame, second, is_local, name, flags, flag, has_ability, ability_link, command_index, ability_data, ability_id, ability, ability_name, ability_type, ability_type_data, other_unit_id, other_unit, x, y, z, location):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :flags: TODO
        :flag: TODO
        :has_ability: TODO
        :ability_link: TODO
        :command_index: TODO
        :ability_data: TODO
        :ability_id: TODO
        :ability: TODO
        :ability_name: TODO
        :ability_type: TODO
        :ability_type_data: TODO
        :other_unit_id: TODO
        :other_unit: TODO
        :x: TODO
        :y: TODO
        :z: TODO
        :location: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._flags = flags
        self._flag = flag
        self._has_ability = has_ability
        self._ability_link = ability_link
        self._command_index = command_index
        self._ability_data = ability_data
        self._ability_id = ability_id
        self._ability = ability
        self._ability_name = ability_name
        self._ability_type = ability_type
        self._ability_type_data = ability_type_data
        self._other_unit_id = other_unit_id
        self._other_unit = other_unit
        self._x = x
        self._y = y
        self._z = z
        self._location = location
        

