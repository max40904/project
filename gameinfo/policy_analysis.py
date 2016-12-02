
		

def evaluate_lib_five(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == flag :
				for i in range(1,5):
					if y - i >= 0 and set[y - i][ x ] ==0:
						anw [ y - i ][ x ] = 1
					else:
						break
				for i in range(1,5):

					if y + i <=14 and set[y + i][ x ] ==0:
						anw [ y + i ][ x ] = 1
					else:
						break
				for i in range(1,5):
					if x + i <= 14 and set[y ][ x + i ] ==0:
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
					if x + i <= 14 and y - i >=0  and set[y - i][ x + i ] ==0:
						anw [ y - i] [x + i] =1
					else:
						break
				for i in range(1,5):
					if x -i >= 0 and y + i <= 14 and set[y + i][ x - i ] ==0:
						anw [y + i][ x - i ] = 1
					else:
						break
				for i in range(1,5):
					if x + i <= 14 and y +i <= 14  and set[y + i][ x + i ] ==0:
						anw [ y + i] [x + i] = 1
					else:
						break
	return anw


def evaluate_dead_two(set, flag , filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
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


	return Return_Num_Filter(anw,filter)


def evaluate_alive_two(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
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


				

				
	return Return_Num_Filter(anw,filter)


def evaluate_dead_three(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
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

	return Return_Num_Filter(anw,filter)

def evaluate_alive_three(set,flag,filter):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	high_edge = 13
	low_edge = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
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


	for y in range(15):
		for x in range(15):
			if set[x][y] != 0 and set[x][y] != flag:
				
				#XOAOO_
				if x+5 < 15 and set[x+1][y] == flag and set[x+2][y] == 0 and set[x+3][y] == flag and set[x+4][y] == flag and set[x+5][y] == 0:
					anw[x+2][y] -= 1
				elif x-5 >= 0 and set[x-1][y] == flag and set[x-2][y] == 0 and set[x-3][y] == flag and set[x-4][y] == flag and set[x-5][y] == 0:
					anw[x-2][y] -= 1
				elif y+5 < 15 and set[x][y+1] == flag and set[x][y+2] == 0 and set[x][y+3] == flag and set[x][y+4] == flag and set[x][y+5] == 0:
					anw[x][y+2] -= 1
				elif y-5 >= 0 and set[x][y-1] == flag and set[x][y-2] == 0 and set[x][y-3] == flag and set[x][y-4] == flag and set[x][y-5] == 0:
					anw[x][y-2] -= 1
				elif x+5 < 15 and y+5 < 15 and set[x+1][y+1] == flag and set[x+2][y+2] == 0 and set[x+3][y+3] == flag and set[x+4][y+4] == flag and set[x+5][y+5] == 0:
					anw[x+2][y+2] -= 1
				elif x-5 >= 0 and y-5 >= 0 and set[x-1][y-1] == flag and set[x-2][y-2] == 0 and set[x-3][y-3] == flag and set[x-4][y-4] == flag and set[x-5][y-5] == 0:
					anw[x-2][y-2] -= 1
				elif x-5 >= 0 and y+5 < 15 and set[x-1][y+1] == flag and set[x-2][y+2] == 0 and set[x-3][y+3] == flag and set[x-4][y+4] == flag and set[x-5][y+5] == 0:
					anw[x-2][y+2] -= 1
				elif x+5 < 15 and y-5 >= 0 and set[x+1][y-1] == flag and set[x+2][y-2] == 0 and set[x+3][y-3] == flag and set[x+4][y-4] == flag and set[x+5][y-5] == 0:
					anw[x+2][y-2] -= 1
				#XO_OOA
				if x+5 < 15 and set[x+1][y] == flag and set[x+2][y] == 0 and set[x+3][y] == flag and set[x+4][y] == flag and set[x+5][y] == 0:
					anw[x+5][y] -= 1
				elif x-5 >= 0 and set[x-1][y] == flag and set[x-2][y] == 0 and set[x-3][y] == flag and set[x-4][y] == flag and set[x-5][y] == 0:
					anw[x-5][y] -= 1
				elif y+5 < 15 and set[x][y+1] == flag and set[x][y+2] == 0 and set[x][y+3] == flag and set[x][y+4] == flag and set[x][y+5] == 0:
					anw[x][y+5] -= 1
				elif y-5 >= 0 and set[x][y-1] == flag and set[x][y-2] == 0 and set[x][y-3] == flag and set[x][y-4] == flag and set[x][y-5] == 0:
					anw[x][y-5] -= 1
				elif x+5 < 15 and y+5 < 15 and set[x+1][y+1] == flag and set[x+2][y+2] == 0 and set[x+3][y+3] == flag and set[x+4][y+4] == flag and set[x+5][y+5] == 0:
					anw[x+5][y+5] -= 1
				elif x-5 >= 0 and y-5 >= 0 and set[x-1][y-1] == flag and set[x-2][y-2] == 0 and set[x-3][y-3] == flag and set[x-4][y-4] == flag and set[x-5][y-5] == 0:
					anw[x-5][y-5] -= 1
				elif x-5 >= 0 and y+5 < 15 and set[x-1][y+1] == flag and set[x-2][y+2] == 0 and set[x-3][y+3] == flag and set[x-4][y+4] == flag and set[x-5][y+5] == 0:
					anw[x-5][y+5] -= 1
				elif x+5 < 15 and y-5 >= 0 and set[x+1][y-1] == flag and set[x+2][y-2] == 0 and set[x+3][y-3] == flag and set[x+4][y-4] == flag and set[x+5][y-5] == 0:
					anw[x+5][y-5] -= 1


			


				

				
	return Return_Num_Filter(anw,filter)

def evaluate_dead_four (set_x,color,filter):

	re_set = [[0 for x in range(15)] for y in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[x][y] != 0 and set_x[x][y] != color:
				#XOOOA_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+4][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-4][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+4] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-4] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+4][y+4] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-4][y-4] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-4][y+4] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+4][y-4] += 1
				#XOOO_A
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XOOAO_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+3][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-3][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+3] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-3] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+3][y+3] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-3][y-3] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-3][y+3] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+3][y-3] += 1 
				#XOO_OA
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1 
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XAOOO_
				if x+5 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+1][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-1][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+1] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-1] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+1][y+1] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-1][y-1] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-1][y+1] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+1][y-1] += 1
				#X_OOOA
				if x+5 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
				#XOAOO_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+2][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-2][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+2] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-2] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+2][y+2] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-2][y-2] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-2][y+2] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+2][y-2] += 1
				#XO_OOA
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] += 1
			if set_x[x][y] == color:
				#0_OA0
				if x+5 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color :
					re_set[x+3][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color:
					re_set[x-3][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color:
					re_set[x][y+3] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color:
					re_set[x][y-3] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color:
					re_set[x+3][y+3] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color :
					re_set[x-3][y-3] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color :
					re_set[x-3][y+3] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color :
					re_set[x+3][y-3] += 1
				#0__O0
				if x+5 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color :
					re_set[x+2][y] += 1
					re_set[x+1][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color:
					re_set[x-2][y] += 1
					re_set[x-1][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color:
					re_set[x][y+2] += 1
					re_set[x][y+1] += 1
				elif y-5 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color:
					re_set[x][y-2] += 1
					re_set[x][y-1] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color:
					re_set[x+1][y+1] += 1
					re_set[x+2][y+2] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color :
					re_set[x-2][y-2] += 1
					re_set[x-1][y-1] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color :
					re_set[x-1][y+1] += 1
					re_set[x-2][y+2] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color :
					re_set[x+1][y-1] += 1
					re_set[x+2][y-2] += 1
	return Return_Num_Filter(re_set,filter)		
def evaluate_defense_four (set_x,color,filter):
	re_set = [[0 for x in range(15)] for y in range(15)]
	for y in range(15):
		for x in range(15):

			if set_x[x][y] == 0:
				#_OOO__
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+4][y] += 1
					re_set[x][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-4][y] += 1
					re_set[x][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+4] += 1
					re_set[x][y] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-4] += 1
					re_set[x][y] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+4][y+4] += 1
					re_set[x][y] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-4][y-4] += 1
					re_set[x][y] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-4][y+4] += 1
					re_set[x][y] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+4][y-4] += 1
					re_set[x][y] += 1

				#_OO_O_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+3][y] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-3][y] += 1
					re_set[x][y] +=1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+3] += 1
					re_set[x][y] +=1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-3] += 1
					re_set[x][y] +=1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+3][y+3] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-3][y-3] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-3][y+3] += 1
					re_set[x][y] +=1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+3][y-3] += 1
					re_set[x][y] +=1
				#_O_0O_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+2][y] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-2][y] += 1
					re_set[x][y] +=1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+2] += 1
					re_set[x][y] +=1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-2] += 1
					re_set[x][y] +=1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+2][y+2] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-2][y-2] += 1
					re_set[x][y] +=1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-2][y+2] += 1
					re_set[x][y] +=1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+2][y-2] += 1
					re_set[x][y] +=1
	
	
	return Return_Num_Filter(re_set,filter)	






