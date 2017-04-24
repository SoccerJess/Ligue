# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:57:50 2017

@author: 3415756
"""

from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from golf import Golfeur
from toolbox import *

def get_golf_team():
    team1 = SoccerTeam()
    team1.add("John",Golfeur())
    return team1

def get_slalom_team1():
    team1 = SoccerTeam()
    team1.add("John",Golfeur())
    return team1