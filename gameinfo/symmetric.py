import numpy as np
def evaluate_all(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == 0:
				anw[y][x] = 1
	return anw
def evaluate_alive_two(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == 0 :  
					for i in range(1 , 3):
						if x + i <= high_edge and set[ y ] [ x + i +1 ] == 0 and set_x[ y ][ x + i] == 0:
							anw [ y ][ x + i ]= 1
						else :
							break

				#left
				if x + 1 <= high_edge + 1  and set [ y ][ x + 1 ] == 0 :
					for i in range( 1 , 3):
						if x - i >= low_edge and set[ y ][ x - i - 1] == 0 and set_x [ y ][ x - i] == 0: 
							anw [ y ] [ x - i ] = 1
						else :
							break

				#up
				if y - 1 >= low_edge -1 and set [ y  - 1][ x ] == 0 :
					for i in range(1 , 3 ):

						if y + i <= high_edge and set [ y + i + 1 ][ x ] ==0 and set_x [ y + i ][ x ] == 0:
							anw [ y + i ][ x ] =1
						else :
							break

				#down
				if y + 1 <= high_edge + 1  and set [ y + 1][ x ] == 0 :
					for i in range( 1 , 3 ):
						if y - i >= low_edge and set [ y - i - 1 ] [ x ] == 0 and set_x [ y - i ][ x ] == 0:
							anw [ y - i ][ x ] = 1
						else :
							break



				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==0:
					for i in range(1 , 3 ):
						if x - i >= low_edge and y - i >= low_edge and set [ y - i -1 ][ x - i -1  ] ==0 and set_x [ y -i ][ x - i] == 0:
							anw [ y - i ][ x - i ] = 1
						else :
							break

				#right_up
				if x - 1 >= low_edge  - 1 and y + 1 <= high_edge  + 1 and set [ y + 1][ x - 1 ] ==0:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y - i >= low_edge and set [ y - i -  1] [ x + i + 1] == 0 and set_x [ y -i ][ x + i] == 0 :
							anw [ y - i ][ x + i ] = 1
						else :
							break

				#right_down
				if x - 1 >= low_edge  - 1 and y - 1 >= low_edge - 1and set [ y - 1][ x - 1 ] ==0:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y + i <= high_edge and set [ y + i +  1] [ x + i + 1] == 0 and set_x [ y + i ][ x + i] == 0:
							anw [ y + i ][ x + i ] = 1
						else :
							break
				#left_down
				if x + 1 <= high_edge + 1  and y - 1 >= low_edge - 1 and set [ y - 1][ x + 1 ] ==0:
					for i in range(1 , 3 ):
						if x  - i >=low_edge and y + i <= high_edge and set [ y + i +  1] [ x - i - 1] == 0 and set_x [ y + i  ][ x - i] == 0:
							anw [ y + i ][ x - i ] = 1
						else :
							break


				

				
	return anw
def evaluate_dead_two(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == rflag :  
					for i in range(1 , 3):
						if x + i <= high_edge and set[ y ] [ x + i +1 ] == 0 and set_x[ y ][ x + i] == 0:
							anw [ y ][ x + i ]= 1
						else :
							break

				#left
				if x + 1 <= high_edge + 1  and set [ y ][ x + 1 ] == rflag :
					for i in range( 1 , 3):
						if x - i >= low_edge and set[ y ][ x - i - 1] == 0 and set_x [ y ][ x - i] == 0: 
							anw [ y ] [ x - i ] = 1
						else :
							break

				#up
				if y - 1 >= low_edge -1 and set [ y  - 1][ x ] == rflag :
					for i in range(1 , 3 ):

						if y + i <= high_edge and set [ y + i + 1 ][ x ] ==0 and set_x [ y + i ][ x ] == 0:
							anw [ y + i ][ x ] =1
						else :
							break

				#down
				if y + 1 <= high_edge + 1  and set [ y + 1][ x ] == rflag :
					for i in range( 1 , 3 ):
						if y - i >= low_edge and set [ y - i - 1 ] [ x ] == 0 and set_x [ y - i ][ x ] == 0:
							anw [ y - i ][ x ] = 1
						else :
							break



				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x - i >= low_edge and y - i >= low_edge and set [ y - i -1 ][ x - i -1  ] ==0 and set_x [ y -i ][ x - i] == 0:
							anw [ y - i ][ x - i ] = 1
						else :
							break

				#right_up
				if x - 1 >= low_edge  - 1 and y + 1 <= high_edge  + 1 and set [ y + 1][ x - 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y - i >= low_edge and set [ y - i -  1] [ x + i + 1] == 0 and set_x [ y -i ][ x + i] == 0 :
							anw [ y - i ][ x + i ] = 1
						else :
							break

				#right_down
				if x - 1 >= low_edge  - 1 and y - 1 >= low_edge - 1and set [ y - 1][ x - 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y + i <= high_edge and set [ y + i +  1] [ x + i + 1] == 0 and set_x [ y + i ][ x + i] == 0:
							anw [ y + i ][ x + i ] = 1
						else :
							break
				#left_down
				if x + 1 <= high_edge + 1  and y - 1 >= low_edge - 1 and set [ y - 1][ x + 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  - i >=low_edge and y + i <= high_edge and set [ y + i +  1] [ x - i - 1] == 0 and set_x [ y + i  ][ x - i] == 0:
							anw [ y + i ][ x - i ] = 1
						else :
							break


				

				
	return anw
def evaluate_dead_three(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == rflag :  
					
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == flag and set[ y ] [ x + 2 ] == 0 and set_x[ y ][ x + 3] == 0:
						anw [ y ][ x + 2 ]= 1
						anw [ y ][ x + 3 ]= 1
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == 0 and set[ y ] [ x + 2 ] == flag and set_x[ y ][ x + 3] == 0:
						anw [ y ][ x + 3 ]= 1
						anw [ y ][ x + 1 ]= 1

				#left
				if x + 1 <= high_edge  + 1 and set [ y ][ x + 1 ] == rflag :  
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == flag and set[ y ] [ x - 2 ] == 0 and set_x[ y ][ x - 3] == 0:
						anw [ y ][ x - 2 ]= 1
						anw [ y ][ x - 3 ]= 1
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == 0 and set[ y ] [ x - 2 ] == flag and set_x[ y ][ x - 3] == 0:
						anw [ y ][ x - 1 ]= 1
						anw [ y ][ x - 3 ]= 1
				#up
				if y - 1 >= low_edge -1 and set [ y - 1 ][ x ] == rflag :  
					if y + 3 <= high_edge and set[ y + 1  ] [ x  ] == flag and set[ y + 2 ] [ x  ] == 0 and set_x[ y + 3 ][ x ] == 0:
						anw [ y + 2 ][ x ]= 1
						anw [ y + 3 ][ x ]= 1
					if y + 3 <= high_edge and set[ y + 1] [ x ] == 0 and set[ y + 2 ] [ x ] == flag and set_x[ y + 3 ][ x ] == 0:
						anw [ y  + 1][ x ]= 1
						anw [ y  + 3][ x ]= 1
				#down
				if y + 1 <= high_edge  + 1 and set [ y + 1 ][ x ] == rflag :  
					if y - 3 <= low_edge and set[ y - 1  ] [ x  ] == flag and set[ y - 2 ] [ x  ] == 0 and set_x[ y - 3 ][ x ] == 0:
						anw [ y - 2 ][ x ]= 1
						anw [ y - 3 ][ x ]= 1
					if y - 3 <= low_edge and set[ y - 1] [ x ] == 0 and set[ y - 2 ] [ x ] == flag and set_x[ y - 3 ][ x ] == 0:
						anw [ y - 1][ x ]= 1
						anw [ y - 3][ x ]= 1

				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==rflag:
					if  x - 3 >= low_edge and y - 3 >= low_edge:
						if  set[ y - 1 ][ x - 1 ] == flag and set[ y - 2 ][ x - 2 ] ==0 and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 2 ][ x - 2 ]= 1
							anw [ y - 3 ][ x - 3 ]= 1
						if  set[ y - 1 ][ x - 1 ] == 0 and set[ y - 2 ][ x - 2 ] == flag and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 1 ][ x - 1 ]= 1
							anw [ y - 3 ][ x - 3 ]= 1


				#right_up

				if x - 1 >= low_edge - 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x - 1 ] ==rflag:
					if x + 3 <= high_edge and  y - 3 >= low_edge :
						if  set[ y - 1 ][ x + 1 ] == flag and set[ y - 2 ][ x + 2 ] ==0 and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 2 ][ x + 2 ]= 1
							anw [ y - 3 ][ x + 3 ]= 1
						if  set[ y - 1 ][ x + 1 ] == 0 and set[ y - 2 ][ x + 2 ] == flag and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 1 ][ x + 1 ]= 1
							anw [ y - 3 ][ x + 3 ]= 1


				#right_down
				if x - 1 >= low_edge - 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x - 1 ] ==rflag:
					if x + 3 <= high_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x + 1 ] == flag and set[ y + 2 ][ x + 2 ] ==0 and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 2 ][ x + 2 ]= 1
							anw [ y + 3 ][ x + 3 ]= 1
						if  set[ y + 1 ][ x + 1 ] == 0 and set[ y + 2 ][ x + 2 ] == flag and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 1 ][ x + 1 ]= 1
							anw [ y + 3 ][ x + 3 ]= 1


				#left_down
				if x + 1 <= high_edge + 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x + 1 ] ==rflag:
					if x - 3>= low_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x - 1 ] == flag and set[ y + 2 ][ x - 2 ] ==0 and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 2 ][ x - 2 ]= 1
							anw [ y + 3 ][ x - 3 ]= 1
						if  set[ y + 1 ][ x - 1 ] == 0 and set[ y + 2 ][ x - 2 ] == flag and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 1 ][ x - 1 ]= 1
							anw [ y + 3 ][ x - 3 ]= 1


			


				

				
	return anw
