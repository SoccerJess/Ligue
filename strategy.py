# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:43:56 2017

@author: 3415756
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math
from toolbox import *

class AttaqueStrategy_1v1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):        
        me = ActionOffensive(state, id_team, id_player)
        if me.zone_tir() and me.est_au_milieu(me.ball_position_x()):
            return me.dribble(me.but_adv())
        if me.zone_tir() and me.est_en_attaque(me.my_position_x()):
            return me.perfect_shoot(me.but_adv())
        return me.aller(me.ball_position())

class AttaqueStrategy_2v2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):        
        me = ActionOffensive(state, id_team, id_player)
        if me.zone_tir():
            return me.perfect_shoot(me.but_adv())
        elif (me.est_en_attaque(me.ball_position_x())):
            return me.aller(me.ball_position_future())
        else:
            return me.aller(me.ball_position_future())
    
#Stategie de defense
class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        me = ActionDefensive(state, id_team, id_player)
        return me.garder_balle() + me.ralentir()
        
#Strategie de passe
class PasseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        me = ActionOffensive(state, id_team, id_player)
        if me.zone_tir() and me.est_en_attaque(me.position_coop_x()):
            return me.passe()
        elif me.zone_tir():
            return me.dribble(me.but_adv())
        elif me.est_en_attaque(me.ball_position_x()):
            return me.aller(Vector2D(75, 45))
        else:
            return me.aller(me.ball_position_future())
        if me.zone_tir() and me.est_en_attaque(me.ball_position_x()):
            return me.perfect_shoot(me.but_adv())