import sys
from pymongo import MongoClient
def inputdata (collections = None):
	client = MongoClient()
	db = client.gomukuDB
	coll =  db[collections]
	seqnumber = coll.count() +1 
	

	for i in range(len(sys.argv)-3):
		print sys.argv[i+3]
		f = open(sys.argv[i+3], 'r')
		sgf = f.read()
		nabw = sgf.split(";")[1].replace("[", " " ).replace("]"," ").split(" ")
		win = nabw[nabw.index("RE")+1]
		PB =  nabw[nabw.index("PB")+1]
		PW =  nabw[nabw.index("PW")+1]
		game = sgf.split(";")[2:len(sgf.split(";"))-1]
		result = coll.insert(
		    {
		    	"SeqNumber" : str(seqnumber),
		    	"PlayerA" : PB,
		        "PlayerB" : PW,
		        "Win"  : win,
		        "Set" : game
		    }
	    )
		seqnumber = seqnumber + 1




		f.close()

	print "success  database"
def removedata(colletions ):
	client = MongoClient()
	db = client.gomukuDB
	coll = db[colletions]
	coll.drop()
	print "delete database"

if sys.argv[1] is "i" :
	inputdata(sys.argv[2])
elif sys.argv[1] is "d":
	removedata(sys.argv[2])


