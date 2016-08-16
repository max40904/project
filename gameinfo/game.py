
from __future__ import print_function
import martix
import policy_analysis
import local_policy_analysis
import numpy as np

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
	up = martix.rotate90(left)
	right = martix.rotate90(up)
	down =  martix.rotate90(up)
	ref_left = martix.reflection(set)
	ref_up = martix.rotate90(ref_left)
	ref_right =  martix.rotate90(ref_up)
	ref_down = martix.rotate90(ref_right)

	all_layer = [np.reshape(left,[225]), np.reshape(up,[225]) , np.reshape(right,[225]), 
	np.reshape(down,[225]), np.reshape(ref_left,[225]), np.reshape(ref_up,[225]), 
	np.reshape(ref_right,[225]), np.reshape(ref_down,[225])]
	return all_layer


def ReturnAllLayer(set,color):
	s = set
	left = ReturnAllInfo(s,color)
	s = martix.rotate90(s)
	up = ReturnAllInfo(s,color)
	s = martix.rotate90(s)
	right = ReturnAllInfo(s,color)
	s = martix.rotate90(s)
	down = ReturnAllInfo(s,color)

	s =  martix.reflection(set)
	ref_left  = ReturnAllInfo(s,color)
	s = martix.rotate90(s)

	ref_up = ReturnAllInfo(s,color)
	s = martix.rotate90(s)

	ref_right = ReturnAllInfo(s,color)
	s = martix.rotate90(s)
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

	layer_6 = policy_analysis.evaluate_square_three(set,color)

	layer_7 = policy_analysis.evaluate_dead_two(set,color)

	layer_8 = policy_analysis.evaluate_alive_two(set,color)

	layer_9 = policy_analysis.evaluate_dead_three(set,color)

	layer_10 = policy_analysis.evaluate_alive_three(set,color)

	layer_11 = policy_analysis.evaluate_dead_four(set,color)

	layer_12 = policy_analysis.evaluate_alive_four(set,color)

	layer_13 = policy_analysis.evaluate_five(set,color)

	layer_14 = [[1 for i in range(15)] for j in range(15)]

	#opponent
	layer_15 = policy_analysis.evaluate_lib_five(set,ocolor)

	layer_16 = policy_analysis.evaluate_square_three(set,ocolor)

	layer_17 = policy_analysis.evaluate_dead_two(set,ocolor)

	layer_18 = policy_analysis.evaluate_alive_two(set,ocolor)

	layer_19 = policy_analysis.evaluate_dead_three(set,ocolor)

	layer_20 = policy_analysis.evaluate_alive_three(set,ocolor)

	layer_21 = policy_analysis.evaluate_dead_four(set,ocolor)

	layer_22 = policy_analysis.evaluate_alive_four(set,ocolor)

	layer_23 = policy_analysis.evaluate_five(set,ocolor)

	layer_24= [[0 for i in range(15)] for j in range(15)]




	all_layer = [[[0 for i in range(24)] for j in range(15)] for x in range(15)]

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
	set_lib = local_policy_analysis.evaluate_square_five_check(set)
	anw_lib = local_policy_analysis.evaluate_square_five_check(out)
 	check = [[0 for i in range(15)] for j in range(15)]
 	for i in range(15):
		for j in range(15):
			if set_lib[i][j] ==1 and set_lib[i][j] ==1:
				check[i][j] =1
			if out[i][j]==1:
				check[i][j] =1

	anw = []
	for i in range(15):
		for j in range(15):
			if check[i][j] ==1:
				ele = local_policy_analysis.ReturnFiftoEight(set,i,j)
				anw.append(ele)





	return anw

def show_game_eight(set):
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
