# -*- coding: utf-8 -*- 
import sys
from PyQt4.QtGui import *
import pygame
import Chessboard

from cnn import Policy
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np
import AI


class Gomoku():

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((600, 500))
		pygame.display.set_caption("五子棋")
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("monospace", 15)
		self.going = True

		self.chessboard = Chessboard.Chessboard()

	def loop(self):
		while self.going:
			self.update()
			self.draw()	
			self.clock.tick(60)

		pygame.quit()

	def update(self):
		global color
		global ai
		global time
		if color == 1:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.going = False
				elif e.type == pygame.MOUSEBUTTONDOWN:
					self.chessboard.handle_key_event(e)
					print self.chessboard.grid					
					y_estimate = ai.ReturnAIAnw(self.chessboard.grid, 0.5)
					print y_estimate
					self.chessboard.set_piece(y_estimate/15,y_estimate%15)
					self.chessboard.check_win(y_estimate/15,y_estimate%15)
		else:
			if time == 0:
				self.chessboard.set_piece(7,7)
				time = 1
			else:
				for e in pygame.event.get():
					if e.type == pygame.QUIT:
						self.going = False
					elif e.type == pygame.MOUSEBUTTONDOWN:
						self.chessboard.handle_key_event(e)
						print self.chessboard.grid					
						y_estimate = ai.ReturnAIAnw(self.chessboard.grid, 1)
						print y_estimate
						self.chessboard.set_piece(y_estimate/15,y_estimate%15)
						self.chessboard.check_win(y_estimate/15,y_estimate%15)

	def draw(self):
		global win
		global color
		self.screen.fill((255, 255, 255))
		self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))	
		self.chessboard.draw(self.screen)
		pygame.display.update()
		if self.chessboard.game_over:
			self.screen.blit(self.font.render("{0} Win".format("Black" if self.chessboard.winner == 1 else "White"), True, (0, 0, 0)), (500, 10))
			pygame.display.update()
			def end():
				endbutton.close()
				pygame.quit()
				sys.exit()
			if(self.chessboard.winner==1 and win==0):
				if(self.chessboard.winner==1 and color==0.5):
					app2 = QApplication(sys.argv)
					endbutton = QPushButton()
					endbutton.resize(200,200)
					endbutton.setText("Black Win!!!")
					endbutton.setWindowTitle("You Lose!!!")
					endbutton.show()
					endbutton.clicked.connect(end)
					app2.exec_()
				else:
					app2 = QApplication(sys.argv)
					endbutton = QPushButton()
					endbutton.resize(200,200)
					endbutton.setText("Black Win!!!")
					endbutton.setWindowTitle("You Win!!!")
					endbutton.show()
					endbutton.clicked.connect(end)
					app2.exec_()
			elif(self.chessboard.winner==0.5 and win==0):
				if(self.chessboard.winner==0.5 and color==1):
					app2 = QApplication(sys.argv)
					endbutton = QPushButton()
					endbutton.resize(200,200)
					endbutton.setText("White Win!!!")
					endbutton.setWindowTitle("You Lose!!!")
					endbutton.show()
					endbutton.clicked.connect(end)
					app2.exec_()
				else:
					app2 = QApplication(sys.argv)
					endbutton = QPushButton()
					endbutton.resize(200,200)
					endbutton.setText("White Win!!!")
					endbutton.setWindowTitle("You Win!!!")
					endbutton.show()
					endbutton.clicked.connect(end)
					app2.exec_()

			win=win+1
		
		'''			
			def buttonClicked2():
				if(radiobutton2.isChecked()):
					color = 1
				else:
					color = 0
				widget2.close()

			app3 = QApplication(sys.argv)
			widget2 = QWidget()
			widget2.resize(400, 200)
			widget2.move(400, 150)
			widget2.setWindowTitle("Choose your color!")
			radiobutton2_1 = QRadioButton(widget2)
			radiobutton2_2 = QRadioButton(widget2)
			radiobutton2_1.setText("Black")
			radiobutton2_2.setText("white")
			radiobutton2_1.move(80,50)
			radiobutton2_2.move(250,50)
			radiobutton2_1.setChecked(True)
			button2 = QPushButton(widget2)
			button2.setText("Let's   Restart   The   Game!!!")
			button2.move(110,120)
			button2.clicked.connect(buttonClicked2)
			widget2.show()
			app3.exec_()
		'''

			

		


if __name__ == '__main__':
	color = 1
	win = 0
	time = 0
	def buttonClicked():
		global color
		if(radiobutton1.isChecked()):
			color = 1
			print 123
		elif(radiobutton2.isChecked()):
			color = 0.5
			print 123
		widget.close()

	app = QApplication(sys.argv)
	widget = QWidget()
	widget.resize(400, 200)
	widget.move(400, 150)
	widget.setWindowTitle("Choose your color!")
	radiobutton1 = QRadioButton(widget)
	radiobutton2 = QRadioButton(widget)
	radiobutton1.setText("Black")
	radiobutton2.setText("white")
	radiobutton1.move(80,50)
	radiobutton2.move(250,50)
	radiobutton1.setChecked(True)
	button = QPushButton(widget)
	button.setText("Let's   Start   The   Game!!!")
	button.move(110,120)
	button.clicked.connect(buttonClicked)
	widget.show()
	app.exec_()

	learning_rate = 0.0003
	input_stack = 48
	step_check_crossenropy = 100
	k_filter = input_stack * 2
	seed = 13


	Data = DataCenter.MongoDB()
	Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 
	ai = AI.Ai(Cnn,input_stack)
	Cnn.restore("./Neural_network_save/save_net530000.ckpt")

	game = Gomoku()
	game.loop()





























