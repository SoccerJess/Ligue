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
import random
import math

#Toolbox

class Position(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
#    def alea(self):
#        self.x = 0
#        self.aux = 0
#        self.y = 0
#        self.const = 1
#        if (self.aux == 0) and (self.const == 1):
#            self.x = Vector2D.create_random(50, 70)
#            self.aux = self.x
#            self.y = self.aux
#            print(self.y)
#        return self.y
            
    def ball_position(self):
        return self.state.ball.position
        
    def ball_position_future(self):
        return self.ball_position() + self.state.ball.vitesse * 10
        
    def ball_position_x(self):
        return self.state.ball.position.x
        
    def ball_position_y(self):
        return self.state.ball.position.y
        
    def but_adv(self):
        if (self.id_team == 1):
            return Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
        else:
            return Vector2D(0, settings.GAME_HEIGHT/2)
            
#    def can_shoot(self):
#            return self.state.player_state(self.id_team, self.id_player).can_shoot
            
#    def est_dans_la_zone(self, p):
#        return p > 125 and p < 135 and p > 5 and p < 15

    def est_au_milieu(self, p):
        return p > 25 and p < 125
                         
    def est_en_attaque(self, p):
        if (self.id_team == 1):
            return p >= 125
        else:
            return p < 25
        
    def est_en_defense(self, p):
        if (self.id_team == 1):
            return p <= 25
        else:
            return p >= 125            
 
    def mon_but(self):        
        if (self.id_team == 2):
            return Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
        else:
            return Vector2D(0, settings.GAME_HEIGHT/2)
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
        
    def my_position_x(self):
        return self.state.player_state(self.id_team, self.id_player).position.x
        
    def my_position_y(self):
        return self.state.player_state(self.id_team, self.id_player).position.y
        
    def position_coop(self):
        if (self.id_team == 1):
            if (self.id_player == 0):
                return self.state.player_state(1,1).position
            if (self.id_player == 1):
                return self.state.player_state(1,0).position
        if (self.id_team == 2):
            if (self.id_player == 0):
                return self.state.player_state(2,1).position
            if (self.id_team == 1):
                return self.state.player_state(2,0).position
                
    def position_coop_x(self):
       if (self.id_team == 1):
           if (self.id_player == 0):
                return self.state.player_state(1,1).position.x
           if (self.id_player == 1):
            return self.state.player_state(1,0).position.x
       if (self.id_team == 2):
            if (self.id_player == 0):
                return self.state.player_state(2,1).position.x
            if (self.id_team == 1):
                return self.state.player_state(2,0).position.x
                
    def position_coop_y(self):
        if (self.id_team == 1):
            if (self.id_player == 0):
                return self.state.player_state(1,1).position.y
            if (self.id_player == 1):
                return self.state.player_state(1,0).position.y
        if (self.id_team == 2):
            if (self.id_player == 0):
                return self.state.player_state(2,1).position.y
            if (self.id_team == 1):
                return self.state.player_state(2,0).position.y
    
    def zone_tir(self):
        return settings.PLAYER_RADIUS + settings.BALL_RADIUS
        
    def zone_hauteGauche(self):
        return Vector2D(10, 75)
        
    def zone_hauteDroite(self):
        return Vector2D(130, 75)
        
    def zone_basseGauche(self):
        return Vector2D(10, 10)
    
    def zone_basseDroite(self):
        return Vector2D(130, 10)
        
#    def position_adv(self):
#        if (self.id_team == 1):
#            return self.state.player_state(self.id_team, self.id_player).position
#        else:
#            return self.state.player_state(2, self.id_player).position
        
###############################################################################
        
class Deplacement(Position):
    def aller(self, p):
        return SoccerAction(p-self.my_position(), Vector2D())
    
#    def ralentir (self):
#        settings.maxPlayerAcceleration = 0.2
#        if (self.but_adv() - self.my_position()).norm <= 50 and (self.ball_position() - self.my_position()).norm <= 10:
#            settings.maxPlayerAcceleration = 0.05
#            return self.aller(self.ball_position())
#        else:
#            return SoccerAction(Vector2D(), Vector2D())
        
###############################################################################
        
class ActionOffensive(Deplacement):
        def dribble(self, p):
            return SoccerAction(Vector2D(), 0.015 * (p-self.my_position()))
            
        def dribbler(self):
            return self.dribble(self.but_adv())
 
        def passe(self):
            if (self.ball_position() - self.my_position()).norm <= self.zone_tir() and self.est_en_attaque(self.position_coop_x()):
                return self.perfect_shoot(self.position_coop())
            elif (self.ball_position() - self.my_position()).norm <= self.zone_tir():
                return self.aller(self.ball_position()) + self.dribble(self.zone_hauteDroite())
            else: 
                return self.aller(self.ball_position())
                    
        def perfect_shoot(self, p):
            return SoccerAction(Vector2D(), 0.1 * (p-self.my_position()))
        
#        def shoot(self, p):
#            return SoccerAction(Vector2D(), p-self.my_position())

###############################################################################

class ActionDefensive(Deplacement):          
    def dribble(self, p):
            return SoccerAction(Vector2D(), 0.015 * (p-self.my_position()))
            
    def garder_balle(self):
        if ((self.ball_position()-self.my_position()).norm <= self.zone_tir()):
            return self.dribble(self.zone_hauteGauche())
        else:
            return self.aller(self.ball_position())
    
    def shoot(self, p):
            return SoccerAction(Vector2D(), p-self.my_position())
        