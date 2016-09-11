from gameinfo import policy_analysis
from gameinfo import game
from cnn import Policy
import numpy as np
import math

class Ai:
	def __init__(self, policy , input_stack, color):
		self.policy = policy
		self.input_stack = input_stack
		self.root = Ai.node()
		self.color = color
		self.dfscount = 0




	def ReturnAIAnw_beforeeight(self,set,color,beforeeight):

		x_48_stack = np.reshape(game.ReturnAllInfo_before (set, color,beforeeight),[1,15,15,self.input_stack])
		y_stack = np.reshape([[0 for i in range(15)] for j in range(15)],[1,225])

		Opennetcolor = 0.5
		if color == 0.5:
			Opennetcolor = 1

		if self.__checkzero(policy_analysis.evaluate_five (set,color))==1:
			return np.argmax(policy_analysis.evaluate_five (set,color))

		if self.__checkzero(policy_analysis.evaluate_five (set,Opennetcolor))==1:
			return np.argmax(policy_analysis.evaluate_five (set,Opennetcolor))
		if self.__checkzero(policy_analysis.evaluate_alive_four (set,color,1))==1:
			
			check = policy_analysis.evaluate_alive_four (set,color,1)
			anw = []
			for i in range(15):
				for j in range(15):
					if check[i][j] ==1:
						anw.append(i*15+j)
			
			return anw[0]

		if self.__checkzero(policy_analysis.evaluate_dead_four (set,color,2))==1:
			return np.argmax(policy_analysis.evaluate_dead_four (set,color,2))

		if self.__checkzero(policy_analysis.evaluate_alive_three_dead_four (set,color))==1:
			return np.argmax(policy_analysis.evaluate_alive_three_dead_four (set,color))

		

		y_estimate = self.policy.Return_prediction( x_48_stack, y_stack )


		return y_estimate

	
	def ReturnAIAnw_beforeeight_prob(self,set,color,beforeeight):

		x_48_stack = np.reshape(game.ReturnAllInfo_before (set, color,beforeeight),[1,15,15,self.input_stack])
		y_stack = np.reshape([[0 for i in range(15)] for j in range(15)],[1,225])

		Opennetcolor = 0.5
		if color == 0.5:
			Opennetcolor = 1
		check =[[0 for i in range(15)] for j in range(15)]
		
		curset = policy_analysis.evaluate_five (set,color)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)

		curset = policy_analysis.evaluate_five (set,Opennetcolor)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)

			
		curset = policy_analysis.evaluate_dead_four (set,color,2)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)


		curset = policy_analysis.evaluate_alive_three_dead_four (set,color)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)

		curset = policy_analysis.evaluate_alive_four (set,color,1)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)


		curset = policy_analysis.evaluate_alive_four (set,Opennetcolor,1)
		if self.__checkzero(curset)==1:
			check = curset
			y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
			return self.filter(y_estimate,check)

		y_estimate = np.reshape(self.policy.Return_softmax( x_48_stack, y_stack ),[15,15])
		check = policy_analysis.evaluate_self (set,0)
		return self.filter(y_estimate,check)

	def filter (self, set,check):
		anw = [[0. for i in range(15)] for j in range(15)]
		for i in range(15):
			for j in range(15):
				if check[i][j] == 1:

					anw[i][j] =set[i][j]
					
		return anw


	def ReturnAIAnw(self,set,color):

		x_48_stack = np.reshape(game.ReturnAllInfo (set, color),[1,15,15,self.input_stack])
		y_stack = np.reshape([[0 for i in range(15)] for j in range(15)],[1,225])



		Opennetcolor = 0.5
		if color == 0.5:
			Opennetcolor = 1

		if self.__checkzero(policy_analysis.evaluate_five (set,color))==1:
			return np.argmax(policy_analysis.evaluate_five (set,color))

		if self.__checkzero(policy_analysis.evaluate_five (set,Opennetcolor))==1:
			return np.argmax(policy_analysis.evaluate_five (set,Opennetcolor))

		if self.__checkzero(policy_analysis.evaluate_alive_three_dead_four (set,color))==1:
			return np.argmax(policy_analysis.evaluate_alive_three_dead_four (set,color))

		if self.__checkzero(policy_analysis.evaluate_alive_four (set,color,1))==1:
			
			check = policy_analysis.evaluate_alive_four (set,color,1)
			anw = []
			for i in range(15):
				for j in range(15):
					if check[i][j] ==1:
						anw.append(i*15+j)
			
			return anw[0]

		y_estimate = self.policy.Return_prediction( x_48_stack, y_stack )


		return y_estimate

	def __checkzero(self,set):
		for i in range(15):
			for j in range(15):
				if set[i][j] == 1:
					return 1
		return -1

	def firststep(self, set, color,  beforeeight,step): 
		#(always black )first step can't be here ,default is black [7][7]
		#second or third start
		ocolor = 1
		if color ==1:
			ocolor = 0.5
		self.root.step = step
		self.root.color = color
		self.root.beforeeight = beforeeight
		self.root.setprob = self.ReturnAIAnw_beforeeight_prob(set, ocolor, beforeeight)
		self.root.set = set
		self.root.totalmatch = 1
		self.root.value = 0
		self.root.totalvalue = 0
		self.root.problist = game.Return_Sort(np.reshape(self.root.setprob, [225]), 225 )


	def run(self, set, color, beforeeight, time):
		for i in range(time):
			self.MontneCarlo(self.root, color, beforeeight, 0)

	def OppentChoose(self,set ,color,beforeeight ,step):
		flag = 0
		print "OppentChoose" 
		for i in range(len(self.root.linklist)):
			print "loop"

			if self.root.linklist[i].step == step:
				print "haved"
				game.show_game_pos(self.root.linklist[i].step)
				flag = 1
				self.root = self.root.linklist[i]
				return 0
				break

		if flag ==0:
			print "nothing"
			self.root = Ai.node()
			self.firststep( set, color,  beforeeight,step)

		return 0




				
				
	def ReturnMonteCarlorun(self, set, color, beforeeight):
		print "ReturnMonteCarlorun"
		self.run(set, color, beforeeight, 200)
		
		maxvalue = -999999999
		maxvalue_num = 0
		self.dfsreview()
		maxvalue_2 = -999999999
		maxvalue_num_2 = 0

		maxrate =-1.0 
		maxrate_num =  0
		print "\n\nall choise"
		print len(self.root.linklist)
		record = 0.
		for i in range(len(self.root.linklist)):
			total = self.root.linklist[i].totalmatch
			if total >=0:
				print self.root.linklist[i].step,"step!!"
				print self.root.linklist[i].totalvalue,"value!!"
				print self.root.linklist[i].totalwin," win!!"
				print self.root.linklist[i].totalloss," loss!!"
				print self.root.linklist[i].totalmatch," total!!"
			

				game.show_game_pos(self.root.linklist[i].step)


				
			winrate = float(self.root.linklist[i].totalwin) / float(self.root.linklist[i].totalmatch) 
			loss = float(self.root.linklist[i].totalloss) /float(self.root.linklist[i].totalmatch)
			
			if  (winrate * 2  - loss ) > ( maxrate )  :
				
				record = winrate
				maxrate = (winrate*2-loss)
				maxrate_num = i

			if maxvalue_2 < self.root.linklist[i].totalvalue  :
				maxvalue_2 = self.root.linklist[i].totalvalue
				maxvalue_num_2 = i

			if maxvalue < self.root.linklist[i].totalvalue  :
				maxvalue = self.root.linklist[i].totalvalue
				maxvalue_num = i
		print "final",maxvalue
		print "winrate ",winrate
		self.root = self.root.linklist[maxrate_num]
		# if maxvalue_num!=0:
		# 	self.root = self.root.linklist[maxvalue_num]
		# else :
		# 	self.root = self.root.linklist[maxvalue_num_2]
		
		
		
		return self.root.step
	def dfsreview(self):
		print "dfs"
		
		self.dfscount = 0
		self.dfs(self.root,1)
		print "dfsallcount"
		print self.dfscount



	def dfs(self,node,depth):
		for i in range(len(node.linklist)):
			self.dfs(node.linklist[i],depth+1)
		if depth ==3:
			game.show_game_pos(node.step),node.step
			print "color", node.color
			print "value",node.value
			print "totalvalue",node.totalvalue
			print "allmatchcount",node.totalmatch
			print "all win",node.totalwin
			print "all lose",node.totalloss
			print ""
		self.dfscount = self.dfscount + 1
		


	

	def MontneCarlo(self, node , color , beforeeight, depth):
		node.totalvalue = node.value
		if node.win == 1:
			node.totalmatch = 1
			node.totalwin = 1
			
			return 1
		elif node.loss ==1:
			node.totalmatch = 1
			node.totalloss = 1
			
			return -1
		elif depth == 15:
			node.totalmatch = 1
			return 0

		ocolor = 0.5
		if color == 0.5:
			ocolor = 1


		selectpath = 0
		selvalue = 0.0
		nextprob = 0
		limit = len(node.problist)
		if limit>6:
			limit = 6
	

		for i in range(limit):
			if node.color !=self.color :
				temp = node.problist[i][1] + 1 *(math.log(node.totalmatch+1))/(1 + node.count[i]) 
			elif node.color ==self.color :
				temp = node.problist[i][1] + node.problist[i][1] *(math.log(node.totalmatch+1))/(1 + node.count[i]) 

			if selvalue < temp:
				selvalue = temp
				selectpath = node.problist[i][0]
				nextprob = node.problist[i][1]
		flag = 0

		for i in range(len(node.linklist)):
			if node.linklist[i].step == selectpath:


				node.count[i] = node.count[i] + 1
				flag = 1
				self.MontneCarlo (node.linklist[i],ocolor,beforeeight,depth+1)

		if flag ==0:
			#create new node

			new = Ai.node()

			
			newset = game.StepGame(selectpath,node.set,color)


			new_beforeeight = [0 for i in range(8)]
			for j in range(len(beforeeight)):

				new_beforeeight.append(beforeeight[j])


			new_beforeeight.append(node.step)
			new.prob = nextprob

			new.color = color
			new.step = selectpath
			new.setprob =self.ReturnAIAnw_beforeeight_prob(newset, ocolor, new_beforeeight)
			new.set = newset
			new.beforeeight = new_beforeeight
			new.totalmatch = 0
			new.value = self.evaluete_value(node.set , color, selectpath)
			new.totalvalue = new.value
			if new.value ==90000000000 and self.color ==color:
				new.win = 1
			if new.value ==-90000000 and self.color != color:
				new.loss = 1




			new.problist = game.Return_Sort(np.reshape(new.setprob,[225]),225)
			
			#add to orighinal list
			node.linklist.append(new)
			self.MontneCarlo (node.linklist[len(node.linklist)-1],ocolor,beforeeight,depth+1)
			

		select_value = 0
		tempvalue = 0

		count_step = 0 
		count_win = 0
		count_loss = 0

		if node.color !=self.color: 
			#player1
			tempvalue =  -922337203685477580

			for i in range(len(node.linklist)):
				if node.linklist[i].totalvalue > tempvalue:
					tempvalue = node.linklist[i].totalvalue
					select_value = node.linklist[i].totalvalue

				count_step = count_step + node.linklist[i].totalmatch
				count_win = count_win +  node.linklist[i].totalwin
				count_loss = count_loss + node.linklist[i].totalloss
		elif node.color ==self.color:
			#player2
			tempvalue = 922337203685477580
			for i in range(len(node.linklist)):
				if node.linklist[i].totalvalue < tempvalue:
					tempvalue = node.linklist[i].totalvalue
					select_value = node.linklist[i].totalvalue

				count_step = count_step + node.linklist[i].totalmatch
				count_win = count_win +  node.linklist[i].totalwin
				count_loss = count_loss + node.linklist[i].totalloss

		node.totalvalue = node.totalvalue  +  select_value 
		node.totalmatch = count_step
		node.totalwin = count_win
		node.totalloss = count_loss



		return 0		


	class node:
		def __init__(self):
			self.color = 0  #
			self.linklist = [] #
			self.count = [0 for i in range(225)]
			self.prob = 0.0
			self.value = 0  
			self.totalvalue = 0 #
			self.win = 0 #
			self.loss = 0#
			self.totalwin = 0 #
			self.totalloss = 0 #

			self.totalmatch = 0 # 
			self.set = [[0 for i in range(15)] for j in range(15)] #
			self.setprob = [[0.0 for i in range(15)] for j in range(15)] #
			self.beforeeight = [0 for i in range(8)] #
			self.problist = [] #
			self.step = 0 #



	def evaluete_value(self,set,color,step):
		y_loc = step/15
		x_loc = step%15
		if self.color==1:
			if color==1:
				check  = policy_analysis.evaluate_five(set,color)
				if check[y_loc][x_loc]==1:
					return 90000000000

				check = policy_analysis.evaluate_alive_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return 50000000
				check = policy_analysis.evaluate_dead_four (set,color,2)
				if check[y_loc][x_loc]==1:
					return 15000000
				check =policy_analysis.evaluate_alive_three_dead_four (set,color)
				if  check[y_loc][x_loc]==1:
					return 15000000
				check = policy_analysis.evaluate_dead_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return 150
				check = policy_analysis.evaluate_alive_three (set,color,2)
				if check[y_loc][x_loc]==1:
					return 0

				check = policy_analysis.evaluate_alive_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return 100
				check = policy_analysis.evaluate_dead_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return 5
				check = policy_analysis.evaluate_alive_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return 10
				check = policy_analysis.evaluate_dead_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return 5
				return 1


			elif color ==0.5:
				check  = policy_analysis.evaluate_five(set,color)
				if check[y_loc][x_loc]==1:
					return -90000000

				check = policy_analysis.evaluate_alive_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return -50000000
				check = policy_analysis.evaluate_dead_four (set,color,2)
				if check[y_loc][x_loc]==1:
					return -1500000
				check =policy_analysis.evaluate_alive_three_dead_four (set,color)
				if  check[y_loc][x_loc]==1:
					return -1500000
				check = policy_analysis.evaluate_dead_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return -120000
				check = policy_analysis.evaluate_alive_three (set,color,2)
				if check[y_loc][x_loc]==1:
					return -800000
				check = policy_analysis.evaluate_alive_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return -10000
				check = policy_analysis.evaluate_dead_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return -500
				check = policy_analysis.evaluate_alive_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return -1000
				check = policy_analysis.evaluate_dead_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return -500
				return -200

		elif self.color ==0.5:
			if color==0.5:
				check  = policy_analysis.evaluate_five(set,color)
				if check[y_loc][x_loc]==1:
					return 90000000000

				check = policy_analysis.evaluate_alive_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return 50000000000
				check = policy_analysis.evaluate_dead_four (set,color,2)
				if check[y_loc][x_loc]==1:
					return 1500000000
				check =policy_analysis.evaluate_alive_three_dead_four (set,color)
				if  check[y_loc][x_loc]==1:
					return 1500000000
				check = policy_analysis.evaluate_dead_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return 150
				check = policy_analysis.evaluate_alive_three (set,color,2)
				if check[y_loc][x_loc]==1:
					return 8000000000

				check = policy_analysis.evaluate_alive_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return 100
				check = policy_analysis.evaluate_dead_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return 5
				check = policy_analysis.evaluate_alive_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return 10
				check = policy_analysis.evaluate_dead_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return 5
				return 1


			elif color ==1:
				check  = policy_analysis.evaluate_five(set,color)
				if check[y_loc][x_loc]==1:
					return -90000000

				check = policy_analysis.evaluate_alive_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return -50000000
				check = policy_analysis.evaluate_dead_four (set,color,2)
				if check[y_loc][x_loc]==1:
					return -1500000
				check =policy_analysis.evaluate_alive_three_dead_four (set,color)
				if  check[y_loc][x_loc]==1:
					return -1500000
				check = policy_analysis.evaluate_dead_four (set,color,1)
				if check[y_loc][x_loc]==1:
					return -120000
				check = policy_analysis.evaluate_alive_three (set,color,2)
				if check[y_loc][x_loc]==1:
					return  0
				check = policy_analysis.evaluate_alive_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return -10000
				check = policy_analysis.evaluate_dead_three (set,color,1)
				if check[y_loc][x_loc]==1:
					return -500
				check = policy_analysis.evaluate_alive_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return -1000
				check = policy_analysis.evaluate_dead_two (set,color,1)
				if check[y_loc][x_loc]==1:
					return -500
				return -200

		return 0






			







				

			

















		

		
