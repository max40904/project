from MongoDB import DataCenter

def initial():
	re_set = [[0 for x in range(15)] for y in range(15)]

def five_attack (set_x,color):
	initial()
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+4 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == 0:
					re_set[x+4][y] = color
				elif x-4 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == 0:
					re_set[x-4][y] = color
				elif y+4 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == 0:
					re_set[x][y+4] = color
				elif y-4 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == 0:
					re_set[x][y-4] = color
				elif x+4 < 15 and y+4 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == 0:
					re_set[x+4][y+4] = color
				elif x-4 >= 0 and y-4 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == 0:
					re_set[x-4][y-4] = color
				elif x-4 >= 0 and y+4 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == 0:
					re_set[x-4][y+4] = color
				elif x+4 < 15 and y-4 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == 0:
					re_set[x+4][y-4] = color
	return re_set

def five_defend (set_x,color):
	initial()
	if color == 1:
		color_temp == 0.5;
	elif color == 0.5:
		color_temp == 1;
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+5 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == color and set_x[x+4][y] == color and set_x[x+5][y] == 0:
					re_set[x+5][y] = color_temp
				elif x-5 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == color and set_x[x-4][y] == color and set_x[x-5][y] == 0:
					re_set[x-5][y] = color_temp
				elif y+5 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == color and set_x[x][y+4] == color and set_x[x][y+5] == 0:
					re_set[x][y+5] = color_temp
				elif y-5 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == color and set_x[x][y-4] == color and set_x[x][y-5] == 0:
					re_set[x][y-5] = color_temp
				elif x+5 < 15 and y+5 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color and set_x[x+4][y+4] == color and set_x[x+5][y+5] == 0:
					re_set[x+5][y+5] = color_temp
				elif x-5 >= 0 and y-5 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color and set_x[x-4][y-4] == color and set_x[x-5][y-5] == 0:
					re_set[x-5][y-5] = color_temp
				elif x-5 >= 0 and y+5 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color and set_x[x-4][y+4] == color and set_x[x-5][y+5] == 0:
					re_set[x-5][y+5] = color_temp
				elif x+5 < 15 and y-5 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color and set_x[x+4][y-4] == color and set_x[x+5][y-5] == 0:
					re_set[x+5][y-5] = color_temp
	return re_set
	
def four_attack (set_x,color):
	initial()
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+3 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0:
					re_set[x+3][y] = color
				elif x-3 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0:
					re_set[x-3][y] = color
				elif y+3 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0:
					re_set[x][y+3] = color
				elif y-3 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0:
					re_set[x][y-3] = color
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0:
					re_set[x+3][y+3] = color
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0:
					re_set[x-3][y-3] = color
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0:
					re_set[x-3][y+3] = color
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0:
					re_set[x+3][y-3] = color
					
				elif x+3 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color:
					re_set[x+1][y] = color
				elif x-3 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color:
					re_set[x-1][y] = color
				elif y+3 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color:
					re_set[x][y+1] = color
				elif y-3 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color:
					re_set[x][y-1] = color
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color:
					re_set[x+1][y+1] = color
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color:
					re_set[x-1][y-1] = color
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color:
					re_set[x-1][y+1] = color
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color:
					re_set[x+1][y-1] = color
				
				elif x+3 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color:
					re_set[x+2][y] = color
				elif x-3 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color:
					re_set[x-2][y] = color
				elif y+3 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color:
					re_set[x][y+2] = color
				elif y-3 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color:
					re_set[x][y-2] = color
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color:
					re_set[x+2][y+2] = color
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color:
					re_set[x-2][y-2] = color
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color:
					re_set[x-2][y+2] = color
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color:
					re_set[x+2][y-2] = color
	return re_set
	
