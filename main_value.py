
from cnn import Value
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np
import Referee
import AI

learning_rate = 0.003
input_stack = 57
step_save = 12000
step_draw = 100
step_check_crossenropy = 100
k_filter = input_stack *3
training_iters = 12000*3 + 1
seed = 19


Data = DataCenter.MongoDB()
Cnn =  Value.ValueNetwork(learning_rate, input_stack, k_filter,seed) 
ai = AI.Ai(Cnn,input_stack)
judge = Referee.referee()


print "please choose  1. train data   2.restore from save   3.restore and train data     "
choose = raw_input()
if choose =='1':
    y = []
    Cnn.initialize()
    for i in range(training_iters):
        
        x = Data.SGFReturnSet_Win_three()
        if Data.ReturnWin()=="black":
            y= [[1 for j in range(1)]for j in range(8)]
        elif Data.ReturnWin()=="draw":
            y= [[0 for j in range(1)]for j in range(8)]
            continue
        else:
            y= [[-1 for j in range(1)]for j in range(8)]
        print i
        cut_color = Data.ReturnColor()
        before_eight = Data.SGFReturnBefore()
        x_8_56_stack = game.ReturnAllLayer_before (x, cut_color,before_eight)
        if cut_color==0.5:
            for x in range(8):
                for p in range(15):
                    for j in range(15):
                        x_8_56_stack[x][p][j].append(0)
        else:
            for x in range(8):
                for p in range(15):
                    for j in range(15):
                        x_8_56_stack[x][p][j].append(1)
        Cnn.train(x_8_56_stack, y)
        if i %step_check_crossenropy ==0:
            a= Cnn.Return_cross_entropy(x_8_56_stack,y)
            print a
        if i%step_draw ==0:
            Cnn.draw(x_8_56_stack,y,i)
        if i%step_save ==0:
            Cnn.savedata("./Value_Neural_network_save/save_net"+str(i)+".ckpt")


elif choose =='2':
    set = [[0 for i in range(15)] for j in range(15)]
    print "what file do you want to restore?"
    restore_loc = raw_input()
    Cnn.restore("./Value_Neural_network_save/save_net36000.ckpt")
    print "Please input 1. Test accuracy"
    check = raw_input()
    count_black = 0
    count_original_black = 0
    count_white = 0
    count_original_white = 0
    count_draw = 0
    count_original_draw = 0
    count_12 = 0 
    count_25 = 0 
    count_50 = 0 
    other = 0


    for i in range(training_iters):
        x = Data.SGFReturnSet_Win_three()
        wincolor = 0
        if Data.ReturnWin()=="black":
            y= [[1 for j in range(1)]for j in range(1)]
            wincolor = 1
            count_original_black = count_original_black + 1
        elif Data.ReturnWin()=="draw":
            y= [[0 for j in range(1)]for j in range(1)]
            count_original_draw = count_original_draw + 1
            wincolor = 0
        else:
            wincolor = -1
            count_original_white = count_original_white  + 1 
            y= [[-1 for j in range(1)]for j in range(1)]
        cut_color = Data.ReturnColor()
        before_eight = Data.SGFReturnBefore()
        x_8_56_stack = [game.ReturnAllInfo_before (x, cut_color,before_eight)]
        if cut_color==0.5:
            for x in range(1):
                for p in range(15):
                    for j in range(15):
                        x_8_56_stack[x][p][j].append(0)
        else:
            for x in range(1):
                for p in range(15):
                    for j in range(15):
                        x_8_56_stack[x][p][j].append(1)

        pre = Cnn.Return_prediction_prob_empty(x_8_56_stack,y)
        
        if pre <0 and wincolor < 0 :
            count_white = count_white +1 
        if pre >0 and wincolor > 0 :
            count_black = count_black + 1
        if pre >-0.125 and pre < 0.125  and wincolor == 0 :
            count_draw =  count_draw + 1
        if abs(pre - wincolor) <0.125:
            count_12 =count_12 +1
        elif abs(pre - wincolor) <0.25:
            count_25 = count_25 + 1
        elif abs(pre - wincolor) <0.5:
            count_50 =  count_50 + 1
        else:
            other = other + 1
        if i %step_save:
            print "black check",count_black," black ori  ",count_original_black
            print "white check",count_white," white ori  ",count_original_white
            print "draw check",count_draw," draw ori  ",count_original_draw
            print "other    :",other
            print "count_50 :",count_50
            print "count_25 :",count_25
            print "count_12 :",count_12

        


        

  