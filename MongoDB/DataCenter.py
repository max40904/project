from pymongo import MongoClient
import random
class MongoDB:
	def __init__(self):
		self.client =  MongoClient()
		self.db = self.client.gomukuDB
		self.curseq = 0
		self.curstep = 1
		self.curset = [[0 for x in range(15)] for y in range(15)] 
		self.allset = self.db.Gamedata.count()
		self.maxstep  = 0
		self.nowchess = "a"
		self.playerA = "unknown"
		self.playerB = "unknown"
		self.Win = "-1"
		

	def Find(self,i):
		Cursor =self.db.Gamedata.find({"SeqNumber" : str(i)})[0]
		return Cursor
	def SGFReturnSet(self):
		self.curstep = self.curstep + 1
		while self.curstep >= self.maxstep:
			self.curseq =self.curseq + 1 
			if self.curseq >= self.allset:
				self.curseq = 1
			cursor =self.db.Gamedata.find({"SeqNumber" : str(self.curseq)})[0]
			self.nowchess = cursor["Set"]
			self.maxstep = len(self.nowchess)
			self.curstep = 1
			self.playerA = cursor["PlayerA"]
			self.playerB =  cursor["PlayerB"]
			self.Win = cursor["Win"]
			self.curset = [[0 for x in range(15)] for y in range(15)] 
		
		game = self.nowchess[self.curstep-1]
		y_loc = int(ord(game[2])-ord('a'))
		x_loc = int(ord(game[3])-ord('a'))

		color = game[0]
		if color == "B":
			self.curset[x_loc][y_loc] = 1
		else:
			self.curset[x_loc][y_loc] = 0.5
		return self.curset

	def SGFReturnAnw(self):
		game = self.nowchess[self.curstep]
		print game
		y_loc = int(ord(game[2])-ord('a'))
		x_loc = int(ord(game[3])-ord('a'))
		curset = [[0 for x in range(15)] for y in range(15)]

		curset[x_loc][y_loc] = 1
		return curset


	def ReturnSet(self):
		self.curstep =self.curstep + 1
		if self.curstep >= self.maxstep :
			self.curseq = random.randint(1,self.allset)
			cursor =self.db.Gamedata.find({"SeqNumber" : str(self.curseq)})[0]
			self.nowchess = cursor["Set"].replace('"',"")
			self.maxstep = len(self.nowchess.split(" "))
			self.curstep = 1
			self.playerA = cursor["PlayerA"]
			self.playerB =  cursor["PlayerB"]
			self.Win = cursor["Win"]
			self.curset = [[0 for x in range(15)] for y in range(15)] 
		game = self.nowchess.split(" ")[self.curstep-1]
		y_loc = int(ord(game[0])-ord('a'))
		x_loc = int(game[1:])-1
		if self.curstep%2 ==1:
			self.curset[x_loc][y_loc] = 1
		else :
			self.curset[x_loc][y_loc] = 0.5
		return self.curset

	def ReturnAnw(self):
		game = self.nowchess[self.curstep]
		y_loc = int(ord(game[2])-ord('a'))
		x_loc = int(ord(game[3])-ord('a'))
		curset = [[0 for x in range(15)] for y in range(15)] 
	
		curset[x_loc][y_loc] = 1
	
		return curset
	def ReturnPlayerA(self):
		return self.playerA 
	def ReturnPlayerA(self):
		return self.playerB
	def ReturnWin(self):
		return self.Win

	def ReturnColor(self):
		step = self.curstep +1
		color = 1.
		if step %2 == 0 :
			color = 0.5
		return color