def four_defend (set_x,color):
	initial()
	if color == 1:
		color_temp == 0.5;
	elif color == 0.5:
		color_temp == 1;
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+3 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == color and set_x[x+3][y] == 0:
					re_set[x+3][y] = color_temp
				elif x-3 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == color and set_x[x-3][y] == 0:
					re_set[x-3][y] = color_temp
				elif y+3 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == color and set_x[x][y+3] == 0:
					re_set[x][y+3] = color_temp
				elif y-3 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == color and set_x[x][y-3] == 0:
					re_set[x][y-3] = color_temp
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == color and set_x[x+3][y+3] == 0:
					re_set[x+3][y+3] = color_temp
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == color and set_x[x-3][y-3] == 0:
					re_set[x-3][y-3] = color_temp
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == color and set_x[x-3][y+3] == 0:
					re_set[x-3][y+3] = color_temp
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == color and set_x[x+3][y-3] == 0:
					re_set[x+3][y-3] = color_temp
					
				elif x+3 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color and set_x[x+3][y] == color:
					re_set[x+1][y] = color_temp
				elif x-3 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color and set_x[x-3][y] == color:
					re_set[x-1][y] = color_temp
				elif y+3 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color and set_x[x][y+3] == color:
					re_set[x][y+1] = color_temp
				elif y-3 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color and set_x[x][y-3] == color:
					re_set[x][y-1] = color_temp
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color and set_x[x+3][y+3] == color:
					re_set[x+1][y+1] = color_temp
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color and set_x[x-3][y-3] == color:
					re_set[x-1][y-1] = color_temp
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color and set_x[x-3][y+3] == color:
					re_set[x-1][y+1] = color_temp
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color and set_x[x+3][y-3] == color:
					re_set[x+1][y-1] = color_temp
				
				elif x+3 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0 and set_x[x+3][y] == color:
					re_set[x+2][y] = color_temp
				elif x-3 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0 and set_x[x-3][y] == color:
					re_set[x-2][y] = color_temp
				elif y+3 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0 and set_x[x][y+3] == color:
					re_set[x][y+2] = color_temp
				elif y-3 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0 and set_x[x][y-3] == color:
					re_set[x][y-2] = color_temp
				elif x+3 < 15 and y+3 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0 and set_x[x+3][y+3] == color:
					re_set[x+2][y+2] = color_temp
				elif x-3 >= 0 and y-3 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0 and set_x[x-3][y-3] == color:
					re_set[x-2][y-2] = color_temp
				elif x-3 >= 0 and y+3 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0 and set_x[x-3][y+3] == color:
					re_set[x-2][y+2] = color_temp
				elif x+3 < 15 and y-3 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0 and set_x[x+3][y-3] == color:
					re_set[x+2][y-2] = color_temp
	return re_set

def three_attack (set_x,color):
	initial()
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+2 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0:
					re_set[x+2][y] = color
				elif x-2 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0:
					re_set[x-2][y] = color
				elif y+2 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0:
					re_set[x][y+2] = color
				elif y-2 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0:
					re_set[x][y-2] = color
				elif x+2 < 15 and y+2 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0:
					re_set[x+2][y+2] = color
				elif x-2 >= 0 and y-2 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0:
					re_set[x-2][y-2] = color
				elif x-2 >= 0 and y+2 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0:
					re_set[x-2][y+2] = color
				elif x+2 < 15 and y-2 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0:
					re_set[x+2][y-2] = color
					
				elif x+2 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color:
					re_set[x+1][y] = color
					if x-1 >= 0 and re_set[x-1][y] == 0:
						re_set[x-1][y] = color
					if x+3 < 15 and re_set[x+3][y] == 0:
						re_set[x+3][y] = color
				elif x-2 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color:
					re_set[x-1][y] = color
					if x+1 < 15 and re_set[x+1][y] == 0:
						re_set[x+1][y] = color
					if x-3 >= 0 and re_set[x-3][y] == 0:
						re_set[x-3][y] = color
				elif y+2 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color:
					re_set[x][y+1] = color
					if y-1 >= 0 and re_set[x][y-1] == 0:
						re_set[x][y-1] = color
					if y+3 < 15 and re_set[x][y+3] == 0:
						re_set[x][y+3] = color
				elif y-2 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color:
					re_set[x][y-1] = color
					if y+1 >= 0 and re_set[x][y+1] == 0:
						re_set[x][y+1] = color
					if y-3 < 15 and re_set[x][y-3] == 0:
						re_set[x][y-3] = color
				elif x+2 < 15 and y+2 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color:
					re_set[x+1][y+1] = color
					if x-1 >= 0 and y-1 >= 0 and re_set[x-1][y-1] == 0:
						re_set[x-1][y-1] = color
					if x+3 < 15 and y+3 < 15 and re_set[x+3][y+3] == 0:
						re_set[x+3][y+3] = color
				elif x-2 >= 0 and y-2 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color:
					re_set[x-1][y-1] = color
					if x+1 >= 0 and y+1 >= 0 and re_set[x+1][y+1] == 0:
						re_set[x+1][y+1] = color
					if x-3 < 15 and y-3 < 15 and re_set[x-3][y-3] == 0:
						re_set[x-3][y-3] = color
				elif x-2 >= 0 and y+2 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color:
					re_set[x-1][y+1] = color
					if x+1 >= 0 and y-1 >= 0 and re_set[x+1][y-1] == 0:
						re_set[x+1][y-1] = color
					if x-3 < 15 and y+3 < 15 and re_set[x-3][y+3] == 0:
						re_set[x-3][y+3] = color
				elif x+2 < 15 and y-2 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color:
					re_set[x+1][y-1] = color
					if x-1 >= 0 and y+1 >= 0 and re_set[x-1][y+1] == 0:
						re_set[x-1][y+1] = color
					if x+3 < 15 and y-3 < 15 and re_set[x+3][y-3] == 0:
						re_set[x+3][y-3] = color
	return re_set	
	
