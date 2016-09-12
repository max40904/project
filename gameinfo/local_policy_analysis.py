def evaluate_square_five_check(set):
	
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] != 0:
				for i in range(-4,5):
					for j in range(-4,5):
						if x + j <=14 and x + j >=0 and y + i >= 0 and y + i <= 14 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def ReturnFiftoEight(set, x , y):
	anw = [[0 for i in range(9)] for h in range(9)]
	for i in range(-4,5):
		for j in range(-4, 5):
			if x + i >=0 and x + i <= 14 and y + j >=0 and y + j <=14 :
				anw [ i + 4 ][ j + 4 ] =set [ x + i ][ y + j ]
			else:
				anw [ i + 4 ][ j + 4 ] =9999

	return anw


def evaluate_nine_self(set,flag):
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[y][x] == flag:
				anw[y][x] = 1
	return anw

def evaluate_nine_square_three(set,flag):
	highedge = 9
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(highedge)] for j in range(highedge)]
	for y in range(highedge):
		for x in range(highedge):
			if set[y][x] == flag:
				for i in range(-2,3):
					for j in range(-2,3):
						if x + j <=highedge - 1 and x + j >=0 and y + i >= 0 and y + i <= highedge -1 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw
def evaluate_nine_square_two(set,flag):
	highedge = 9
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(highedge)] for j in range(highedge)]
	for y in range(highedge):
		for x in range(highedge):
			if set[y][x] == flag:
				for i in range(-1,2):
					for j in range(-1,2):
						if x + j <=highedge - 1 and x + j >=0 and y + i >= 0 and y + i <= highedge -1 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def evaluate_nine_square_four(set,flag):
	highedge = 9
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(highedge)] for j in range(highedge)]
	for y in range(highedge):
		for x in range(highedge):
			if set[y][x] == flag:
				for i in range(-3,4):
					for j in range(-3,4):
						if x + j <=highedge - 1 and x + j >=0 and y + i >= 0 and y + i <= highedge -1 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def evaluate_nine_lib_five(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[y][x] == flag :
				for i in range(1,5):
					if y - i >= 0 and set[y - i][ x ] ==0:
						anw [ y - i ][ x ] = 1
					else:
						break
				for i in range(1,5):
					if y + i <=8 and set[y + i][ x ] ==0:
						anw [ y + i ][ x ] = 1
					else:
						break
				for i in range(1,5):
					if x + i <= 8 and set[y ][ x + i ] ==0:
						anw [ y ][ x + i ] = 1
					else:
						break
				for i in range(1,5):
					if x - i >= 0  and set[y ][ x - i ] ==0:
						anw [ y ][ x - i ] = 1
					else:
						break
				for i in range(1,5):
					if x - i >= 0 and y - i >=0 and set[y - i][ x - i ] ==0:
						anw [ y - i] [ x -  i] =1
					else:
						break
				for i in range(1,5):
					if x + i <= 8 and y - i >=0  and set[y - i][ x + i ] ==0:
						anw [ y - i] [x + i] =1
					else:
						break
				for i in range(1,5):
					if x -i >= 0 and y + i <= 8 and set[y + i][ x - i ] ==0:
						anw [y + i][ x - i ] = 1
					else:
						break
				for i in range(1,5):
					if x + i <= 8 and y +i <= 8  and set[y + i][ x + i ] ==0:
						anw [ y + i] [x + i] = 1
					else:
						break
	return anw


def evaluate_nine_dead_two(set, flag , filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 7
	low_edge = 1
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == rflag :  
					for i in range(1 , 3):
						if x + i <= high_edge and set[ y ] [ x + i +1 ] == 0 and set[ y ][ x + i] == 0:
							anw [ y ][ x + i ]= anw [ y ][ x + i ] + 1
						else :
							break

				#left
				if x + 1 <= high_edge + 1  and set [ y ][ x + 1 ] == rflag :
					for i in range( 1 , 3):
						if x - i >= low_edge and set[ y ][ x - i - 1] == 0 and set [ y ][ x - i] == 0: 
							anw [ y ] [ x - i ] =anw [ y ] [ x - i ]  +  1
						else :
							break

				#up
				if y - 1 >= low_edge -1 and set [ y  - 1][ x ] == rflag :
					for i in range(1 , 3 ):

						if y + i <= high_edge and set [ y + i + 1 ][ x ] ==0 and set [ y + i ][ x ] == 0:
							anw [ y + i ][ x ] =anw [ y + i ][ x ] + 1
						else :
							break

				#down
				if y + 1 <= high_edge + 1  and set [ y + 1][ x ] == rflag :
					for i in range( 1 , 3 ):
						if y - i >= low_edge and set [ y - i - 1 ] [ x ] == 0 and set [ y - i ][ x ] == 0:
							anw [ y - i ][ x ] = anw [ y - i ][ x ] + 1
						else :
							break



				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x - i >= low_edge and y - i >= low_edge and set [ y - i -1 ][ x - i -1  ] ==0 and set [ y -i ][ x - i] == 0:
							anw [ y - i ][ x - i ] = anw [ y - i ][ x - i ] + 1
						else :
							break

				#right_up
				if x - 1 >= low_edge  - 1 and y + 1 <= high_edge  + 1 and set [ y + 1][ x - 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y - i >= low_edge and set [ y - i -  1] [ x + i + 1] == 0 and set [ y -i ][ x + i] == 0 :
							anw [ y - i ][ x + i ] = anw [ y - i ][ x + i ] +  1
						else :
							break

				#right_down
				if x - 1 >= low_edge  - 1 and y - 1 >= low_edge - 1and set [ y - 1][ x - 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y + i <= high_edge and set [ y + i +  1] [ x + i + 1] == 0 and set [ y + i ][ x + i] == 0:
							anw [ y + i ][ x + i ] = anw [ y + i ][ x + i ] + 1
						else :
							break
				#left_down
				if x + 1 <= high_edge + 1  and y - 1 >= low_edge - 1 and set [ y - 1][ x + 1 ] ==rflag:
					for i in range(1 , 3 ):
						if x  - i >=low_edge and y + i <= high_edge and set [ y + i +  1] [ x - i - 1] == 0 and set [ y + i  ][ x - i] == 0:
							anw [ y + i ][ x - i ] =anw [ y + i ][ x - i ] +  1
						else :
							break


	return Return_nine_Num_Filter(anw,filter)


def evaluate_nine_alive_two(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 7
	low_edge = 1
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == 0 :  
					for i in range(1 , 3):
						if x + i <= high_edge and set[ y ] [ x + i +1 ] == 0 and set[ y ][ x + i] == 0:
							anw [ y ][ x + i ]+= 1
						else :
							break

				#left
				if x + 1 <= high_edge + 1  and set [ y ][ x + 1 ] == 0 :
					for i in range( 1 , 3):
						if x - i >= low_edge and set[ y ][ x - i - 1] == 0 and set [ y ][ x - i] == 0: 
							anw [ y ] [ x - i ] += 1
						else :
							break

				#up
				if y - 1 >= low_edge -1 and set [ y  - 1][ x ] == 0 :
					for i in range(1 , 3 ):

						if y + i <= high_edge and set [ y + i + 1 ][ x ] ==0 and set [ y + i ][ x ] == 0:
							anw [ y + i ][ x ] +=1
						else :
							break

				#down
				if y + 1 <= high_edge + 1  and set [ y + 1][ x ] == 0 :
					for i in range( 1 , 3 ):
						if y - i >= low_edge and set [ y - i - 1 ] [ x ] == 0 and set [ y - i ][ x ] == 0:
							anw [ y - i ][ x ] += 1
						else :
							break



				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==0:
					for i in range(1 , 3 ):
						if x - i >= low_edge and y - i >= low_edge and set [ y - i -1 ][ x - i -1  ] ==0 and set [ y -i ][ x - i] == 0:
							anw [ y - i ][ x - i ] += 1
						else :
							break

				#right_up
				if x - 1 >= low_edge  - 1 and y + 1 <= high_edge  + 1 and set [ y + 1][ x - 1 ] ==0:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y - i >= low_edge and set [ y - i -  1] [ x + i + 1] == 0 and set [ y -i ][ x + i] == 0 :
							anw [ y - i ][ x + i ] += 1
						else :
							break

				#right_down
				if x - 1 >= low_edge  - 1 and y - 1 >= low_edge - 1and set [ y - 1][ x - 1 ] ==0:
					for i in range(1 , 3 ):
						if x  + i <=high_edge and y + i <= high_edge and set [ y + i +  1] [ x + i + 1] == 0 and set [ y + i ][ x + i] == 0:
							anw [ y + i ][ x + i ] += 1
						else :
							break
				#left_down
				if x + 1 <= high_edge + 1  and y - 1 >= low_edge - 1 and set [ y - 1][ x + 1 ] ==0:
					for i in range(1 , 3 ):
						if x  - i >=low_edge and y + i <= high_edge and set [ y + i +  1] [ x - i - 1] == 0 and set [ y + i  ][ x - i] == 0:
							anw [ y + i ][ x - i ] += 1
						else :
							break


				

				
	return Return_nine_Num_Filter(anw,filter)


def evaluate_nine_dead_three(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 7
	low_edge = 1
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == rflag :  
					
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == flag and set[ y ] [ x + 2 ] == 0 and set[ y ][ x + 3] == 0:
						anw [ y ][ x + 2 ] += 1
						anw [ y ][ x + 3 ] += 1
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == 0 and set[ y ] [ x + 2 ] == flag and set[ y ][ x + 3] == 0:
						anw [ y ][ x + 3 ] += 1
						anw [ y ][ x + 1 ] += 1

				#left
				if x + 1 <= high_edge  + 1 and set [ y ][ x + 1 ] == rflag :  
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == flag and set[ y ] [ x - 2 ] == 0 and set[ y ][ x - 3] == 0:
						anw [ y ][ x - 2 ] += 1
						anw [ y ][ x - 3 ] += 1
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == 0 and set[ y ] [ x - 2 ] == flag and set[ y ][ x - 3] == 0:
						anw [ y ][ x - 1 ] += 1
						anw [ y ][ x - 3 ] += 1
				#up
				if y - 1 >= low_edge -1 and set [ y - 1 ][ x ] == rflag :  
					if y + 3 <= high_edge and set[ y + 1  ] [ x  ] == flag and set[ y + 2 ] [ x  ] == 0 and set[ y + 3 ][ x ] == 0:
						anw [ y + 2 ][ x ] += 1
						anw [ y + 3 ][ x ] += 1
					if y + 3 <= high_edge and set[ y + 1] [ x ] == 0 and set[ y + 2 ] [ x ] == flag and set[ y + 3 ][ x ] == 0:
						anw [ y  + 1][ x ] += 1
						anw [ y  + 3][ x ] += 1
				#down
				if y + 1 <= high_edge  + 1 and set [ y + 1 ][ x ] == rflag :  
					if y - 3 >= low_edge and set[ y - 1  ] [ x  ] == flag and set[ y - 2 ] [ x  ] == 0 and set[ y - 3 ][ x ] == 0:
						anw [ y - 2 ][ x ] += 1
						anw [ y - 3 ][ x ] += 1
					if y - 3 >= low_edge and set[ y - 1] [ x ] == 0 and set[ y - 2 ] [ x ] == flag and set[ y - 3 ][ x ] == 0:
						anw [ y - 1][ x ] += 1
						anw [ y - 3][ x ] += 1

				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==rflag:
					if  x - 3 >= low_edge and y - 3 >= low_edge:
						if  set[ y - 1 ][ x - 1 ] == flag and set[ y - 2 ][ x - 2 ] ==0 and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 2 ][ x - 2 ] += 1
							anw [ y - 3 ][ x - 3 ] += 1
						if  set[ y - 1 ][ x - 1 ] == 0 and set[ y - 2 ][ x - 2 ] == flag and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 1 ][ x - 1 ] += 1
							anw [ y - 3 ][ x - 3 ] += 1


				#right_up

				if x - 1 >= low_edge - 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x - 1 ] ==rflag:
					if x + 3 <= high_edge and  y - 3 >= low_edge :
						if  set[ y - 1 ][ x + 1 ] == flag and set[ y - 2 ][ x + 2 ] ==0 and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 2 ][ x + 2 ] += 1
							anw [ y - 3 ][ x + 3 ] += 1
						if  set[ y - 1 ][ x + 1 ] == 0 and set[ y - 2 ][ x + 2 ] == flag and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 1 ][ x + 1 ] += 1
							anw [ y - 3 ][ x + 3 ] += 1


				#right_down
				if x - 1 >= low_edge - 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x - 1 ] ==rflag:
					if x + 3 <= high_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x + 1 ] == flag and set[ y + 2 ][ x + 2 ] ==0 and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 2 ][ x + 2 ]+= 1
							anw [ y + 3 ][ x + 3 ]+= 1
						if  set[ y + 1 ][ x + 1 ] == 0 and set[ y + 2 ][ x + 2 ] == flag and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 1 ][ x + 1 ] += 1
							anw [ y + 3 ][ x + 3 ] += 1


				#left_down
				if x + 1 <= high_edge + 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x + 1 ] ==rflag:
					if x - 3>= low_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x - 1 ] == flag and set[ y + 2 ][ x - 2 ] ==0 and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 2 ][ x - 2 ] += 1
							anw [ y + 3 ][ x - 3 ] += 1
						if  set[ y + 1 ][ x - 1 ] == 0 and set[ y + 2 ][ x - 2 ] == flag and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 1 ][ x - 1 ] += 1
							anw [ y + 3 ][ x - 3 ] += 1

	return Return_nine_Num_Filter(anw,filter)

