
from __future__ import print_function
import martix
import policy_analysis
import local_policy_analysis
import numpy as np
def Return_Biggest_Five_Prob(set):
	anw = []
	s  = set.copy()
	for i in range(5):
		anw.append(s[np.argmax(s)])
		s[np.argmax(s)] = 0
	return anw
def Show_Biggest_Five_Loc(set):
	anw = []
	s = set.copy()
	for i in range(5):
		show_game_pos(np.argmax(s))
		s[np.argmax(s)] = 0
	

def Return_Biggest_Five_Loc(set):
	anw = []
	s = set.copy()
	for i in range(5):
		anw.append(np.argmax(s))
		s[np.argmax(s)] = 0
	return anw

def ReturnSelectField(set,flag):

	anw = policy_analysis.evaluate_self(set,flag)
	return anw

def show_all_info_game(set,y):
	for x in range(y):
		seq = 1
		for i in range(15):
			for j in range(15):
				if set[i][j][x] == 1:
					print ("X ",end = "")
				else:
					print (". ",end = "")
			print ("")
		print ("\n")
	print ("\n")

def show_game_prob(set):
	seq = 1
	for i in range(225):
		if i %15 ==0:
			print ("")

		print(set[i], end=" ")
		if i %15 ==14:
			print("",seq,end= "")
			seq = seq + 1
	print ("")
	for i in range(15):
		print (chr(ord('a')+i),end = "  ")

	print ("\n")


def show_game(set):
	seq = 1
	for i in range(225):
		if i %15 ==0:
			print ("")
		if set[i] == 1:
			print("X ", end="")

			
		elif set[i] ==0.5:
			print("O ", end="")

			
		else :
			print('. ', end="")
		if i %15 ==14:
			print("",seq,end= "")
			seq = seq + 1
	print ("")
	for i in range(15):
		print (chr(ord('a')+i),end = " ")

	print ("\n")

def show_game_pos(num):
	byte =  num % 15
	y =  num / 15 + 1
	x = chr(ord('a')+byte) 
	print(x,y)

def show_game_set(num):
	seq = 1
	for i in range(225):
		if i %15 ==0:
			print ("")
		if i == num:
			print ("X ",end = "")
		else :
			print('. ', end="")
		if i %15 ==14:
			print("",seq,end= "")
			seq = seq + 1
	print ("")
	for i in range(15):
		print (chr(ord('a')+i),end = " ")

	print ("\n")
	
def Return_Eight_Layer(set):
	
	left = set
	up = martix.rotate90_fif(left)
	right = martix.rotate90_fif(up)
	down =  martix.rotate90_fif(up)
	ref_left = martix.reflection_fif(set)
	ref_up = martix.rotate90_fif(ref_left)
	ref_right =  martix.rotate90_fif(ref_up)
	ref_down = martix.rotate90_fif(ref_right)

	all_layer = [np.reshape(left,[225]), np.reshape(up,[225]) , np.reshape(right,[225]), 
	np.reshape(down,[225]), np.reshape(ref_left,[225]), np.reshape(ref_up,[225]), 
	np.reshape(ref_right,[225]), np.reshape(ref_down,[225])]
	return all_layer

def ReturnAllLayer(set,color):
	s = set
	left = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)
	up = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)
	right = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)
	down = ReturnAllInfo(s,color)

	s =  martix.reflection_fif(set)
	ref_left  = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)

	ref_up = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)

	ref_right = ReturnAllInfo(s,color)
	s = martix.rotate90_fif(s)
	ref_down = ReturnAllInfo(s,color)
	all_layer = [left, up, right, down, ref_left, ref_up, ref_right, ref_down]

	return all_layer

