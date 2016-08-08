
from __future__ import print_function
import symmetric
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
	show_game_pos(num)

def ReturnAllLayer(set,color):
	s = set
	left = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)
	up = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)
	right = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)
	down = ReturnAllInfo(s,color)

	s =  symmetric.reflection(set)
	ref_left  = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)

	ref_up = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)

	ref_right = ReturnAllInfo(s,color)
	s = symmetric.rotate90(s)
	ref_down = ReturnAllInfo(s,color)
	all_layer = [left, up, right, down, ref_left, ref_up, ref_right, ref_down]

	return 

def ReturnAllInfo(set,color):
	ocolor = 1
	if color == 1:
		ocolor = 0.5

	layer_1 = symmetric.evaluate_self(set,color)

	layer_2 = symmetric.evaluate_self(set,ocolor)

	layer_3 = symmetric.evaluate_self(set,0)

	layer_4 = [[1 for i in range(15)] for j in range(15)]

	# player
	layer_6 = symmetric.evaluate_lib_five(set,color)

	layer_5 = symmetric.evaluate_square_three(set,color)

	layer_7 = symmetric.evaluate_dead_two(set,color)

	layer_8 = symmetric.evaluate_alive_two(set,color)

	layer_9 = symmetric.evaluate_dead_three(set,color)

	layer_10 = symmetric.evaluate_alive_three(set,color)

	layer_11 = symmetric.evaluate_dead_four(set,color)

	layer_12 = symmetric.evaluate_alive_four(set,color)

	layer_13 = symmetric.evaluate_five(set,color)

	layer_14 = [[1 for i in range(15)] for j in range(15)]

	#opponent
	layer_15 = symmetric.evaluate_lib_five(set,ocolor)

	layer_16 = symmetric.evaluate_square_three(set,ocolor)

	layer_17 = symmetric.evaluate_dead_two(set,ocolor)

	layer_18 = symmetric.evaluate_alive_two(set,ocolor)

	layer_19 = symmetric.evaluate_dead_three(set,ocolor)

	layer_20 = symmetric.evaluate_alive_three(set,ocolor)

	layer_21 = symmetric.evaluate_dead_four(set,ocolor)

	layer_22 = symmetric.evaluate_alive_four(set,ocolor)

	layer_23 = symmetric.evaluate_five(set,ocolor)

	layer_24= [[0 for i in range(15)] for j in range(15)]




	all_layer = [[[0 for i in range(4)] for j in range(15)] for x in range(15)]

	for i in range(15):
		for j in range(15):
			all_layer[i][j][0] = layer_1[i][j]
			all_layer[i][j][1] = layer_2[i][j]
			all_layer[i][j][2] = layer_3[i][j]
			all_layer[i][j][3] = layer_4[i][j]

	return all_layer

