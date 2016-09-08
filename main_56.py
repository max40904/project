# View more python tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial
from cnn import Policy
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np
import Referee
import AI

learning_rate = 0.003 / 2
input_stack = 56
step_save = 10000
step_draw = 100
step_check_crossenropy = 100
k_filter = input_stack * 2
training_iters = 540002
seed = 23

openfile = 510000

Data = DataCenter.MongoDB()
Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 

judge = Referee.referee()


print "please choose  1. train data   2.restore from save   3.restore and train data     "
choose = raw_input()
if choose =='1':
    Cnn.initialize()
    for i in range(training_iters):
        print i
        x = Data.SGFReturnSet()
        y = Data.SGFReturnAnw()
        cut_color = Data.ReturnColor()
        before_eight = Data.SGFReturnBefore()
        x_8_56_stack = game.ReturnAllLayer_before (x, cut_color,before_eight)
        y_8_stack = game.Return_Eight_Layer (y )

        Cnn.train(x_8_56_stack, y_8_stack)
        if i %step_check_crossenropy ==0:
            a= Cnn.Return_cross_entropy(x_8_56_stack,y_8_stack)
            print a
        if i%step_draw ==0:
            Cnn.draw(x_8_56_stack,y_8_stack,i)
        if i%step_save ==0:
            Cnn.savedata("./Neural_network_save/save_net"+str(i)+".ckpt")


elif choose =='2':
    set = [[0 for i in range(15)] for j in range(15)]
    print "what file do you want to restore?"
    restore_loc = raw_input()
    Cnn.restore("./Neural_network_save/save_net"+str(openfile)+".ckpt")
    print "Please input 1. Test accuracy         2.Player Black     3. Player White "
    check = raw_input()
    if check =="1":
        count = 0.
        for i in range(training_iters):
            x = Data.SGFReturnSet()
            y = Data.SGFReturnAnw()
            cut_color = Data.ReturnColor()
            before_eight = Data.SGFReturnBefore()

            x_8_24_stack = np.reshape(game.ReturnAllInfo_before (x, cut_color,before_eight),[1,15,15,input_stack])
            
            y_8_stack = np.reshape(y,[1,225])
            y_estimate = Cnn.Return_prediction(x_8_24_stack,y_8_stack)
            nownum =np.matrix(np.reshape(y,[225]))
            if nownum.argmax()==y_estimate:
                count = count + 1
            if i%10000 ==1:
                print count,  count/i

    if check =="2":
        game.show_game(np.reshape(set,[225,1]))
        ai = AI.Ai(Cnn,input_stack,1)
        while True:
            print "Your turn"
            print "Please input : "

            choose  =raw_input()
            step = game.ConvertToNum(choose)

            game.StepGame(step, set, 1)
            judge.input(set,step)
            before_eight = judge.Before_Eight()
            x_8_24_stack =np.reshape(game.ReturnAllInfo_before(set,0.5,before_eight),[1,15,15,input_stack])
            y_8_stack = np.reshape(set,[1,225])

            y_prob = Cnn.Return_softmax( x_8_24_stack, y_8_stack )
            #print game.Return_Sort(np.reshape(y_prob,[225]),225)
            y_estimate = ai.ReturnAIAnw_beforeeight(set, 0.5,before_eight)
            judge.input(set,y_estimate)
            game.StepGame(y_estimate, set, 0.5)
            game.show_game_set(y_estimate)
            game.show_game(np.reshape(set,[225,1]))
            game.show_game_pos(y_estimate)

    if check =="3":
        ai = AI.Ai(Cnn,input_stack,0.5)
        set[7][7] = 1
        game.show_game(np.reshape(set,[225,1]))
        step = 7*15+7
        judge.input(set,step)
        before_eight = judge.Before_Eight()
        while True:
            print "Your turn"
            print "Please input :"
            choose = raw_input()
            step = game.ConvertToNum(choose)
            game.StepGame(step,set,0.5)
            judge.input(set,step)
            before_eight = judge.Before_Eight()
            x_8_56_stack = np.reshape(game.ReturnAllInfo_before(set,1,before_eight),[1,15,15,input_stack])
            y_8_stack = np.reshape(set,[1,225])
            y_prob =  Cnn.Return_softmax(x_8_56_stack,y_8_stack)
            y_estimate = ai.ReturnAIAnw_beforeeight(set, 1,before_eight)
            judge.input(set,y_estimate)
            game.StepGame(y_estimate, set, 1)
            game.show_game_set(y_estimate)
            game.show_game(np.reshape(set,[225,1]))
            game.show_game_pos(y_estimate)









elif choose =='3':
    Cnn.restore("./Neural_network_save/save_net39.ckpt")




elif choose =='4':
    print '4'


