from MongoDB import DataCenter 
from gameinfo import policy_analysis
from gameinfo import game
from cnn import Policy
import numpy as np
import time
import Referee
import AI
import math

print math.sqrt(10)
learning_rate = 0.003 / 2
input_stack = 56
step_save = 10000
step_draw = 100
step_check_crossenropy = 100
k_filter = input_stack * 4
training_iters = 540002
seed = 23
class node:
	def __init__(self):
		self.list = []
		self.num = 0
Data = DataCenter.MongoDB("Gamedata")
Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 
ai = AI.Ai(Cnn,input_stack,1)
set_x = Data.SGFReturnSet()

set_x[7][7]= 0
set_x[6][11]= 1
set_x[7][12]= 1
set_x[8][13]= 1

set_x[7][7]= 0
set_x[1][8]= 0.5
set_x[2][7]= 0.5
set_x[3][6]= 0.5



print Data.ReturnBeforeStep()
game.show_game(np.reshape(set_x,[225]))
game.show_game(np.reshape(policy_analysis.evaluate_five(set_x,1),[225]))
game.show_game(np.reshape(policy_analysis.evaluate_defense_four(set_x,0.5,1),[225]))
game.show_game(np.reshape(policy_analysis.evaluate_defense_four(set_x,1,1),[225]))