def evaluate_nine_alive_three(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 7
	low_edge = 1
	anw = [[0 for i in range(9)] for j in range(9)]
	for y in range(9):
		for x in range(9):
			if set[ y ][ x ] == flag :
				#right
				if x - 1 >= low_edge -1 and set [ y ][ x - 1 ] == 0 :  
					
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == flag and set[ y ] [ x + 2 ] == 0 and set[ y ][ x + 3] == 0:
						anw [ y ][ x + 2 ]+= 1
						if x + 4 <= high_edge + 1 and set[y ] [x + 4 ] ==0:
							anw [ y ][ x + 3 ]+= 1
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == 0 and set[ y ] [ x + 2 ] == flag and set[ y ][ x + 3] == 0:
						anw [ y ][ x + 1 ]+= 1
						if x + 4 <= high_edge + 1 and set[y ] [x + 4 ] ==0:
							anw [ y ][ x + 3 ]+= 1
					if x + 3 <= high_edge and set[ y ] [ x + 1 ] == 0 and set[ y ] [ x + 2 ] == 0 and set[ y ][ x + 3] == flag and x + 4 <= high_edge + 1 and set[y ] [x + 4 ] ==0:
						anw [ y ][ x + 1 ]+= 1

				#left
				if x + 1 <= high_edge  + 1 and set [ y ][ x + 1 ] == 0 :  
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == flag and set[ y ] [ x - 2 ] == 0 and set[ y ][ x - 3] == 0:
						anw [ y ][ x - 2 ]+= 1
						if x - 4 >= low_edge - 1 and set[ y ][ x - 4 ] == 0:
							anw [ y ][ x - 3 ]+= 1
					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == 0 and set[ y ] [ x - 2 ] == flag and set[ y ][ x - 3] == 0:
						anw [ y ][ x - 1 ]+= 1
						if x - 4 >= low_edge - 1 and set[ y ][ x - 4 ] == 0:
							anw [ y ][ x - 3 ] += 1

					if x - 3 >= low_edge and set[ y ] [ x - 1 ] == 0 and set[ y ] [ x - 2 ] == 0 and set[ y ][ x - 3] == flag and x - 4 >= low_edge - 1 and set[ y ][ x - 4 ] == 0:
						anw [ y ][ x - 1 ] += 1
				#up
				if y - 1 >= low_edge -1 and set [ y - 1 ][ x ] == 0 :  
					if y + 3 <= high_edge and set[ y + 1  ] [ x  ] == flag and set[ y + 2 ] [ x  ] == 0 and set[ y + 3 ][ x ] == 0:
						anw [ y + 2 ][ x ] += 1
						if y + 4 <=high_edge + 1 and set [ y + 4 ] [ x ] ==0:
							anw [ y + 3 ][ x ] += 1
					if y + 3 <= high_edge and set[ y + 1] [ x ] == 0 and set[ y + 2 ] [ x ] == flag and set[ y + 3 ][ x ] == 0:
						anw [ y  + 1][ x ] += 1
						if y + 4 <=high_edge + 1 and set [ y + 4 ] [ x ] ==0:
							anw [ y + 3 ][ x ] += 1
					if y + 3 <= high_edge and set[ y + 1] [ x ] == 0 and set[ y + 2 ] [ x ] == 0  and set[ y + 3 ][ x ] == flag and y + 4 <=high_edge + 1 and set [ y + 4 ] [ x ] ==0:
						anw [ y  + 1][ x ] += 1
				#down
				if y + 1 <= high_edge  + 1 and set [ y + 1 ][ x ] == 0 :  
					if y - 3 >= low_edge and set[ y - 1  ] [ x  ] == flag and set[ y - 2 ] [ x  ] == 0 and set[ y - 3 ][ x ] == 0:
						anw [ y - 2 ][ x ] += 1
						if y - 4 >=low_edge - 1 and set[ y - 4 ] [ x ] ==0 :
							anw [ y - 3 ][ x ] += 1
					if y - 3 >= low_edge and set[ y - 1] [ x ] == 0 and set[ y - 2 ] [ x ] == flag and set[ y - 3 ][ x ] == 0:
						anw [ y - 1][ x ] += 1
						if y-4 >= low_edge - 1 and set[ y - 4 ] [ x ] ==0 :
							anw [ y - 3][ x ] += 1
					if y - 3 >= low_edge and set[ y - 1] [ x ] == 0 and set[ y - 2 ] [ x ] == 0 and set[ y - 3 ][ x ] == flag and y-4 >= low_edge - 1 and set[ y - 4 ] [ x ] ==0:
						anw [ y - 1][ x ] += 1

				#left_up
				if x + 1 <= high_edge + 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x + 1 ] ==0:
					if  x - 3 >= low_edge and y - 3 >= low_edge:
						if  set[ y - 1 ][ x - 1 ] == flag and set[ y - 2 ][ x - 2 ] ==0 and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 2 ][ x - 2 ] += 1
							if y - 4 >=low_edge - 1 and x - 4 >= low_edge - 1  and set[ x - 4  ][ y - 4] ==0:
								anw [ y - 3 ][ x - 3 ] += 1
						if  set[ y - 1 ][ x - 1 ] == 0 and set[ y - 2 ][ x - 2 ] == flag and set[ y - 3 ][ x - 3 ] == 0:
							anw [ y - 1 ][ x - 1 ] += 1
							if y - 4 >=low_edge - 1 and x - 4 >= low_edge  - 1and set[ x - 4  ][ y - 4] ==0:
								anw [ y - 3 ][ x - 3 ] += 1
						if  set[ y - 1 ][ x - 1 ] == 0 and set[ y - 2 ][ x - 2 ] == 0 and set[ y - 3 ][ x - 3 ] == flag and y - 4 >=low_edge - 1 and x - 4 >= low_edge  - 1and set[ x - 4  ][ y - 4] ==0:
							anw [ y - 1 ][ x - 1 ] += 1


				#right_up

				if x - 1 >= low_edge - 1 and y + 1 <= high_edge + 1 and set[ y + 1 ] [ x - 1 ] ==0:
					if x + 3 <= high_edge and  y - 3 >= low_edge :
						if  set[ y - 1 ][ x + 1 ] == flag and set[ y - 2 ][ x + 2 ] ==0 and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 2 ][ x + 2 ] += 1
							if y - 4 >=low_edge - 1 and x + 4 <=high_edge + 1 and set [ y - 4][x + 4 ] ==0:
								anw [ y - 3 ][ x + 3 ] += 1
						if  set[ y - 1 ][ x + 1 ] == 0 and set[ y - 2 ][ x + 2 ] == flag and set[ y - 3 ][ x + 3 ] == 0:
							anw [ y - 1 ][ x + 1 ] += 1
							if y - 4 >=low_edge - 1 and x + 4 <=high_edge + 1 and set [ y - 4][x + 4 ] ==0:
								anw [ y - 3 ][ x + 3 ] += 1
						if  set[ y - 1 ][ x + 1 ] == 0 and set[ y - 2 ][ x + 2 ] == 0 and set[ y - 3 ][ x + 3 ] == flag and y - 4 >=low_edge - 1 and x + 4 <=high_edge + 1 and set [ y - 4][x + 4 ] ==0:
							anw [ y - 1 ][ x + 1 ] += 1


				#right_down
				if x - 1 >= low_edge - 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x - 1 ] ==0:
					if x + 3 <= high_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x + 1 ] == flag and set[ y + 2 ][ x + 2 ] ==0 and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 2 ][ x + 2 ] += 1
							if y + 4 <=high_edge + 1 and x + 4 <= high_edge + 1 and set[ y + 4] [x  + 4] ==0:
								anw [ y + 3 ][ x + 3 ] += 1
						if  set[ y + 1 ][ x + 1 ] == 0 and set[ y + 2 ][ x + 2 ] == flag and set[ y + 3 ][ x + 3 ] == 0:
							anw [ y + 1 ][ x + 1 ] += 1
							if y + 4 <=high_edge + 1 and x + 4 <= high_edge + 1 and set[ y + 4] [x  + 4] ==0:
								anw [ y + 3 ][ x + 3 ] += 1
						if  set[ y + 1 ][ x + 1 ] == 0 and set[ y + 2 ][ x + 2 ] == 0 and set[ y + 3 ][ x + 3 ] == flag and y + 4 <=high_edge + 1 and x + 4 <= high_edge + 1 and set[ y + 4] [x  + 4] ==0:
							anw [ y + 1 ][ x + 1 ] += 1


				#left_down
				if x + 1 <= high_edge + 1 and y - 1 >=  low_edge - 1 and set[ y - 1 ] [ x + 1 ] ==0:
					if x - 3>= low_edge and  y + 3 <= high_edge :
						if  set[ y + 1 ][ x - 1 ] == flag and set[ y + 2 ][ x - 2 ] ==0 and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 2 ][ x - 2 ] += 1
							if y + 4 <=high_edge+ 1  and x - 4 >=low_edge - 1 and set [y + 4][ x - 4 ] ==0:
								anw [ y + 3 ][ x - 3 ] += 1
						if  set[ y + 1 ][ x - 1 ] == 0 and set[ y + 2 ][ x - 2 ] == flag and set[ y + 3 ][ x - 3 ] == 0:
							anw [ y + 1 ][ x - 1 ]+= 1
							if y + 4 <=high_edge+ 1  and x - 4 >=low_edge- 1  and set [y + 4][ x - 4 ] ==0:
								anw [ y + 3 ][ x - 3 ]+= 1
						if  set[ y + 1 ][ x - 1 ] == 0 and set[ y + 2 ][ x - 2 ] == 0 and set[ y + 3 ][ x - 3 ] == flag and  + 4 <=high_edge+ 1  and x - 4 >=low_edge- 1  and set [y + 4][ x - 4 ] ==0:
							anw [ y + 1 ][ x - 1 ] += 1


			


				

				
	return Return_nine_Num_Filter(anw,filter)