def three_defend (set_x,color):
	initial()
	if color == 1:
		color_temp == 0.5;
	elif color == 0.5:
		color_temp == 1;
	for y in range(15):
		for x in range(15):
			if set_x[x][y] == color:
				if x+2 < 15 and set_x[x+1][y] == color and set_x[x+2][y] == 0:
					re_set[x+2][y] = color_temp
				elif x-2 >= 0 and set_x[x-1][y] == color and set_x[x-2][y] == 0:
					re_set[x-2][y] = color_temp
				elif y+2 < 15 and set_x[x][y+1] == color and set_x[x][y+2] == 0:
					re_set[x][y+2] = color_temp
				elif y-2 >= 0 and set_x[x][y-1] == color and set_x[x][y-2] == 0:
					re_set[x][y-2] = color_temp
				elif x+2 < 15 and y+2 < 15 and set_x[x+1][y+1] == color and set_x[x+2][y+2] == 0:
					re_set[x+2][y+2] = color_temp
				elif x-2 >= 0 and y-2 >= 0 and set_x[x-1][y-1] == color and set_x[x-2][y-2] == 0:
					re_set[x-2][y-2] = color_temp
				elif x-2 >= 0 and y+2 < 15 and set_x[x-1][y+1] == color and set_x[x-2][y+2] == 0:
					re_set[x-2][y+2] = color_temp
				elif x+2 < 15 and y-2 >= 0 and set_x[x+1][y-1] == color and set_x[x+2][y-2] == 0:
					re_set[x+2][y-2] = color_temp
					
				elif x+2 < 15 and set_x[x+1][y] == 0 and set_x[x+2][y] == color:
					re_set[x+1][y] = color_temp
					if x-1 >= 0 and re_set[x-1][y] == 0:
						re_set[x-1][y] = color_temp
					if x+3 < 15 and re_set[x+3][y] == 0:
						re_set[x+3][y] = color_temp
				elif x-2 >= 0 and set_x[x-1][y] == 0 and set_x[x-2][y] == color:
					re_set[x-1][y] = color_temp
					if x+1 < 15 and re_set[x+1][y] == 0:
						re_set[x+1][y] = color_temp
					if x-3 >= 0 and re_set[x-3][y] == 0:
						re_set[x-3][y] = color_temp
				elif y+2 < 15 and set_x[x][y+1] == 0 and set_x[x][y+2] == color:
					re_set[x][y+1] = color_temp
					if y-1 >= 0 and re_set[x][y-1] == 0:
						re_set[x][y-1] = color_temp
					if y+3 < 15 and re_set[x][y+3] == 0:
						re_set[x][y+3] = color_temp
				elif y-2 >= 0 and set_x[x][y-1] == 0 and set_x[x][y-2] == color:
					re_set[x][y-1] = color_temp
					if y+1 >= 0 and re_set[x][y+1] == 0:
						re_set[x][y+1] = color_temp
					if y-3 < 15 and re_set[x][y-3] == 0:
						re_set[x][y-3] = color_temp
				elif x+2 < 15 and y+2 < 15 and set_x[x+1][y+1] == 0 and set_x[x+2][y+2] == color:
					re_set[x+1][y+1] = color_temp
					if x-1 >= 0 and y-1 >= 0 and re_set[x-1][y-1] == 0:
						re_set[x-1][y-1] = color_temp
					if x+3 < 15 and y+3 < 15 and re_set[x+3][y+3] == 0:
						re_set[x+3][y+3] = color_temp
				elif x-2 >= 0 and y-2 >= 0 and set_x[x-1][y-1] == 0 and set_x[x-2][y-2] == color:
					re_set[x-1][y-1] = color_temp
					if x+1 >= 0 and y+1 >= 0 and re_set[x+1][y+1] == 0:
						re_set[x+1][y+1] = color_temp
					if x-3 < 15 and y-3 < 15 and re_set[x-3][y-3] == 0:
						re_set[x-3][y-3] = color_temp
				elif x-2 >= 0 and y+2 < 15 and set_x[x-1][y+1] == 0 and set_x[x-2][y+2] == color:
					re_set[x-1][y+1] = color_temp
					if x+1 >= 0 and y-1 >= 0 and re_set[x+1][y-1] == 0:
						re_set[x+1][y-1] = color_temp
					if x-3 < 15 and y+3 < 15 and re_set[x-3][y+3] == 0:
						re_set[x-3][y+3] = color_temp
				elif x+2 < 15 and y-2 >= 0 and set_x[x+1][y-1] == 0 and set_x[x+2][y-2] == color:
					re_set[x+1][y-1] = color_temp
					if x-1 >= 0 and y+1 >= 0 and re_set[x-1][y+1] == 0:
						re_set[x-1][y+1] = color_temp
					if x+3 < 15 and y-3 < 15 and re_set[x+3][y-3] == 0:
						re_set[x+3][y-3] = color_temp
	return re_set

	
	
	
	
	
	