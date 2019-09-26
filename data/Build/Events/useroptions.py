"""
File: useroptions.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class UserOptions(object):

    """Docstring for UserOptions. """

    def __init__(self, pid, player, frame, second, is_local, name, game_fully_downloaded, development_cheats_enabled, multiplayer_cheats_enabled, sync_checksumming_enabled, is_map_to_map_transition, use_ai_beacons, starting_rally, debug_pause_enabled, base_build_num):
        """TODO: to be defined.

        :pid: TODO
        :player: TODO
        :frame: TODO
        :second: TODO
        :is_local: TODO
        :name: TODO
        :game_fully_downloaded: TODO
        :development_cheats_enabled: TODO
        :multiplayer_cheats_enabled: TODO
        :sync_checksumming_enabled: TODO
        :is_map_to_map_transition: TODO
        :use_ai_beacons: TODO
        :starting_rally: TODO
        :debug_pause_enabled: TODO
        :base_build_num: TODO

        """
        self._pid = pid
        self._player = player
        self._frame = frame
        self._second = second
        self._is_local = is_local
        self._name = name
        self._game_fully_downloaded = game_fully_downloaded
        self._development_cheats_enabled = development_cheats_enabled
        self._multiplayer_cheats_enabled = multiplayer_cheats_enabled
        self._sync_checksumming_enabled = sync_checksumming_enabled
        self._is_map_to_map_transition = is_map_to_map_transition
        self._use_ai_beacons = use_ai_beacons
        self._starting_rally = starting_rally
        self._debug_pause_enabled = debug_pause_enabled
        self._base_build_num = base_build_num
        

