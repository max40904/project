import png
import sys
import chesstopng_module
import os
f = open(sys.argv[1], 'r')
while True:
    l1 = f.readline()
    if not l1: break
    l2 = f.readline()
    games=l1.split('"')[1].split(' ')
    game =[]
    if not os.path.exists("./image/"+l2):
    	os.makedirs("./image/"+l2)
    for i in range(len(games)-1):
    	game.append(games[i+1])
    	chesstopng_module.chesstopng(game,"./image/"+l2+"/"+games[i])

f.close()
# for l1 in f.readline():
# 	l2 = f.readline()
# 	print l1
	#print l2
	# games=l1.split('"')[0].split(' ')
	# game = []
	# for i in range(len(games)-1):
	# 	game.append(games[i+1])
	# 	chesstopng_module.chesstopng(game,"./image/"+l2+"/"+games[i])

