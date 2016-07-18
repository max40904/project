import png

def chtopng(in_file,op_file)
	f = open(in_file, 'r')
	file_str = f.read()
	game = file_str.split('"')[1].split(' ')

	w, h = 15, 15
	p = [[0 for x in range(w*3	)] for y in range(h)] 
	for i in range (w):
		for j in range(h):
			p[j][i*3]=147
			p[j][i*3+1]=147
			p[j][i*3+2]=72


	for i in range(len(game)):
		x_loc = int(game[i][1:])
		y_loc = int(ord(game[i][0])-ord('a'))
		if i%2 == 1:
			p[x_loc][y_loc*3]=255
			p[x_loc][y_loc*3+1]=255
			p[x_loc][y_loc*3+2]=255
		else :
			p[x_loc][y_loc*3]=0
			p[x_loc][y_loc*3+1]=0
			p[x_loc][y_loc*3+2]=0

	f = open(sop_file, 'wb')
	w = png.Writer(w, h)
	w.write(f, p) ; f.close()