def evaluate_lib_five(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[y][x] == flag :
				for i in range(5):
				
					if y - i >= 0 and set[y - i][ x ] ==0:
						anw [ y - i ][ x ] = 1

					if y + i <=14 and set[y + i][ x ] ==0:
						anw [ y + i ][ x ] = 1


					if x + i <= 14 and set[y ][ x + i ] ==0:
						anw [ y ][ x + i ] = 1


					if x - i >= 0  and set[y ][ x - i ] ==0:
						anw [ y ][ x - i ] = 1 


					if x - i >= 0 and y - i >=0 and set[y - i][ x - i ] ==0:
						anw [ y - i] [ x -  i] =1


					if x + i <= 14 and y - i >=0  and set[y - i][ x + i ] ==0:
						anw [ y - i] [x + i] =1

					if x -i >= 0 and y + i <= 14 and set[y + i][ x - i ] ==0:
						anw [y + i][ x - i ] = 1

					if x + i <= 14 and y +i <= 14  and set[y + i][ x + i ] ==0:
						anw [ y + i] [x + i] = 1
	return anw


def rotate90(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[14 - j][ i ]



	return anw


def reflection(set):
	anw = [[0 for i in range(15)] for j in range(15)]
	for i in range( 0 , 15 ) :
		for j in range( 0 , 15 ):
			anw [i] [j]=  set[ i ][ 14 - j ]



	return anw