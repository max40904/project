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

set_x[7][7]= 1
set_x[7][8]= 1
set_x[7][9]= 1
set_x[7][10]= 0.5



set_x[8][6]= 1
set_x[9][6]= 1
set_x[10][6]= 1
set_x[11][6]= 0.5


# set_x[4][6]= 1
# set_x[5][6]= 1
# set_x[8][6]= 1
# set_x[9][6]= 0.5



# set_x[4][2]= 1
# set_x[5][2]= 1
# set_x[8][2]= 1
# set_x[9][2]= 0.5



# set_x[6][14]= 1
# set_x[7][14]= 1
# set_x[8][14]= 1
# set_x[9][14]= 0.5


set_x[4][13]= 1
set_x[7][13]= 1
set_x[8][13]= 1


# set_x[4][1]= 1
# set_x[7][1]= 1
# set_x[8][1]= 1
# set_x[9][1]= 0.5

# set_x[5][3]= 1
# set_x[7][3]= 1
# set_x[8][3]= 1




print Data.ReturnBeforeStep()
game.show_game(np.reshape(set_x,[225]))
game.show_game(np.reshape(policy_analysis.evaluate_dead_four(set_x,1,1),[225]))
game.show_game(np.reshape(policy_analysis.evaluate_dead_four(set_x,1,2),[225]))
game.show_game(np.reshape(policy_analysis.evaluate_alive_three_dead_four(set_x,1),[225]))
game.show_game(np.reshape(policy_analysis.evaluate_defense_four(set_x,1,1),[225]))
