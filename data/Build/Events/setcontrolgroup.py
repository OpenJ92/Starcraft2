"""
File: setcontrolgroup.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class SetControlGroup(object):

    """Docstring for SetControlGroup. """

    def __init__(self, pid, player, frame, second, is_local, name, control_group, bank, hotkey, update_type, mask_type, mask_data):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :control_group: TODO
        :bank: TODO
        :hotkey: TODO
        :update_type: TODO
        :mask_type: TODO
        :mask_data: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._control_group = control_group
        self._bank = bank
        self._hotkey = hotkey
        self._update_type = update_type
        self._mask_type = mask_type
        self._mask_data = mask_data
        
