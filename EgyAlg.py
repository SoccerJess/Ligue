from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator.settings import * 
from Toolbox import *
import math


## Ma Strategie d'attaque
class MyAttackStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma Strategie d'attaque")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_prediction())    
        return my_state.shoot(my_state.position_but_adv())

## Ma Strategie de defense
class MyDefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma Strategie de defense")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if(my_state.distanceMonBut()<=GAME_WIDTH/3.2):
            if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):   
                return my_state.aller(my_state.ball_prediction())
            else:
                return my_state.shoot(my_state.position_but_adv())
        else:
            return my_state.get_position_def()
                   
## Ma Strategie de dribble
class DribblerStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Ma strategie de dribble")
    def compute_strategy(self, state, id_team, id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_prediction())
        else:
            if(my_state.distanceAuButAdv()>GAME_WIDTH/3.2):
                return my_state.mini_shoot(my_state.position_but_adv())
            else:
                return my_state.shoot(my_state.position_but_adv())

class IntelligentStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Strategie Intelligente")
    def compute_strategy(self, state, id_team, id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if(my_state.distanceAuButAdv()>GAME_WIDTH/2):
            if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
                return my_state.laisse()
            else:
                return my_state.mini_shoot(my_state.position_but_adv())
        else:    
            if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
                return my_state.laisse()
            else:
                if(my_state.distanceAuButAdv()>GAME_WIDTH/3.2):
                    return my_state.passe() + my_state.trace()    
                else:
                    return my_state.shoot(my_state.position_but_adv())
                                           
    
## Creation d'une equipe
team1 = SoccerTeam(name="EGY",login="")
team2 = SoccerTeam(name="ALG",login="")
team1.add("Salah",MyAttackStrategy())
team1.add("Warda",MyDefenseStrategy())
team1.add("Trezeguet",IntelligentStrategy())
team1.add("Kahraba",IntelligentStrategy())  
team2.add("Mahrez",IntelligentStrategy())
team2.add("Brahimi",IntelligentStrategy())
team2.add("Mandi",MyDefenseStrategy()) 
team2.add("Soudani",MyAttackStrategy()) 