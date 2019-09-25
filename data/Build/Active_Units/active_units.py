"""
File: active_units.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Active_Units(object):

    """Docstring for Active_Units. """

    def __init__(self, owner, started_at, finished_at, died_at, killed_by, killing_player, killing_unit, killed_units, _id, _type_class, type_history, hallucinated, flags, location):
        """TODO: to be defined.

        :owner: TODO
        :started_at: TODO
        :finished_at: TODO
        :died_at: TODO
        :killed_by: TODO
        :killing_player: TODO
        :killing_unit: TODO
        :killed_units: TODO
        :id: TODO
        :_type_class: TODO
        :type_history: TODO
        :hallucinated: TODO
        :flags: TODO
        :location: TODO

        """
        self._owner = owner
        self._started_at = started_at
        self._finished_at = finished_at
        self._died_at = died_at
        self._killed_by = killed_by
        self._killing_player = killing_player
        self._killing_unit = killing_unit
        self._killed_units = killed_units
        self._id = _id
        self._type_class = _type_class
        self._type_history = type_history
        self._hallucinated = hallucinated
        self._flags = flags
        self._location = location
        

