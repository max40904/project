from MongoDB import DataCenter 
from gameinfo import policy_analysis
from gameinfo import game
import numpy as np
import time
import Referee
judge = Referee.referee()
str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + ".sgf"
print str
Data = DataCenter.MongoDB()
set_x = Data.SGFReturnSet()
set_y = Data.SGFReturnAnw()
set_x[7][6] =  1
set_x[7][5] =  1

set_x[7][4] =  1

game.show_game(np.reshape(set_x,[225]))
game.show_game(np.reshape(policy_analysis.evaluate_five(set_x,1),[225]))
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