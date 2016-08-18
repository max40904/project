import numpy as np



def rotate90_fif(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[14 - j][ i ]



	return anw


def reflection_fif(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[ i ][ 14 - j ]



	return anw

def rotate90_nine(set):
	anw = [[0 for i in range(9)] for j in range(9)]
	for i in range( 0 , 9 ) :
		for j in range( 0 , 9 ):
			anw [i] [j]=  set[8 - j][ i ]



	return anw

def reflection_nine(set):
	anw = [[0 for i in range(9)] for j in range(9)]
	for i in range( 0 , 9 ) :
		for j in range( 0 , 9 ):
			anw [i] [j]=  set[ i ][ 8 - j ]



	return anw