def ReturnAllInfo(set,color):
	ocolor = 1
	if color == 1:
		ocolor = 0.5

	layer_1 = policy_analysis.evaluate_self(set,color)

	layer_2 = policy_analysis.evaluate_self(set,ocolor)

	layer_3 = policy_analysis.evaluate_self(set,0)

	layer_4 = [[1 for i in range(15)] for j in range(15)]

	# player
	layer_5 = policy_analysis.evaluate_lib_five(set,color)

	layer_6 = policy_analysis.evaluate_square_four(set,color)

	layer_7 = policy_analysis.evaluate_square_three(set,color)

	layer_8 = policy_analysis.evaluate_square_two(set,color)

	layer_9 = policy_analysis.evaluate_dead_two(set,color,1)

	layer_10 = policy_analysis.evaluate_dead_two(set,color,2)

	layer_11= policy_analysis.evaluate_dead_two(set,color,3)

	layer_12 = policy_analysis.evaluate_dead_two(set,color,4)

	layer_13 = policy_analysis.evaluate_alive_two(set,color,1)

	layer_14 = policy_analysis.evaluate_alive_two(set,color,2)

	layer_15 = policy_analysis.evaluate_alive_two(set,color,3)

	layer_16 = policy_analysis.evaluate_alive_two(set,color,4)

	layer_17 = policy_analysis.evaluate_dead_three(set,color,1)

	layer_18 = policy_analysis.evaluate_dead_three(set,color,2)
	
	
	layer_19 = policy_analysis.evaluate_alive_three(set,color,1)

	layer_20 = policy_analysis.evaluate_alive_three(set,color,2)

	layer_21 = policy_analysis.evaluate_dead_four(set,color,1)

	layer_22 = policy_analysis.evaluate_dead_four(set,color,2)

	layer_23 = policy_analysis.evaluate_alive_three_dead_four(set,color)

	layer_24 = policy_analysis.evaluate_alive_four(set,color,1)

	layer_25 = policy_analysis.evaluate_five(set,color)

	layer_26 = [[1 for i in range(15)] for j in range(15)]

	layer_27 = policy_analysis.evaluate_lib_five(set,ocolor)

	layer_28 = policy_analysis.evaluate_square_four(set,ocolor)

	layer_29 = policy_analysis.evaluate_square_three(set,ocolor)

	layer_30 = policy_analysis.evaluate_square_two(set,ocolor)

	layer_31 = policy_analysis.evaluate_dead_two(set,ocolor,1)

	layer_32 = policy_analysis.evaluate_dead_two(set,ocolor,2)

	layer_33= policy_analysis.evaluate_dead_two(set,ocolor,3)

	layer_34 = policy_analysis.evaluate_dead_two(set,ocolor,4)

	layer_35 = policy_analysis.evaluate_alive_two(set,ocolor,1)

	layer_36 = policy_analysis.evaluate_alive_two(set,ocolor,2)

	layer_37 = policy_analysis.evaluate_alive_two(set,ocolor,3)

	layer_38 = policy_analysis.evaluate_alive_two(set,ocolor,4)

	layer_39 = policy_analysis.evaluate_dead_three(set,ocolor,1)

	layer_40 = policy_analysis.evaluate_dead_three(set,ocolor,2)
	
	
	layer_41 = policy_analysis.evaluate_alive_three(set,ocolor,1)

	layer_42 = policy_analysis.evaluate_alive_three(set,ocolor,2)

	layer_43 = policy_analysis.evaluate_dead_four(set,ocolor,1)

	layer_44 = policy_analysis.evaluate_dead_four(set,ocolor,2)
	
	layer_45 = policy_analysis.evaluate_alive_three_dead_four(set,ocolor)

	layer_46 = policy_analysis.evaluate_alive_four(set,ocolor,1)

	layer_47 = policy_analysis.evaluate_five(set,ocolor)

	layer_48 = [[0 for i in range(15)] for j in range(15)]




	all_layer = [[[0 for i in range(28)] for j in range(15)] for x in range(15)]

	for i in range(15):
		for j in range(15):
			all_layer[i][j][0] = layer_1[i][j]
			all_layer[i][j][1] = layer_2[i][j]
			all_layer[i][j][2] = layer_3[i][j]
			all_layer[i][j][3] = layer_4[i][j]
			all_layer[i][j][4] = layer_5[i][j]
			all_layer[i][j][5] = layer_6[i][j]
			all_layer[i][j][6] = layer_7[i][j]
			all_layer[i][j][7] = layer_8[i][j]
			all_layer[i][j][8] = layer_9[i][j]
			all_layer[i][j][9] = layer_10[i][j]
			all_layer[i][j][10] = layer_11[i][j]
			all_layer[i][j][11] = layer_12[i][j]
			all_layer[i][j][12] = layer_13[i][j]
			all_layer[i][j][13] = layer_14[i][j]
			all_layer[i][j][14] = layer_15[i][j]
			all_layer[i][j][15] = layer_16[i][j]
			all_layer[i][j][16] = layer_17[i][j]
			all_layer[i][j][17] = layer_18[i][j]
			all_layer[i][j][18] = layer_19[i][j]
			all_layer[i][j][19] = layer_20[i][j]
			all_layer[i][j][20] = layer_21[i][j]
			all_layer[i][j][21] = layer_22[i][j]
			all_layer[i][j][22] = layer_23[i][j]
			all_layer[i][j][23] = layer_24[i][j]
			all_layer[i][j][24] = layer_25[i][j]
			all_layer[i][j][25] = layer_26[i][j]
			all_layer[i][j][26] = layer_27[i][j]
			all_layer[i][j][27] = layer_28[i][j]
			all_layer[i][j][28] = layer_29[i][j]
			all_layer[i][j][29] = layer_30[i][j]
			all_layer[i][j][30] = layer_31[i][j]
			all_layer[i][j][31] = layer_32[i][j]
			all_layer[i][j][32] = layer_33[i][j]
			all_layer[i][j][33] = layer_34[i][j]
			all_layer[i][j][34] = layer_35[i][j]
			all_layer[i][j][35] = layer_36[i][j]
			all_layer[i][j][36] = layer_37[i][j]
			all_layer[i][j][37] = layer_38[i][j]
			all_layer[i][j][38] = layer_39[i][j]
			all_layer[i][j][39] = layer_40[i][j]
			all_layer[i][j][40] = layer_41[i][j]
			all_layer[i][j][41] = layer_42[i][j]
			all_layer[i][j][42] = layer_43[i][j]
			all_layer[i][j][43] = layer_44[i][j]
			all_layer[i][j][44] = layer_45[i][j]
			all_layer[i][j][45] = layer_46[i][j]
			all_layer[i][j][46] = layer_47[i][j]
			all_layer[i][j][47] = layer_48[i][j]
	return all_layer

