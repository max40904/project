# View more python tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial
from cnn import Policy
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np


learning_rate = 0.0003
input_stack = 24

k_filter = 24 * 4
training_iters = 10



Data = DataCenter.MongoDB()
Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter) 

Cnn.initialize()
for i in range(training_iters):
    x = Data.SGFReturnSet()
    y = Data.SGFReturnAnw()
    cut_color = Data.ReturnColor()
    x_8_24_stack = game.ReturnAllLayer (x, cut_color)
    y_8_stack = game.Return_Eight_Layer (y )
    Cnn.train(x_8_24_stack, y_8_stack)
Cnn.savedata("./Neural_network_save/save_net39.ckpt")




for i in range(training_iters):
    print i
    x = Data.SGFReturnSet()
    y = Data.SGFReturnAnw()
    cut_color = Data.ReturnColor()
    x_8_24_stack = np.reshape(game.ReturnAllInfo (x, cut_color),[1,15,15,24])
    y_8_stack = np.reshape(y,[1,225]) 
    y_estimate = Cnn.prediction(x_8_24_stack,y_8_stack)
    game.show_game(np.reshape(x,[225,1]))
    game.show_game(np.reshape(y,[225,1]))
    game.show_game_set(y_estimate)
    a = raw_input()