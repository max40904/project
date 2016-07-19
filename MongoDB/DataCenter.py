import sys
from pymongo import MongoClient

client = MongoClient()
db = client.test
coll =  db.Gamedata
seqnumber = 1 
for i in range(len(sys.argv)-1):
	f = open(sys.argv[i+1], 'r')
	while True:
		game = f.readline()
		if not game :break
		name = f.readline()
		print name, game
		Aname = name.split("[")[0].split("vs")[0]
		Bname = name.split("[")[0].split("vs")[0]
		Win = name.split("[")[1].replace("]","")[1]
		game =  game.split("=")[1].replace("\n","")
		print str(seqnumber)
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