def ConvertToNum(step):
	first = step[0]
	second = step[1:]
	num = (ord(first)-ord('a'))+(int(second)-1)*15
	return num

def StepGame(step ,set,color ):
	y = step /15
	x = step %15
	set[y][x] = color
	return set

def Retrun_fif_to_nine_set(set,out):
	check =Return_nine_can_use(set,out)

	anw = []
	for i in range(15):
		for j in range(15):
			if check[i][j] ==1:
				ele = local_policy_analysis.ReturnFiftoEight(set,i,j)
				anw.append(ele)





	return anw

def Return_nine_can_use(set,out):
	anw_lib = local_policy_analysis.evaluate_square_five_check(out)
 	check = [[0 for i in range(15)] for j in range(15)]
 	for i in range(15):
		for j in range(15):
			if anw_lib[i][j] ==1 and set[i][j] ==0:
				check[i][j] =1
			if out[i][j]==1:
				check[i][j] =1
	return check


def ReturnFif_to_Nine(set, x , y):
	return local_policy_analysis.ReturnFiftoEight(set, x ,y )

def Retrun_fif_to_nine_anw(set,out):
	
 	check =Return_nine_can_use(set,out)

	anw = []
	for i in range(15):
		for j in range(15):
			if check[i][j] ==1:
				ele = local_policy_analysis.ReturnFiftoEight(out,i,j)
				anw.append(ele)
	return anw

def Show_game_nine(set):
	seq = 1
	for i in range(81):
		if i %9 ==0:
			print ("")
		if set[i] == 1:
			print("X ", end="")

			
		elif set[i] ==0.5:
			print("O ", end="")
		elif set[i] ==9999:
			print ("? ", end="")

			
		else :
			print('. ', end="")
		if i %9 ==8:
			print("",seq,end= "")
			seq = seq + 1
	print ("")
	for i in range(9):
		print (chr(ord('a')+i),end = " ")

	print ("\n")

def Return_Eight_anw_nine(set,color):
	all_anw = []
	if set[4][4]==1:
		if color ==1:
			all_anw = [[0,1,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0]]
		if color ==0.5:
			all_anw = [[0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1]]
	else:
		all_anw = [[1,0,0], [1,0,0], [1,0,0], [1,0,0], [1,0,0], [1,0,0], [1,0,0], [1,0,0]]
	

	
	return all_anw
def Return__anw_nine(set,color):
	all_anw = []
	if set[4][4]==1:
		if color ==1:
			all_anw = [0,1,0]
		if color ==0.5:
			all_anw = [0,0,1]
	else:
		all_anw = [0,0,0]
	

	
	return all_anw


def Return_Eight_Layer_nine(set):
	
	left = set
	up = martix.rotate90_nine(left)
	right = martix.rotate90_nine(up)
	down =  martix.rotate90_nine(up)
	ref_left = martix.reflection_nine(set)
	ref_up = martix.rotate90_nine(ref_left)
	ref_right =  martix.rotate90_nine(ref_up)
	ref_down = martix.rotate90_nine(ref_right)

	all_layer = [np.reshape(left,[81]), np.reshape(up,[81]) , np.reshape(right,[81]), 
	np.reshape(down,[81]), np.reshape(ref_left,[81]), np.reshape(ref_up,[81]), 
	np.reshape(ref_right,[81]), np.reshape(ref_down,[81])]
	return all_layer

