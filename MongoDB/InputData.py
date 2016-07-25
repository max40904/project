import sys
from pymongo import MongoClient
def inputdata ():
	client = MongoClient()
	db = client.gomukuDB
	coll =  db.Gamedata
	seqnumber = 1 
	for i in range(len(sys.argv)-2):
		f = open(sys.argv[i+2], 'r')
		while True:
			game = f.readline()
			if not game :break
			name = f.readline()
			Aname = name.split("[")[0].split("vs")[0]
			Bname = name.split("[")[0].split("vs")[0]
			Win = name.split("[")[1].replace("]","")[1]
			game =  game.split("=")[1].replace("\n","")
			result = coll.insert_one(
			    {
			    	"SeqNumber" : str(seqnumber),
			    	"PlayerA" : Aname,
			        "PlayerB" : Bname,
			        "Win"  : Win,
			        "Set" : game
			    }
		    )
			seqnumber = seqnumber + 1
		f.close()
	print "success  database"
def removedata():
	client = MongoClient()
	db = client.gomukuDB
	db.Gamedata.drop()
	print "delete database"

if sys.argv[1] is "i" :
	inputdata()
elif sys.argv[1] is "d":
	removedata()


