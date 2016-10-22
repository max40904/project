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
k_filter = input_stack * 4
training_iters = 540002
seed = 23

openfile = 520000

Data = DataCenter.MongoDB("Gamedata")
Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 

judge = Referee.referee()


print "please choose  1. train data   2.restore from save   3.regression  "
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
                print "Correct:",count, "\t\tPosition:",i, "\t\taccuracy",count/i 

    if check =="2":
        time = 0
        game.show_game(np.reshape(set,[225,1]))
        ai = AI.Ai(Cnn,input_stack,0.5)
        while True:
            print "Your turn"
            print "Please input : "

            choose  =raw_input()
            step = game.ConvertToNum(choose)

            set = game.StepGame(step, set, 1)
            judge.input(set,step)
            before_eight = judge.Before_Eight()
            if time ==0:
                ai.firststep(set, 1, before_eight,step)
                time = 1
            else :
                ai.OppentChoose(set,1,before_eight,step)


            x_8_24_stack =np.reshape(game.ReturnAllInfo_before(set,0.5,before_eight),[1,15,15,input_stack])
            y_8_stack = np.reshape(set,[1,225])

            #print game.Return_Sort(np.reshape(y_prob,[225]),225)
            test =  ai.ReturnSet_Result(set,0.5,before_eight)

            y_estimate = ai.ReturnMonteCarlorun(set, 0.5,before_eight)
            judge.input(set,y_estimate)
            set =game.StepGame(y_estimate, set, 0.5)
            print "who win color ",test
            game.show_game_set(y_estimate)
            game.show_game(np.reshape(set,[225,1]))
            game.show_game_pos(y_estimate)

    if check =="3":
        ai = AI.Ai(Cnn,input_stack,1)
        set[7][7] = 1
        game.show_game(np.reshape(set,[225,1]))
        step = 7*15+7
        judge.input(set,step)
        before_eight = judge.Before_Eight()
        time = 0
        while True:
            print "Your turn"
            print "Please input :"
            choose = raw_input()
            step = game.ConvertToNum(choose)
            set = game.StepGame(step, set, 0.5)
            judge.input(set,step)
            before_eight = judge.Before_Eight()
            if time ==0:
                ai.firststep(set, 0.5, before_eight,step)
                time = 1
            else :
                ai.OppentChoose(set,0.5,before_eight,step)
            x_8_56_stack = np.reshape(game.ReturnAllInfo_before(set,1,before_eight),[1,15,15,input_stack])
            y_8_stack = np.reshape(set,[1,225])
            y_prob =  Cnn.Return_softmax(x_8_56_stack,y_8_stack)
            y_estimate = ai.ReturnMonteCarlorun(set, 1,before_eight)
            judge.input(set,y_estimate)
            set = game.StepGame(y_estimate, set, 1)
            game.show_game_set(y_estimate)
            game.show_game(np.reshape(set,[225,1]))
            game.show_game_pos(y_estimate)









elif choose =='3':
    judge = Referee.referee()
    Cnn.restore("./Neural_network_save/save_net"+str(openfile)+".ckpt")
    ai = AI.Ai(Cnn,input_stack,0.5)
    
    for i in range(12000*3+1):

        cur_set = Data.SGFReturnSet_Win_three()
        cut_color = Data.ReturnColor()
        before_eight = Data.SGFReturnBefore()
        allstep = Data.ReturnBeforeStep()



        result =  ai.ReturnSet_Result(cur_set,cut_color,before_eight)
        print i,"result: ",result
        empty_Set = [[0 for i in range(15)] for j in range(15)]
        for i in range(len(allstep)):
            judge.pure_input(empty_Set,allstep[i])
        judge.Set_Win(result)
        judge.writefile("./value_record/",str(i))





    





elif choose =='4':
    print '4'


