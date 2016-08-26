from gameinfo import policy_analysis
from gameinfo import game
from cnn import Policy
import numpy as np

class Ai:
	def __init__(self, policy , input_stack):
		self.policy = policy
		self.input_stack = input_stack


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
		

		
