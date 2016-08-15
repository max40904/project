import sys
seqnum = 1
for count in range(len(sys.argv)-1):
	f = open(sys.argv[count+1],'r')
	print sys.argv[count+1]
	while True:
	    line1 = f.readline()
	    # print line1,seqnum
	    if not line1: break
	    line2 = f.readline()
	    # print line2,seqnum
	    RE ="black"
	    if line2.split("[")[1][1] == "1":
	    	RE ="black"
	    elif line2.split("[")[1][1] == "0":
	    	RE = "white"
	    else:
	    	RE ="draw"
	    game = line1.split("\"")[1].split(" ")
	    PB =  line2.split("[")[0].split("vs")[0]
	    PW =  line2.split("[")[0].split("vs")[1]
	    f_out = open("./gomuku_sgf/"+str(seqnum),"w")
	    f_out.write("(;PB[")
	    f_out.write(PB)
	    f_out.write("]PW[")
	    f_out.write(PW)
	    f_out.write("]RE[")
	    f_out.write(RE)
	    f_out.write("];")
	    for i in range(len(game)):
	    	x_loc = game[i][0]
	    	y_loc = chr(int(game[i][1:])+ord("a")-1)
	    	if i%2 == 0 :
	    		f_out.write("B[")
	    	else:
	    		f_out.write("W[")

	    	f_out.write(x_loc)
	    	f_out.write(y_loc)
	    	f_out.write("];")
		
	    seqnum = seqnum +1
	    f_out.write(")")
	
	f_out.close()
		
	print seqnum
	f.close()









