# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:21:26 2017

@author: 3415756
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#Toolbox

class Position(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    def mon_but(self):        
        return Vector2D(0, settings.GAME_HEIGHT/2)
    
    def but_adv(self):
        return Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    def ball_position(self):
        return self.state.ball.position
        
    def ball_position_x(self):
        return self.state.ball.position.x
        
    def ball_position_y(self):
        return self.state.ball.position.y
    
    def zone_tir(self):
        return settings.PLAYER_RADIUS + settings.BALL_RADIUS
        
###############################################################################
        
class Deplacement(Position):
    def aller(self, p):
        return SoccerAction(p-self.my_position(), Vector2D())
    
    def ralentir(self, p):
        if (p-self.my_position() <= 10):
            return self.aller(self.ball_position())
        
###############################################################################
        
class ActionOffensive(Deplacement):
        def shoot(self, p):
            return SoccerAction(Vector2D(), p-self.my_position())
            
        def dribble(self, p):
            return SoccerAction(Vector2D(), 0.1 * p-self.my_position())
            
        def dribbler(self):
            if (self.id_team == 1):
                if ((self.ball_position()-self.my_position()).norm <= self.zone_tir()) and self.ball_position_x() > 110:
                    return self.shoot(self.but_adv())            
                elif ((self.ball_position()-self.my_position()).norm <= self.zone_tir()):       
                    return self.aller(self.ball_position()) + self.dribble(self.but_adv())
                else:
                    return self.aller(self.ball_position())
            else: 
                if ((self.ball_position()-self.my_position()).norm <= self.zone_tir()) and self.ball_position_x() < 50:
                    return self.shoot(self.but_adv())
                elif ((self.ball_position()-self.my_position()).norm <= self.zone_tir()):       
                    return self.aller(self.state.ball_position()) + self.dribble(self.but_adv())
                else:
                    return self.aller(self.ball_position())