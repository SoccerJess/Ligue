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

class AttaqueStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):        
        me = ActionOffensive(state, id_team, id_player)
        return me.aller(me.ball_position()) + me.dribbler()
    
#Stategie de defense
class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        me = ActionDefensive(state, id_team, id_player)
        return me.garder_balle(me.my_position()) + me.ralentir()
            
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",AttaqueStrategy()) #Strategie qui ne fait rien
team2.add("Paul",DefenseStrategy())   #Strategie aleatoire