def evaluate_alive_four (set_x,color,filter) :
	re_set = [[0 for x in range(15)] for y in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == 0:
				#_OOO__
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0 and set_x[x+5][y] == 0:
					re_set[x+4][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0 and set_x[x-5][y] == 0:
					re_set[x-4][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0 and set_x[x][y+5] == 0:
					re_set[x][y+4] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0 and set_x[x][y-5] == 0:
					re_set[x][y-4] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0 and set_x[x+5][y+5] == 0:
					re_set[x+4][y+4] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0 and set_x[x-5][y-5] == 0:
					re_set[x-4][y-4] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0 and set_x[x-5][y+5] == 0:
					re_set[x-4][y+4] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0 and set_x[x+5][y-5] == 0:
					re_set[x+4][y-4] += 1
				#_OO_O_
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0 and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+3][y] += 1
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0 and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-3][y] += 1
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0 and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+3] += 1
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0 and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-3] += 1
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0 and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+3][y+3] += 1
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0 and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-3][y-3] += 1
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0 and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-3][y+3] += 1
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0 and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+3][y-3] += 1
	return Return_Num_Filter(re_set,filter)	


def evaluate_five (set_x,color):
	re_set = [[0 for x in range(15)] for y in range(15)]
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				#OOOO_
				if x+4 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0:
					re_set[x+4][y] += 1
				elif x-4 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0:
					re_set[x-4][y] += 1
				elif y+4 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0:
					re_set[x][y+4] += 1
				elif y-4 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0:
					re_set[x][y-4] += 1
				elif x+4 < 15 and y+4 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0:
					re_set[x+4][y+4] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0:
					re_set[x-4][y-4] += 1
				elif x-4 >= 0 and y+4 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0:
					re_set[x-4][y+4] += 1
				elif x+4 < 15 and y-4 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0:
					re_set[x+4][y-4] += 1
				#O_OOO
				if x+4 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color:
					re_set[x+1][y] += 1
				elif x-4 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color:
					re_set[x-1][y] += 1
				elif y+4 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color:
					re_set[x][y+1] += 1
				elif y-4 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color:
					re_set[x][y-1] += 1
				elif x+4 < 15 and y+4 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color:
					re_set[x+1][y+1] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color:
					re_set[x-1][y-1] += 1
				elif x-4 >= 0 and y+4 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color:
					re_set[x-1][y+1] += 1
				elif x+4 < 15 and y-4 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color:
					re_set[x+1][y-1] += 1
				#OO_OO
				if x+4 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color and set_x[x+4][y] == color:
					re_set[x+2][y] += 1 
				elif x-4 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color and set_x[x-4][y] == color:
					re_set[x-2][y] += 1
				elif y+4 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color and set_x[x][y+4] == color:
					re_set[x][y+2] += 1
				elif y-4 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color and set_x[x][y-4] == color:
					re_set[x][y-2] += 1
				elif x+4 < 15 and y+4 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color:
					re_set[x+2][y+2] += 1
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color:
					re_set[x-2][y-2] += 1
				elif x-4 >= 0 and y+4 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color:
					re_set[x-2][y+2] += 1
				elif x+4 < 15 and y-4 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color:
					re_set[x+2][y-2] += 1
	return Return_Num_Filter(re_set,1)