def evaluate_nine_dead_four (set_x,color,filter):
	re_set = [[0 for x in range(9)] for y in range(9)]
	for y in range(9):
		for x in range(9):
			if set_x[x][y] != 0 and set_x[x][y] != color:
				#XOOOA_
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+4][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-4][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+4] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-4] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+4][y+4] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-4][y-4] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-4][y+4] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+4][y-4] += 1
				#XOOO_A
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XOOAO_
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+3][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-3][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+3] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-3] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+3][y+3] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-3][y-3] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-3][y+3] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+3][y-3] += 1 
				#XOO_OA
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1 
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XAOOO_
				if x+5 < 9 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+1][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-1][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+1] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-1] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+1][y+1] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-1][y-1] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-1][y+1] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+1][y-1] += 1
				#X_OOOA
				if x+5 < 9 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XOAOO_
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+2][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-2][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+2] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-2] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+2][y+2] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-2][y-2] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-2][y+2] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+2][y-2] += 1
				#XO_OOA
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
	return Return_nine_Num_Filter(re_set,filter)		

def evaluate_nine_alive_four (set_x,color,filter) :
	re_set = [[0 for x in range(9)] for y in range(9)]
	for y in range(9):
		for x in range(9):
			if set_x[x][y] == 0:
				#_OOO__
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+4][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-4][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+4] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-4] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+4][y+4] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-4][y-4] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-4][y+4] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+4][y-4] += 1
				#_OO_O_
				if x+5 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+3][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-3][y] += 1
				elif y+5 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+3] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-3] += 1
				elif x+5 < 9 and y+5 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+3][y+3] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-3][y-3] += 1
				elif x-5 >= 0 and y+5 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-3][y+3] += 1
				elif x+5 < 9 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+3][y-3] += 1
	return Return_nine_Num_Filter(re_set,filter)	

