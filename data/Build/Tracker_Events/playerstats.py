"""
File: playerstats.py
Author: Jacob Vartuli-Schonberg
Email: jacob.vartuli.schonberg@gmail.com
Github: https://github.com/OpenJ92
Description: 
"""

class PlayerStats(object):

    """Docstring for PlayerStats. """

    def __init__(self, frame, second, name, pid, player, stats, minerals_current, vespene_current, minerals_collection_rate, vespene_collection_rate, workers_active_count, minerals_used_in_progress_army, minerals_used_in_progress_economy, minerals_used_in_progress_technology, minerals_used_in_progress, vespene_used_in_progress_army, vespene_used_in_progress_economy, vespene_used_in_progress_technology, vespene_used_in_progress, resources_used_in_progress, minerals_used_current_army, minerals_used_current_economy, minerals_used_current_technology, minerals_used_current, vespene_used_current_army, vespene_used_current_economy, vespene_used_current_technology, vespene_used_current, resources_used_current, minerals_lost_army, minerals_lost_economy, minerals_lost_technology, minerals_lost, vespene_lost_army, vespene_lost_economy, vespene_lost_technology, vespene_lost, resources_lost, minerals_killed_army, minerals_killed_economy, minerals_killed_technology, minerals_killed, vespene_killed_army, vespene_killed_economy, vespene_killed_technology, vespene_killed, resources_killed, food_used, food_made, minerals_used_active_forces, vespene_used_active_forces, ff_minerals_lost_army, ff_minerals_lost_economy, ff_minerals_lost_technology, ff_vespene_lost_army, ff_vespene_lost_economy, ff_vespene_lost_technology):
        """TODO: to be defined.

        :frame: TODO
        :second: TODO
        :name: TODO
        :pid: TODO
        :player: TODO
        :stats: TODO
        :minerals_current: TODO
        :vespene_current: TODO
        :minerals_collection_rate: TODO
        :vespene_collection_rate: TODO
        :workers_active_count: TODO
        :minerals_used_in_progress_army: TODO
        :minerals_used_in_progress_economy: TODO
        :minerals_used_in_progress_technology: TODO
        :minerals_used_in_progress: TODO
        :vespene_used_in_progress_army: TODO
        :vespene_used_in_progress_economy: TODO
        :vespene_used_in_progress_technology: TODO
        :vespene_used_in_progress: TODO
        :resources_used_in_progress: TODO
        :minerals_used_current_army: TODO
        :minerals_used_current_economy: TODO
        :minerals_used_current_technology: TODO
        :minerals_used_current: TODO
        :vespene_used_current_army: TODO
        :vespene_used_current_economy: TODO
        :vespene_used_current_technology: TODO
        :vespene_used_current: TODO
        :resources_used_current: TODO
        :minerals_lost_army: TODO
        :minerals_lost_economy: TODO
        :minerals_lost_technology: TODO
        :minerals_lost: TODO
        :vespene_lost_army: TODO
        :vespene_lost_economy: TODO
        :vespene_lost_technology: TODO
        :vespene_lost: TODO
        :resources_lost: TODO
        :minerals_killed_army: TODO
        :minerals_killed_economy: TODO
        :minerals_killed_technology: TODO
        :minerals_killed: TODO
        :vespene_killed_army: TODO
        :vespene_killed_economy: TODO
        :vespene_killed_technology: TODO
        :vespene_killed: TODO
        :resources_killed: TODO
        :food_used: TODO
        :food_made: TODO
        :minerals_used_active_forces: TODO
        :vespene_used_active_forces: TODO
        :ff_minerals_lost_army: TODO
        :ff_minerals_lost_economy: TODO
        :ff_minerals_lost_technology: TODO
        :ff_vespene_lost_army: TODO
        :ff_vespene_lost_economy: TODO
        :ff_vespene_lost_technology: TODO

        """
        self._frame = frame
        self._second = second
        self._name = name
        self._pid = pid
        self._player = player
        self._stats = stats
        self._minerals_current = minerals_current
        self._vespene_current = vespene_current
        self._minerals_collection_rate = minerals_collection_rate
        self._vespene_collection_rate = vespene_collection_rate
        self._workers_active_count = workers_active_count
        self._minerals_used_in_progress_army = minerals_used_in_progress_army
        self._minerals_used_in_progress_economy = minerals_used_in_progress_economy
        self._minerals_used_in_progress_technology = minerals_used_in_progress_technology
        self._minerals_used_in_progress = minerals_used_in_progress
        self._vespene_used_in_progress_army = vespene_used_in_progress_army
        self._vespene_used_in_progress_economy = vespene_used_in_progress_economy
        self._vespene_used_in_progress_technology = vespene_used_in_progress_technology
        self._vespene_used_in_progress = vespene_used_in_progress
        self._resources_used_in_progress = resources_used_in_progress
        self._minerals_used_current_army = minerals_used_current_army
        self._minerals_used_current_economy = minerals_used_current_economy
        self._minerals_used_current_technology = minerals_used_current_technology
        self._minerals_used_current = minerals_used_current
        self._vespene_used_current_army = vespene_used_current_army
        self._vespene_used_current_economy = vespene_used_current_economy
        self._vespene_used_current_technology = vespene_used_current_technology
        self._vespene_used_current = vespene_used_current
        self._resources_used_current = resources_used_current
        self._minerals_lost_army = minerals_lost_army
        self._minerals_lost_economy = minerals_lost_economy
        self._minerals_lost_technology = minerals_lost_technology
        self._minerals_lost = minerals_lost
        self._vespene_lost_army = vespene_lost_army
        self._vespene_lost_economy = vespene_lost_economy
        self._vespene_lost_technology = vespene_lost_technology
        self._vespene_lost = vespene_lost
        self._resources_lost = resources_lost
        self._minerals_killed_army = minerals_killed_army
        self._minerals_killed_economy = minerals_killed_economy
        self._minerals_killed_technology = minerals_killed_technology
        self._minerals_killed = minerals_killed
        self._vespene_killed_army = vespene_killed_army
        self._vespene_killed_economy = vespene_killed_economy
        self._vespene_killed_technology = vespene_killed_technology
        self._vespene_killed = vespene_killed
        self._resources_killed = resources_killed
        self._food_used = food_used
        self._food_made = food_made
        self._minerals_used_active_forces = minerals_used_active_forces
        self._vespene_used_active_forces = vespene_used_active_forces
        self._ff_minerals_lost_army = ff_minerals_lost_army
        self._ff_minerals_lost_economy = ff_minerals_lost_economy
        self._ff_minerals_lost_technology = ff_minerals_lost_technology
        self._ff_vespene_lost_army = ff_vespene_lost_army
        self._ff_vespene_lost_economy = ff_vespene_lost_economy
        self._ff_vespene_lost_technology = ff_vespene_lost_technology
        
