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


