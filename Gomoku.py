# -*- coding: utf-8 -*- 
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import pygame
import Chessboard
import Referee
from cnn import Policy
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np
import AI
import thread

class Gomoku():

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((650, 500))
		pygame.display.set_caption("五子棋")
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("monospace", 15)
		self.going = True
		self.first_R=-1
		self.first_C=-1
		
		self.chessboard = Chessboard.Chessboard()

	def loop(self):		
		#thread.start_new_thread( self.draw_thread,() )
		while self.going:
			self.update()
			self.draw(self.first_R,self.first_C)
			self.clock.tick(60)
			if self.chessboard.game_over:
				global ai
				ai.Clear()
				print '><'
				return 0
		pygame.quit()

	def update(self):
		global color
		global ai
		global time
		global level
		if color == 1:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.going = False
				elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
					origin_x = self.chessboard.start_x - self.chessboard.edge_size
					origin_y = self.chessboard.start_y - self.chessboard.edge_size
					size = (self.chessboard.grid_count - 1) * self.chessboard.grid_size + self.chessboard.edge_size * 2
					pos = e.pos
					if origin_x <= pos[0] <= origin_x + size and origin_y <= pos[1] <= origin_y + size:
						if not self.chessboard.game_over:
							x = pos[0] - origin_x
							y = pos[1] - origin_y
							r = int(y // self.chessboard.grid_size)
							c = int(x // self.chessboard.grid_size)
							if self.chessboard.grid[r][c] != 0:
								print 123
								break
					else:
						print 456
						break
					
					if self.chessboard.check_three(r,c)==False:
						self.screen.blit(self.font.render(("You can not put here"), True, (0, 0, 0)), (120, 465))
						pygame.display.update()
						pygame.time.wait(1000)
						break

					self.chessboard.handle_key_event(e)
					
					print self.chessboard.grid
					judge.input(self.chessboard.grid,self.chessboard.nowstep)
					self.first_R=r
					self.first_C=c
					self.draw(self.first_R,self.first_C)			
					if self.chessboard.winner ==None:
						before_eight = judge.Before_Eight()

						if time ==0:
							ai.firststep(self.chessboard.grid, 1, before_eight,self.chessboard.nowstep)
							time = 1
						else :
							ai.OppentChoose(self.chessboard.grid,1,before_eight,self.chessboard.nowstep)
						if level==3:
							y_estimate = ai.ReturnMonteCarlorun(self.chessboard.grid, 0.5,before_eight)
						else:
							y_estimate = ai.ReturnAIAnw_beforeeight(self.chessboard.grid, 0.5,before_eight)
						print y_estimate
						self.chessboard.set_piece(y_estimate/15,y_estimate%15)
						judge.input(self.chessboard.grid,self.chessboard.nowstep)
						self.chessboard.check_win(y_estimate/15,y_estimate%15)
						self.first_R=y_estimate/15
						self.first_C=y_estimate%15
		else:
			if time == 0:
				self.chessboard.set_piece(7,7)
				judge.input(self.chessboard.grid,self.chessboard.nowstep)
				self.first_R=7
				self.first_C=7
				time = 1
			else:
				for e in pygame.event.get():
					if e.type == pygame.QUIT:
						self.going = False
					elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
						origin_x = self.chessboard.start_x - self.chessboard.edge_size
						origin_y = self.chessboard.start_y - self.chessboard.edge_size
						size = (self.chessboard.grid_count - 1) * self.chessboard.grid_size + self.chessboard.edge_size * 2
						pos = e.pos
						if origin_x <= pos[0] <= origin_x + size and origin_y <= pos[1] <= origin_y + size:
							if not self.chessboard.game_over:
								x = pos[0] - origin_x
								y = pos[1] - origin_y
								r = int(y // self.chessboard.grid_size)
								c = int(x // self.chessboard.grid_size)
								if self.chessboard.grid[r][c] != 0:
									print 123
									break
						else:
							print 456
							break

						self.chessboard.handle_key_event(e)

						print self.chessboard.grid
						judge.input(self.chessboard.grid,self.chessboard.nowstep)

						self.first_R=r
						self.first_C=c

						self.draw(self.first_R,self.first_C)	
						if self.chessboard.winner ==None:
							before_eight = judge.Before_Eight()

							if time == 1:
								ai.firststep(self.chessboard.grid,0.5,before_eight,self.chessboard.nowstep)
								time = 2
							else :
								ai.OppentChoose(self.chessboard.grid,0.5,before_eight,self.chessboard.nowstep)
							if level==3:
								y_estimate = ai.ReturnMonteCarlorun(self.chessboard.grid, 1,before_eight)
							else:
								y_estimate = ai.ReturnAIAnw_beforeeight(self.chessboard.grid, 1,before_eight)
							print y_estimate

							self.chessboard.set_piece(y_estimate/15,y_estimate%15)
							judge.input(self.chessboard.grid,self.chessboard.nowstep)

							self.chessboard.check_win(y_estimate/15,y_estimate%15)

							self.first_R=y_estimate/15
							self.first_C=y_estimate%15

	def draw(self,r,c):
		global win
		global color
		self.screen.fill((255, 255, 255))
		self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))	
		self.chessboard.draw(self.screen,r,c)

		for i in range (15):
			x = i+1
			font = pygame.font.Font(None,20)
			game.screen.blit(font.render(str(x), True, (0,128,255)), (410,i*26+46))
			y = i+97	
			game.screen.blit(font.render(chr(y), True, (255,0,0)), (i*26+26,430))
		
		game.screen.blit(font.render("The black player can", True, (0,0,0)), (450,120))
		game.screen.blit(font.render("not play three to three,", True, (0,0,0)), (450,170))
		game.screen.blit(font.render("and four to four.", True, (0,0,0)), (450,220))
		
		pygame.display.update()

		if self.chessboard.game_over:
			self.screen.blit(self.font.render("{0} Win".format("Black" if self.chessboard.winner == 1 else "White"), True, (0, 0, 0)), (500, 10))
			pygame.display.update()
			print "XD"
			global appx
			global i2
			global endbutton
			def end():
				print '@@'
				endbutton[i2].close()
				win2=1

			if(self.chessboard.winner==1 and win==0):
				if(self.chessboard.winner==1 and color==0.5):
					appx[i2] = QApplication(sys.argv)
					endbutton[i2] = QPushButton()
					endbutton[i2].resize(200,200)
					endbutton[i2].setText("Black Win!!!")
					endbutton[i2].setWindowTitle("You Lose!!!")
					endbutton[i2].show()
					endbutton[i2].clicked.connect(end)
					appx[i2].exec_()
				else:
					appx[i2] = QApplication(sys.argv)
					endbutton[i2] = QPushButton()
					endbutton[i2].resize(200,200)
					endbutton[i2].setText("Black Win!!!")
					endbutton[i2].setWindowTitle("You Win!!!")
					endbutton[i2].show()
					endbutton[i2].clicked.connect(end)
					appx[i2].exec_()
			elif(self.chessboard.winner==0.5 and win==0):
				if(self.chessboard.winner==0.5 and color==1):
					appx[i2] = QApplication(sys.argv)
					endbutton[i2] = QPushButton()
					endbutton[i2].resize(200,200)
					endbutton[i2].setText("White Win!!!")
					endbutton[i2].setWindowTitle("You Lose!!!")
					endbutton[i2].show()
					endbutton[i2].clicked.connect(end)
					appx[i2].exec_()
				else:
					appx[i2] = QApplication(sys.argv)
					endbutton[i2] = QPushButton()
					endbutton[i2].resize(200,200)
					endbutton[i2].setText("White Win!!!")
					endbutton[i2].setWindowTitle("You Win!!!")
					endbutton[i2].show()
					endbutton[i2].clicked.connect(end)
					appx[i2].exec_()

			win=win+1
			i2=i2+1	
	
	#def draw_thread(self):
	#	while 1:
	#		self.clock.tick(60)
	#		self.draw()


if __name__ == '__main__':
	win2 = 0
	level = 1
	i=0
	app={}
	i2=0
	appx={}
	endbutton={}
	learning_rate = 0.003 / 2
	input_stack = 56
	step_save = 10000
	step_draw = 100
	step_check_crossenropy = 100
	k_filter = input_stack * 4
	training_iters = 540002
	seed = 23
	ai=None

	openfile = 520000

	Data = DataCenter.MongoDB("Gamedata")
	Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 
	

	
	judge = Referee.referee()
	
	def buttonClicked():
		global color
		global ai
		global level
		global openfile	
		if(radiobutton1.isChecked()):
			color = 1
			if(lvradiobutton1.isChecked()):
				openfile = 100000
				level = 1
				
			elif(lvradiobutton2.isChecked()):
				openfile = 520000
				level = 2

			elif(lvradiobutton3.isChecked()):
				openfile = 520000
				level = 3
			Cnn.restore("./Neural_network_save/save_net"+str(openfile)+".ckpt")
			ai = AI.Ai(Cnn,input_stack,0.5)
			print level
		elif(radiobutton2.isChecked()):
			color = 0.5
			if(lvradiobutton1.isChecked()):
				openfile = 100000
				level = 1
			elif(lvradiobutton2.isChecked()):
				openfile = 520000
				level = 2
			elif(lvradiobutton3.isChecked()):
				openfile = 520000
				level = 3
			Cnn.restore("./Neural_network_save/save_net"+str(openfile)+".ckpt")
			ai = AI.Ai(Cnn,input_stack,1)
			print level
		if level!=3:
			ai.Clear()
		widget.close()

	def buttonClicked2():
		widget.close()
		sys.exit()
		pygame.quit()
		

	while win2 == 0:	
		color = 1
		win = 0
		time = 0
		app[i] = QApplication(sys.argv)
		layout=QtGui.QGridLayout()
		widget=QtGui.QWidget()
		widget.setLayout(layout)
		widget.resize(500, 200)
		widget.move(400, 150)
		widget.setWindowTitle("Choose your color!")
		color_group=QtGui.QButtonGroup(widget)
		radiobutton1 = QtGui.QRadioButton("Black")
		radiobutton2 = QtGui.QRadioButton("white")
		radiobutton1.setChecked(True)
		color_group.addButton(radiobutton1)
		color_group.addButton(radiobutton2)
		layout.addWidget(radiobutton1,0,0)
		layout.addWidget(radiobutton2,0,1)

		lv_group=QtGui.QButtonGroup(widget)
		lvradiobutton1 = QtGui.QRadioButton("Normal")
		lvradiobutton2 = QtGui.QRadioButton("Hard")
		lvradiobutton3 = QtGui.QRadioButton("Chaos")
		lvradiobutton1.setChecked(True)
		lv_group.addButton(lvradiobutton1)
		lv_group.addButton(lvradiobutton2)
		lv_group.addButton(lvradiobutton3)
		layout.addWidget(lvradiobutton1,1,0)
		layout.addWidget(lvradiobutton2,1,1)
		layout.addWidget(lvradiobutton3,1,2)

		label1=QLabel(widget)
		label1.setText("The Black can't put in")
		label2=QLabel(widget)
		label2.setText("1.three and three")		
		label3=QLabel(widget)
		label3.setText("2.four and four")		
		layout.addWidget(label1,2,0)
		layout.addWidget(label2,2,1)
		layout.addWidget(label3,2,2)

		button = QPushButton(widget)
		button.setText("Start!!!")
		layout.addWidget(button,3,1)
		button.clicked.connect(buttonClicked)
		button2 = QPushButton(widget)
		button2.setText("Finish Game")
		layout.addWidget(button2,3,2)
		button2.clicked.connect(buttonClicked2)
		widget.show()
		app[i].exec_()

		
		game = Gomoku()
		game.loop()

		if game.loop() == 0:
			print 123
			#game.pygame.quit()
			win2=0
			i=i+1

























