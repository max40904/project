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
		self.time = 0

	def SGFReturnSet_Win_three(self):
		if self.time ==0:
			self.SGFReturnSet()
			self.curstep = self.curstep +  self.maxstep/3
			self.time = 1
		
		elif self.time ==1:
			self.curstep = self.curstep +  self.maxstep/3
			self.time = 2
		
		elif self.time ==2:
			self.curstep = self.maxstep -2
			self.time =0

		
		return self.SGFReturnSet()
		

	def Find(self,i):
		Cursor =self.db.Gamedata.find({"SeqNumber" : str(i)})[0]
		return Cursor

	def SGFReturnSet_Random(self):
		
		self.curseq =random.randint(1,self.allset)
		if self.curseq >= self.allset:
			self.curseq = 1
		cursor =self.db.Gamedata.find({"SeqNumber" : str(self.curseq)})[0]
		self.nowchess = cursor["Set"]
		self.maxstep = len(self.nowchess)
		self.curstep = random.randint(0,self.maxstep-1)
		self.playerA = cursor["PlayerA"]
		self.playerB =  cursor["PlayerB"]
		self.Win = cursor["Win"]
		self.curset = [[0 for x in range(15)] for y in range(15)] 
		for i in range(self.curstep):
			game = self.nowchess[i]
			y_loc = int(ord(game[2])-ord('a'))
			x_loc = int(ord(game[3])-ord('a'))

			color = game[0]
			if color == "B":
				self.curset[x_loc][y_loc] = 1
			else:
				self.curset[x_loc][y_loc] = 0.5
		return self.curset
	def SGFReturnBefore(self):
		anw = []
		for i in range(8):
			if self.curstep - 8  + i >= 0:
				game = self.nowchess[self.curstep - 8  + i]
				num = self.__convert_char_to_num(game)
				anw.append(num)


		return anw



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
		y_loc = int(ord(game[2])-ord('a'))
		x_loc = int(ord(game[3])-ord('a'))
		curset = [[0 for x in range(15)] for y in range(15)]

		curset[x_loc][y_loc] = 1
		return curset
	def ReturnBeforeStep(self):
		gamestep = self.nowchess[:self.curstep]
		record = []
		for i in range(len(gamestep)):
			record.append(self.__convert_char_to_num(gamestep[i]))

		return record


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
	def __convert_char_to_num(self,game):
		y_loc = int(ord(game[2])-ord('a'))
		x_loc = int(ord(game[3])-ord('a'))
		num = y_loc + x_loc*15
		return num

