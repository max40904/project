# View more python tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial
from cnn import Local_Policy
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np


learning_rate = 0.0003
input_stack = 49
step_save = 1000
step_draw = 1000
step_check_crossenropy = 500
k_filter = input_stack * 2 
training_iters = 1600001
seed = 13



Data = DataCenter.MongoDB()
LocalCnn =  Local_Policy.LocalPolicy(learning_rate, input_stack, k_filter,seed) 
print "1. train 2. restoredata    3.restore data and then train"
choose = raw_input()
if choose =='1':
	LocalCnn.initialize()
	count = 0
	for i in range(training_iters ):
	    x = Data.SGFReturnSet()
	    y = Data.SGFReturnAnw()
	    cut_color = Data.ReturnColor()
	    all_set_nine = game.Retrun_fif_to_nine_set( x, y ) 
	    all_anw_nine = game.Retrun_fif_to_nine_anw( x, y )
	    print i
	    for j in range(len(all_set_nine)):
	    	input = game.ReturnAllLayer_nine(all_set_nine[j],cut_color)
	    	y_real = game.Return_Eight_anw_nine(all_anw_nine[j],cut_color)
	    	LocalCnn.train(input,y_real)
	    	
	    	LocalCnn.draw(input,y_real,count)
	    	result = LocalCnn.Return_cross_entropy(input,y_real)
	    	print result
	    	count = count +1
	    if i %step_save ==0:
	    	LocalCnn.savedata("Loc_Neural_network_save/save_net"+str(i)+".ckpt")
if choose =='2':
	LocalCnn.restore("./Loc_Neural_network_save/save_net411000.ckpt")
	for i in range(200000 ):
		x = Data.SGFReturnSet()
		y = Data.SGFReturnAnw()
	for i in range(200000 ):
		x = Data.SGFReturnSet()
		y = Data.SGFReturnAnw()
		game.show_game(np.reshape(x,[225,1]))
		game.show_game(np.reshape(y,[225,1]))

		cut_color = Data.ReturnColor()
		check = game.ReturnSelectField(x , 0)
		prob = [[0.0 for i in range(15)] for j in range(15)]
		for i in range(15):
			for j in range(15):
				if check[i][j] == 1 :
					input = game.ReturnAllInfo_nine(game.ReturnFif_to_Nine(x,i,j), cut_color)
					output = [[0 for sss in range(3)] for jjjj in range(1)]
					if cut_color == 1:
						prob[i][j] = LocalCnn.Return_prediction_prob_black(np.reshape(input,[1,9,9,25]), output)

					if cut_color == 0.5:
						prob[i][j] = LocalCnn.Return_prediction_prob_black(np.reshape(input,[1,9,9,25]), output)
		prob_flat = np.reshape(prob,[225])
		test = game.Return_Biggest_Five_Loc(prob_flat)
		test2 = game.Return_Biggest_Five_Prob(prob_flat)
		print test
		print test2
		game.Show_Biggest_Five_Loc(prob_flat)
		ss = np.argmax(np.reshape(prob,[225]))
		game.show_game_set(ss)
		game.show_game_pos(ss)

		a = raw_input()
if choose =='3':
	LocalCnn.restore("./Loc_Neural_network_save/save_net411000.ckpt")
	print "where you want to start?"
	aaa = raw_input()
	time = int(aaa)
	count = time * 60
	for j in range(time):
		x = Data.SGFReturnSet()


	for i in range(time ,time + training_iters):
	    x = Data.SGFReturnSet()
	    y = Data.SGFReturnAnw()
	    cut_color = Data.ReturnColor()
	    all_set_nine = game.Retrun_fif_to_nine_set( x, y ) 
	    all_anw_nine = game.Retrun_fif_to_nine_anw( x, y )
	    print i
	    for j in range(len(all_set_nine)):
	    	input = game.ReturnAllLayer_nine(all_set_nine[j],cut_color)
	    	y_real = game.Return_Eight_anw_nine(all_anw_nine[j],cut_color)
	    	LocalCnn.train(input,y_real)
	    	
	    	
	    	if count %step_draw ==0:
	    		LocalCnn.draw(input,y_real,count)
	    	if count %step_check_crossenropy ==0:
	    		result = LocalCnn.Return_cross_entropy(input,y_real)
	    		print result
	    	count = count +1
	    if i %step_save ==0:
	    	LocalCnn.savedata("Loc_Neural_network_save/save_net"+str(i)+".ckpt")


		




	 		






