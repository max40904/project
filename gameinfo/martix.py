import numpy as np



def rotate90_fif(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[14 - j][ i ]



	return anw

def rotate90_num_fif(num):
	if num ==0:
		return 0
	j = num /15
	i = num %15
	new_j = i
	new_i = 14 - j
	return new_j*15+new_i

def reflection_num_fif(num):
	if num ==0:
		return 0
	j = num /15
	i = num %15
	new_j = j
	new_i = 14 - i
	return new_j*15+new_i

def reflection_fif(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[ i ][ 14 - j ]



	return anw

def rotate90_nine(set):
	anw = [[0 for i in range(11)] for j in range(11)]
	for i in range( 0 , 11 ) :
		for j in range( 0 , 11 ):
			anw [i] [j]=  set[10 - j][ i ]



	return anw

def reflection_nine(set):
	anw = [[0 for i in range(11)] for j in range(11)]
	for i in range( 0 , 11 ) :
		for j in range( 0 , 11 ):
			anw [i] [j]=  set[ i ][ 10 - j ]



	return anw