def evaluate_nine_five (set_x,color):
	re_set = [[0 for x in range(9)] for y in range(9)]
	for y in range(9):
		for x in range(9):
			if set_x[x][y] == color:
				#OOOO_
				if x+4 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0:
					re_set[x+4][y] += 1
				elif x-4 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0:
					re_set[x-4][y] += 1
				elif y+4 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0:
					re_set[x][y+4] += 1
				elif y-4 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0:
					re_set[x][y-4] += 1
				elif x+4 < 9 and y+4 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0:
					re_set[x+4][y+4] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0:
					re_set[x-4][y-4] += 1
				elif x-4 >= 0 and y+4 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0:
					re_set[x-4][y+4] += 1
				elif x+4 < 9 and y-4 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0:
					re_set[x+4][y-4] += 1
				#O_OOO
				if x+4 < 9 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color:
					re_set[x+1][y] += 1
				elif x-4 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color:
					re_set[x-1][y] += 1
				elif y+4 < 9 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color:
					re_set[x][y+1] += 1
				elif y-4 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color:
					re_set[x][y-1] += 1
				elif x+4 < 9 and y+4 < 9 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color:
					re_set[x+1][y+1] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color:
					re_set[x-1][y-1] += 1
				elif x-4 >= 0 and y+4 < 9 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color:
					re_set[x-1][y+1] += 1
				elif x+4 < 9 and y-4 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color:
					re_set[x+1][y-1] += 1
				#OO_OO
				if x+4 < 9 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color:
					re_set[x+2][y] += 1 
				elif x-4 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color:
					re_set[x-2][y] += 1
				elif y+4 < 9 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color:
					re_set[x][y+2] += 1
				elif y-4 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color:
					re_set[x][y-2] += 1
				elif x+4 < 9 and y+4 < 9 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color:
					re_set[x+2][y+2] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color:
					re_set[x-2][y-2] += 1
				elif x-4 >= 0 and y+4 < 9 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color:
					re_set[x-2][y+2] += 1
				elif x+4 < 9 and y-4 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color:
					re_set[x+2][y-2] += 1
	return  Return_Num_Filter(re_set,1)

def evaluate_nine_alive_three_dead_four(set , color):
	three = evaluate_nine_alive_three(set,color,1)
	four = evaluate_nine_dead_four(set,color , 1)
	anw = [[0 for x in range(9)] for y in range(9)]
	for i in range(9):
		for j in range(9):
			if three[i][j]==1 and four[i][j]==1:
				anw [i][j] =1

	return anw