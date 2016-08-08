import sys
f_num = open("num.ty","r")
con = f_num.read()
seq = int(con)
f_num.close()
for count in range(len(sys.argv)-1):
	
	file_lib = open(sys.argv[count + 1],'r')
	content = file_lib.read()
	game = content.split("-----")[2].replace("\r\n","").replace("   "," ").replace("  "," ").replace("  "," ").split(" ")
	RE = "draw"
	PB = "PB"
	PW = "PA"

	f_out = open("./renju_toumuent/a" + str(seq)+".sgf",'w')
	f_out.write("(;PB[")
	f_out.write(PB)
	f_out.write("]PW[")
	f_out.write(PW)
	f_out.write("]RE[")
	f_out.write(RE)
	f_out.write("];")
	print sys.argv[count + 1]
	print len(game)
	for i in range(1, len(game)-1,2):
		print game[i],game[i+1]
		x_loc = game[i+1][0].lower()
	 	y_loc = chr (int(game[i+1][1:])+ord("a")-1)
		if int(game[i]) % 2 == 1 :
			f_out.write("B[")
		else :
			f_out.write("W[")
		f_out.write(x_loc)
		f_out.write(y_loc)
		f_out.write("];")
	seq = seq + 1
	f_out.write(")")
		
f_flag = open("num.ty","w")
f_flag.write(str(seq))
f_flag.close()

