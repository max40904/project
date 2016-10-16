import time

class referee:
	def __init__(self):
		self.CurSet = [[0 for i in range(15)] for j in range(15)]
		self.SetStep = [[0 for i in range(15)] for j in range(15)]
		self.Step_Rer = []
		self.step = 1
		self.winner = 0
		self.grid_count = 15




	def input(self,set,num):
		print "input",num
		self.Step_Rer.append(num)
		j = num / 15
		i = num % 15
		self.SetStep[j][i] =  self.step
		self.CurSet = set

		self.step = self.step + 1
		if self.__CheckWin(j,i) ==1:
			self.writefile()
			print "Referee"
			self.step = 1
			self.winner = 0
			self.CurSet =  [[0 for i in range(15)] for j in range(15)]
			self.SetStep = [[0 for i in range(15)] for j in range(15)]
			self.Step_Rer = []

	def Before_Eight(self):
		num = []
		for i in range(8):
			if  self.step - 9  + i >=0:
				print "eight",self.Step_Rer[self.step - 9  + i ]
				num.append(self.Step_Rer[self.step - 9  + i ])



		return num
		



	def writefile(self):
		file = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + ".sgf"
		RE = "black"
		if self.winner ==0.5:
			RE = "white"
		PB = "player1"
		PW = "player2"
		f_out = open("./set_record/"+file,"w")
		f_out.write("(;PB[")
		f_out.write(PB)
		f_out.write("]PW[")
		f_out.write(PW)
		f_out.write("]RE[")
		f_out.write(RE)
		f_out.write("];")
		for i in range(self.step - 1):
			x_loc = chr(self.Step_Rer[i]/15+ord("a"))
			y_loc = chr(self.Step_Rer[i]%15+ord("a"))
			if i%2 == 0 :
				f_out.write("B[")
			else: 
				f_out.write("W[")
			f_out.write(x_loc)
			f_out.write(y_loc)
			f_out.write("];")
		f_out.write(")")
		f_out.close()



	def __CheckWin(self, j , i):
		n_count = self.__get_continuous_count(j, i, -1, 0)
		s_count = self.__get_continuous_count(j, i, 1, 0)

		e_count = self.__get_continuous_count(j, i, 0, 1)
		w_count = self.__get_continuous_count(j, i, 0, -1)

		se_count = self.__get_continuous_count(j, i, 1, 1)
		nw_count = self.__get_continuous_count(j, i, -1, -1)

		ne_count = self.__get_continuous_count(j, i, -1, 1)
		sw_count = self.__get_continuous_count(j, i, 1, -1)

		if (n_count + s_count + 1 >= 5) or (e_count + w_count + 1 >= 5) or (se_count + nw_count + 1 >= 5) or (ne_count + sw_count + 1 >= 5):
			self.winner = self.CurSet[j][i]
			return 1

		return -1
 			



	def __get_continuous_count(self, r, c, dr, dc):
		piece = self.CurSet[r][c]
		result = 0
		i = 1
		while True:
			new_r = r + dr * i
			new_c = c + dc * i
			if 0 <= new_r < self.grid_count and 0 <= new_c < self.grid_count:
				if self.CurSet[new_r][new_c] == piece:
					result += 1
				else:
					break
			else:
				break
			i += 1
		return result


