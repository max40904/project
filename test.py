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
for i in range(5):
	set_x = Data.SGFReturnSet_End()


	print Data.ReturnBeforeStep()
	game.show_game(np.reshape(set_x,[225]))
	game.show_game(np.reshape(policy_analysis.evaluate_five(set_x,1),[225]))
	game.show_game(np.reshape(policy_analysis.evaluate_defense_four(set_x,1,1),[225]))

	

# judge = Referee.referee()
# str = tim
# e.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + ".sgf"
# print str
# Data = DataCenter.MongoDB()
# for i in range(10000):
# 	set_x = Data.SGFReturnSet_Win_three()
# 	print Data.ReturnWin()
# 	set_x = Data.SGFReturnSet_Win_three()
# 	print Data.ReturnWin()
# 	set_x = Data.SGFReturnSet_Win_three()
# 	print Data.ReturnWin()

# 	set_y = Data.SGFReturnAnw()



# game.show_game(np.reshape(set_x,[225]))
# game.show_game(np.reshape(policy_analysis.evaluate_five(set_x,1),[225]))
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()
# set_x = Data.SGFReturnSet()

# set_x = Data.SGFReturnSet()





# all_layer = game.ReturnAllInfo(set_x,1)
# game.show_all_info_game(all_layer,24)
# print "   \n\n\n"
# print set_x[1][1]
# out_y = Data.SGFReturnAnw()
# x = [0 for i in range(225)]
# x[0]=0.5
# x[2+14]= 1
# x[4+14+14+14 +2]=1
# x[5+14+1+14+14+14 +2]=1
# # x[6+14+14+1+1+14]=1

# y = np.reshape(x,[225,1])
# game.show_game(y)
# y = np.reshape(symmetric.evaluate_alive_four(np.reshape(x,[15,15]),1),[225,1])

# game.show_game(y)