# print "please choose  1. train data   2.restore from save   3.restore and train data     "
# choose = raw_input()
# if choose =='1':
#     Cnn.initialize()
#     for i in range(training_iters):
#         x = Data.SGFReturnSet()
#         y = Data.SGFReturnAnw()
#         cut_color = Data.ReturnColor()
#         x_8_24_stack = game.ReturnAllLayer (x, cut_color)
#         y_8_stack = game.Return_Eight_Layer (y )
#         print i
#         Cnn.train(x_8_24_stack, y_8_stack)
#         if i %step_check_crossenropy ==0:
#             a= Cnn.Return_cross_entropy(x_8_24_stack,y_8_stack)
#             print a
#         if i%step_draw ==0:
#             Cnn.draw(x_8_24_stack,y_8_stack,i)
#         if i%step_save ==0:
#             Cnn.savedata("./Neural_network_save/save_net"+str(i)+".ckpt")


# elif choose =='2':
#     set = [[0 for i in range(15)] for j in range(15)]
#     print "what file do you want to restore?"
#     restore_loc = raw_input()
#     Cnn.restore("./Neural_network_save/save_net400000.ckpt")
#     print "Please input 1. Test accuracy         2.Player Black     3. Player White "
#     check = raw_input()
#     if check =="1":
#         count = 0.
#         for i in range(training_iters):
#             x = Data.SGFReturnSet()
#             y = Data.SGFReturnAnw()
#             cut_color = Data.ReturnColor()
#             x_8_24_stack = np.reshape(game.ReturnAllInfo (x, cut_color),[1,15,15,24])
#             y_8_stack = np.reshape(y,[1,225])
#             y_estimate = Cnn.Return_prediction(x_8_24_stack,y_8_stack)
#             nownum =np.matrix(np.reshape(y,[225]))
#             if nownum.argmax()==y_estimate:
#                 count = count + 1
#             if i%10000 ==0:
#                 print count,  count/training_iters

#     if check =="2":
#         game.show_game(np.reshape(set,[225,1]))
#         while True:
#             print "Your turn"
#             print "Please input : "

#             choose  =raw_input()
#             step = game.ConvertToNum(choose)
#             game.StepGame(step, set, 1)
#             x_8_24_stack =np.reshape(game.ReturnAllInfo(set,0.5),[1,15,15,24])
#             y_8_stack = np.reshape(set,[1,225])
#             y_estimate = Cnn.Return_prediction(x_8_24_stack,y_8_stack)
#             game.StepGame(y_estimate, set, 0.5)
#             game.show_game_set(y_estimate)
#             game.show_game(np.reshape(set,[225,1]))
#             game.show_game_pos(y_estimate)

#     if check =="3":
#         set[7][7] = 1
#         loc = raw_input()
#         step  = game.ConvertToNum(loc)
#         game.StepGame(step, set, 0.5)
#         y = set
#         x = set
#         x_8__stack = np.reshape(game.ReturnAllInfo (set, 1),[1,15,15,24])
#         y_stack = np.reshape(y,[1,225])
#         y_estimate = Cnn.Return_prediction(x_8__stack,y_stack) 
#         game.StepGame(y_estimate, set, 1)
#         show_game_set(y_estimate)
#         game.show_game(np.reshape(set,[225,1]))
#         game.show_game_pos(y_estimate)







# elif choose =='3':
#     Cnn.restore("./Neural_network_save/save_net39.ckpt")




# elif choose =='4':
#     print '4'


# # for i in range(training_iters):
# #     print i
# #     x = Data.SGFReturnSet()
# #     y = Data.SGFReturnAnw()
# #     cut_color = Data.ReturnColor()
# #     x_8_24_stack = np.reshape(game.ReturnAllInfo (x, cut_color),[1,15,15,24])
# #     y_8_stack = np.reshape(y,[1,225]) 
# #     y_estimate = Cnn.prediction(x_8_24_stack,y_8_stack)
# #     game.show_game(np.reshape(x,[225,1]))
# #     game.show_game(np.reshape(y,[225,1]))
# #     game.show_game_set(y_estimate)
# #     a = raw_input()