def evaluate_alive_three_dead_four(set , color):
	three = evaluate_alive_three(set,color,1)
	four = evaluate_dead_four(set,color , 1)
	anw = [[0 for x in range(15)] for y in range(15)]
	for i in range(15):
		for j in range(15):
			if three[i][j]==1 and four[i][j]==1:
				anw [i][j] =1


	for x in range(15):
		for y in range(15):
			if set[x][y] == color:
				#0_OA0
				if x+5 < 15 and set[x+1][y] == 0 and set[x+2][y] == color and set[x+3][y] == 0 and set[x+4][y] == color and set[x+5][y] == 0  :
					anw[x+3][y] = 0
				elif x-5 >= 0 and set[x-1][y] == 0 and set[x-2][y] == color and set[x-3][y] == 0 and set[x-4][y] == color and set[x-5][y] == 0:
	
					anw[x-3][y] = 0
				elif y+5 < 15 and set[x][y+1] == 0 and set[x][y+2] == color and set[x][y+3] == 0 and set[x][y+4] == color and set[x][y+5] == 0:
					anw[x][y+3] = 0
				elif y-5 >= 0 and set[x][y-1] == 0 and set[x][y-2] == color and set[x][y-3] == 0 and set[x][y-4] == color and set[x][y-5] == 0:
					anw[x][y-3]= 0
				elif x+5 < 15 and y+5 < 15 and set[x+1][y+1] == 0 and set[x+2][y+2] == color and set[x+3][y+3] == 0 and set[x+4][y+4] == color and set[x+5][y+5] == 0:
					anw[x+3][y+3] = 0
				elif x-5 >= 0 and y-5 >= 0 and set[x-1][y-1] == 0 and set[x-2][y-2] == color and set[x-3][y-3] == 0 and set[x-4][y-4] == color  and set[x-5][y-5] == 0:
					anw[x-3][y-3] = 0
				elif x-5 >= 0 and y+5 < 15 and set[x-1][y+1] == 0 and set[x-2][y+2] == color and set[x-3][y+3] == 0 and set[x-4][y+4] == color and set[x-5][y+5] == 0:
					anw[x-3][y+3] = 0
				elif x+5 < 15 and y-5 >= 0 and set[x+1][y-1] == 0 and set[x+2][y-2] == color and set[x+3][y-3] == 0 and set[x+4][y-4] == color and set[x+5][y-5] == 0:
					anw[x+3][y-3] = 0
				#0__O0
				if x+5 < 15 and set[x+1][y] == 0 and set[x+2][y] == 0 and set[x+3][y] == color and set[x+4][y] == color and set[x+5][y] == 0 :
					anw[x+2][y] = 0
	
				elif x-5 >= 0 and set[x-1][y] == 0 and set[x-2][y] == 0 and set[x-3][y] == color and set[x-4][y] == color and set[x-5][y] == 0:
					anw[x-2][y] = 0

				elif y+5 < 15 and set[x][y+1] == 0 and set[x][y+2] == 0 and set[x][y+3] == color and set[x][y+4] == color and set[x][y+5] == 0:
					anw[x][y+2]= 0
				elif y-5 >= 0 and set[x][y-1] == 0 and set[x][y-2] == 0 and set[x][y-3] == color and set[x][y-4] == color and set[x][y-5] ==0:
					anw[x][y-2] = 0
	
				elif x+5 < 15 and y+5 < 15 and set[x+1][y+1] == 0 and set[x+2][y+2] == 0 and set[x+3][y+3] == color and set[x+4][y+4] == color and set[x+5][y+5] == 0:
		
					anw[x+2][y+2] = 0
				elif x-5 >= 0 and y-5 >= 0 and set[x-1][y-1] == 0 and set[x-2][y-2] == 0 and set[x-3][y-3] == color and set[x-4][y-4] == color and set[x-5][y-5] == 0:
					anw[x-2][y-2] = 0

				elif x-5 >= 0 and y+5 < 15 and set[x-1][y+1] == 0 and set[x-2][y+2] == 0 and set[x-3][y+3] == color and set[x-4][y+4] == color and set[x-5][y+5] == 0:
			
					anw[x-2][y+2] = 0
				elif x+5 < 15 and y-5 >= 0 and set[x+1][y-1] == 0 and set[x+2][y-2] == 0 and set[x+3][y-3] == color and set[x+4][y-4] == color and set[x+5][y-5] == 0:
				
					anw[x+2][y-2] = 0
	



	return anw


