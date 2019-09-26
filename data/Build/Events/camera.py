"""
File: camera.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Camera(object):

    """Docstring for Camera. """

    def __init__(self, pid, player, frame, second, is_local, name, x, y, location, distance, pitch, yaw):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :x: TODO
        :y: TODO
        :location: TODO
        :distance: TODO
        :pitch: TODO
        :yaw: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._x = x
        self._y = y
        self._location = location
        self._distance = distance
        self._pitch = pitch
        self._yaw = yaw
        

