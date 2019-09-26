"""
File: chat.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Chat(object):

    """Docstring for Chat. """

    def __init__(self, pid, frame, second, name, target, text, to_all, to_allies, to_observers, player):
        """TODO: to be defined.

        :pid: TODO
        :frame: TODO
        :second: TODO
        :name: TODO
        :target: TODO
        :text: TODO
        :to_all: TODO
        :to_allies: TODO
        :to_observers: TODO
        :player: TODO

        """
        self._pid = pid
        self._frame = frame
        self._second = second
        self._name = name
        self._target = target
        self._text = text
        self._to_all = to_all
        self._to_allies = to_allies
        self._to_observers = to_observers
        self._player = player
        