def evaluate_self(set,flag):
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == flag:
				anw[y][x] = 1
	return anw

def evaluate_square_three(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == flag:
				for i in range(-2,3):
					for j in range(-2,3):
						if x + j <=14 and x + j >=0 and y + i >= 0 and y + i <= 14 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def evaluate_square_two(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == flag:
				for i in range(-1,2):
					for j in range(-1,2):
						if x + j <=14 and x + j >=0 and y + i >= 0 and y + i <= 14 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def evaluate_square_four(set,flag):
	rflag = 0.5
	if flag == 0.5:
		rflag = 1
	anw = [[0 for i in range(15)] for j in range(15)]
	for y in range(15):
		for x in range(15):
			if set[y][x] == flag:
				for i in range(-3,4):
					for j in range(-3,4):
						if x + j <=14 and x + j >=0 and y + i >= 0 and y + i <= 14 and set [ y + i ][ x + j ]==0:
							anw [ y + i ][ x + j ] = 1  



	return anw

def Return_Num_Filter(set, limit):
	anws = [[0 for i in range(15)] for j in range(15)]
	for i in range(15):
		for j in range(15):
			if set[i][j]>=limit:
				anws[i][j] = 1
	return anws

def check_three(array,r,c,piece):
	if array[r][c] != 0:
		return False

	array[r][c] = piece
	count = 0



	

	for i in range (5):
		if r-i>=0 and r-i+4<15 and c>=0 and c<15:
			if array[r-i][c]==0  and array[r-i+1][c]==piece and array[r-i+2][c]==piece and array[r-i+3][c]==piece and array[r-i+4][c]==0:
				count += 1

	for i in range (5):
		if r-i>=0 and r-i+4<15 and c-i>=0 and c-i+4<15:
			if array[r-i][c-i]==0  and array[r-i+1][c-i+1]==piece and array[r-i+2][c-i+2]==piece and array[r-i+3][c-i+3]==piece and array[r-i+4][c-i+4]==0:
				count += 1

	for i in range (5):
		if r>=0 and r<15 and c-i>=0 and c-i+4<15:
			if array[r][c-i]==0  and array[r][c-i+1]==piece and array[r][c-i+2]==piece and array[r][c-i+3]==piece and array[r][c-i+4]==0:
				count += 1

	for i in range (5):
		if r+i-4>=0 and r+i<15 and c-i>=0 and c-i+4<15:
			if array[r+i][c-i]==0  and array[r+i-1][c-i+1]==piece and array[r+i-2][c-i+2]==piece and array[r+i-3][c-i+3]==piece and array[r+i-4][c-i+4]==0:
				count += 1
	

	
	for i in range (4):
		if r-i-1>=0 and r-i+4<15 and c>=0 and c<15:
			if array[r-i-1][c]==0  and array[r-i][c]==piece and array[r-i+1][c]==piece and array[r-i+2][c]==0 and array[r-i+3][c]==piece and array[r-i+4][c]==0:
				count += 1
			if array[r-i-1][c]==0  and array[r-i][c]==piece and array[r-i+1][c]==0 and array[r-i+2][c]==piece and array[r-i+3][c]==piece and array[r-i+4][c]==0:
				count += 1

	for i in range (4):
		if r-i-1>=0 and r-i+4<15 and c-i-1>=0 and c-i+4<15:
			if array[r-i-1][c-i-1]==0  and array[r-i][c-i]==piece and array[r-i+1][c-i+1]==piece and array[r-i+2][c-i+2]==0 and array[r-i+3][c-i+3]==piece and array[r-i+4][c-i+4]==0:
				count += 1
			if array[r-i-1][c-i-1]==0  and array[r-i][c-i]==piece and array[r-i+1][c-i+1]==0 and array[r-i+2][c-i+2]==piece and array[r-i+3][c-i+3]==piece and array[r-i+4][c-i+4]==0:
				count += 1

	for i in range (4):
		if r>=0 and r<15 and c-i-1>=0 and c-i+4<15:
			if array[r][c-i-1]==0 and array[r][c-i]==piece  and array[r][c-i+1]==piece and array[r][c-i+2]==0 and array[r][c-i+3]==piece and array[r][c-i+4]==0:
				count += 1
			if array[r][c-i-1]==0 and array[r][c-i]==piece  and array[r][c-i+1]==0 and array[r][c-i+2]==piece and array[r][c-i+3]==piece and array[r][c-i+4]==0:
				count += 1

	for i in range (4):
		if r+i-4>=0 and r+i+1<15 and c-i-1>=0 and c-i+4<15:
			if array[r+i+1][c-i-1]==0  and array[r+i][c-i]==piece  and array[r+i-1][c-i+1]==piece and array[r+i-2][c-i+2]==0 and array[r+i-3][c-i+3]==piece and array[r+i-4][c-i+4]==0:
				count += 1
			if array[r+i+1][c-i-1]==0  and array[r+i][c-i]==piece  and array[r+i-1][c-i+1]==0 and array[r+i-2][c-i+2]==piece and array[r+i-3][c-i+3]==piece and array[r+i-4][c-i+4]==0:
				count += 1	


	array[r][c] = 0
	if count > 1:

		return False
	return True


def evaluate_double_three(set,color):
	anw =  [[0 for i in range(15)] for j in range(15)]
	for i in range(15):
		for j in range(15):
			if (set[i][j]==0 and check_three(set,i,j,color)==False):
				anw [i][j] = 1

	return anw