def ReturnAllInfo_nine(set,color):
	ocolor = 1
	if color == 1:
		ocolor = 0.5

	layer_1 = local_policy_analysis.evaluate_nine_self(set,color)

	layer_2 = local_policy_analysis.evaluate_nine_self(set,ocolor)

	layer_3 = local_policy_analysis.evaluate_nine_self(set,0)

	layer_4 = [[1 for i in range(9)] for j in range(9)]

	# player
	layer_5 = local_policy_analysis.evaluate_nine_lib_five(set,color)

	layer_6 = local_policy_analysis.evaluate_nine_square_three(set,color)

	layer_7 = local_policy_analysis.evaluate_nine_dead_two(set,color)

	layer_8 = local_policy_analysis.evaluate_nine_alive_two(set,color)

	layer_9 = local_policy_analysis.evaluate_nine_dead_three(set,color)

	layer_10 = local_policy_analysis.evaluate_nine_alive_three(set,color)

	layer_11 = local_policy_analysis.evaluate_nine_dead_four(set,color)

	layer_12 = local_policy_analysis.evaluate_nine_alive_four(set,color)

	layer_13 = local_policy_analysis.evaluate_nine_five(set,color)

	layer_14 = [[1 for i in range(9)] for j in range(9)]

	#opponent
	layer_9 = local_policy_analysis.evaluate_nine_lib_five(set,ocolor)

	layer_16 = local_policy_analysis.evaluate_nine_square_three(set,ocolor)

	layer_17 = local_policy_analysis.evaluate_nine_dead_two(set,ocolor)

	layer_18 = local_policy_analysis.evaluate_nine_alive_two(set,ocolor)

	layer_19 = local_policy_analysis.evaluate_nine_dead_three(set,ocolor)

	layer_20 = local_policy_analysis.evaluate_nine_alive_three(set,ocolor)

	layer_21 = local_policy_analysis.evaluate_nine_dead_four(set,ocolor)

	layer_22 = local_policy_analysis.evaluate_nine_alive_four(set,ocolor)

	layer_23 = local_policy_analysis.evaluate_nine_five(set,ocolor)
	layer_24= [[0 for i in range(9)] for j in range(9)]

	layer_25= [[1 for i in range(9)] for j in range(9)]
	if color ==0.5:
		layer_24= [[0 for i in range(9)] for j in range(9)]




	all_layer = [[[0 for i in range(25)] for j in range(9)] for x in range(9)]

	for i in range(9):
		for j in range(9):
			all_layer[i][j][0] = layer_1[i][j]
			all_layer[i][j][1] = layer_2[i][j]
			all_layer[i][j][2] = layer_3[i][j]
			all_layer[i][j][3] = layer_4[i][j]
			all_layer[i][j][4] = layer_5[i][j]
			all_layer[i][j][5] = layer_6[i][j]
			all_layer[i][j][6] = layer_7[i][j]
			all_layer[i][j][7] = layer_8[i][j]
			all_layer[i][j][8] = layer_9[i][j]
			all_layer[i][j][9] = layer_10[i][j]
			all_layer[i][j][10] = layer_11[i][j]
			all_layer[i][j][11] = layer_12[i][j]
			all_layer[i][j][12] = layer_13[i][j]
			all_layer[i][j][13] = layer_14[i][j]
			all_layer[i][j][14] = layer_9[i][j]
			all_layer[i][j][9] = layer_16[i][j]
			all_layer[i][j][16] = layer_17[i][j]
			all_layer[i][j][17] = layer_18[i][j]
			all_layer[i][j][18] = layer_19[i][j]
			all_layer[i][j][19] = layer_20[i][j]
			all_layer[i][j][20] = layer_21[i][j]
			all_layer[i][j][21] = layer_22[i][j]
			all_layer[i][j][22] = layer_23[i][j]
			all_layer[i][j][23] = layer_24[i][j]
			all_layer[i][j][24] = layer_25[i][j]
	return all_layer

def ReturnAllLayer_nine(set,color):
	s = set
	left = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)
	up = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)
	right = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)
	down = ReturnAllInfo_nine(s,color)

	s =  martix.reflection_nine(set)
	ref_left  = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)

	ref_up = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)

	ref_right = ReturnAllInfo_nine(s,color)
	s = martix.rotate90_nine(s)
	ref_down = ReturnAllInfo_nine(s,color)
	all_layer = [left, up, right, down, ref_left, ref_up, ref_right, ref_down]

	return all_layer
