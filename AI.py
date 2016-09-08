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

		if self.__checkzero(policy_analysis.evaluate_dead_four (set,color,2))==1:
			return np.argmax(policy_analysis.evaluate_dead_four (set,color,2))

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

		y_estimate = self.policy.Return_softmax( x_48_stack, y_stack )
		check = policy_analysis.evaluate_self (set,color)

		return self.filter(y_estimate,check)

	def filter (set,check):
		anw = [[0 for i in range(15)] for j in range(15)]
		for i in range(15):
			for j in range(15):
				if check[i][j] == 1:
					anw = set[i][j]

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

	def run(self, set, color, beforeeight,time):
		pass

	def MontneCarlo(self, node , color , beforeeight, depth):
		
		if node.win == 1:
			return 1
		elif depte == 20:
			return 0

		ocolor = 0.5
		if color == 0.5:
			ocolor = 1


		selectpath = 0
		selvalue = 0.0
		for i in range(node.problist):
			temp = node.problist[i][1] + math.sqrt(math.log(node.num_match))/(1 +node.problist[i][2]) 
			if selvalue < temp:
				temp =selvalue
				selectpath = node.problist[i][0]
		flag = 0
		for i in range(len(node.nodelist)):
			if node.nodelist[i].step == selectpath:
				flag = 1
				self.MontneCarlo (node.nodelist[i],ocolor,beforeeight,depth+1)

		if flag ==0:
			 new = Ai.node()
			 newset = set.copy()
			 newset = game.StepGame(selectpath,newset,color)




			#newnode
			#self.MontneCarlo (node.nodelist[i],ocolor,beforeeight,depth+1)
			pass

		maxvalue = 
		allstep = 
		for i in range(len(node.nodelist)):
			pass


			







				

			
















	class node:
		def __init__(self):
			self.nodelist = []
			self.nprob = 0.0
			self.value = 0
			self.totalvalue = 0
			self.win = 0
			self.num_match = 0
			self.set = [[0 for i in range(15)] for j in range(15)]
			self.setprob = [[0.0 for i in range(15)] for j in range(15)]
			self.problist = []
			self.step = 0
		

		
