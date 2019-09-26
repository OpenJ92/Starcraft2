"""
File: playerleave.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class PlayerLeave(object):

    """Docstring for PlayerLeave. """

    def __init__(self, pid, player, frame, second, is_local, name, data):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :data: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._data = data
        
