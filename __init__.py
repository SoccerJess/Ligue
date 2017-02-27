# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:57:50 2017

@author: 3415756
"""

from toolbox import *
from soccersimulator import Player,SoccerTeam
from strategy import AttaqueStrategy_1v1, AttaqueStrategy_2v2, DefenseStrategy, PasseStrategy

def get_team(i):
    s = SoccerTeam(name = "EDF")
    if i == 1:
        s.add("Bakambu", AttaqueStrategy_1v1())
    if i == 2:
        s.add("Giroud", AttaqueStrategy_2v2())
        s.add("Perrin", PasseStrategy())
    if i == 4:
        s.add("Carl", AttaqueStrategy())
        s.add("Cabaye", AttaqueStrategy())
        s.add("Doria", DefenseStrategy())
        s.add("Jallet", DefenseStrategy())
    return s