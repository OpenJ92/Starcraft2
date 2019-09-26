"""
File: ability.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class Ability(object):

    """Docstring for Ability. """

    def __init__(self, id_, name, title, is_build, build_time, build_unit):
        """TODO: to be defined.

        :id_: TODO
        :name: TODO
        :title: TODO
        :is_build: TODO
        :build_time: TODO
        :build_unit: TODO

        """
        self._id_ = id_
        self._name = name
        self._title = title
        self._is_build = is_build
        self._build_time = build_time
        self._build_unit = build_unit
        
