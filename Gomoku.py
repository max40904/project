# -*- coding: utf-8 -*- 
import sys
from PyQt4.QtGui import *
import pygame
import Chessboard
import Referee
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
			if self.chessboard.game_over:
				print '><'
				return 0
		pygame.quit()

	def update(self):
		global color
		global ai
		global time
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

					self.chessboard.handle_key_event(e)
					
					print self.chessboard.grid
					judge.input(self.chessboard.grid,self.chessboard.nowstep)
					self.draw()			
					if self.chessboard.winner ==None:
						before_eight = judge.Before_Eight()
						y_estimate = ai.ReturnAIAnw_beforeeight(self.chessboard.grid, 0.5,before_eight)
						print y_estimate
						self.chessboard.set_piece(y_estimate/15,y_estimate%15)
						judge.input(self.chessboard.grid,self.chessboard.nowstep)
						self.chessboard.check_win(y_estimate/15,y_estimate%15)
		else:
			if time == 0:
				self.chessboard.set_piece(7,7)
				judge.input(self.chessboard.grid,self.chessboard.nowstep)

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
						self.draw()
						if self.chessboard.winner ==None:
							before_eight = judge.Before_Eight()
							y_estimate = ai.ReturnAIAnw_beforeeight(self.chessboard.grid, 1,before_eight)
							print y_estimate
							
							self.chessboard.set_piece(y_estimate/15,y_estimate%15)
							judge.input(self.chessboard.grid,self.chessboard.nowstep)

							self.chessboard.check_win(y_estimate/15,y_estimate%15)

	def draw(self):
		global win
		global color
		self.screen.fill((255, 255, 255))
		self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))	
		self.chessboard.draw(self.screen)

		for i in range (15):
			x = i+1
			font = pygame.font.Font(None,20)
			game.screen.blit(font.render(str(x), True, (0,128,255)), (410,i*26+46))
			y = i+97	
			game.screen.blit(font.render(chr(y), True, (255,0,0)), (i*26+26,430))

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


if __name__ == '__main__':
	win2 = 0
	i=0
	app={}
	i2=0
	appx={}
	endbutton={}
	learning_rate = 0.0003
	input_stack = 56
	step_check_crossenropy = 100
	k_filter = input_stack * 3
	seed = 30


	Data = DataCenter.MongoDB()
	Cnn =  Policy.PolicyNetwork(learning_rate, input_stack, k_filter,seed) 
	ai = AI.Ai(Cnn,input_stack)
	Cnn.restore("./Neural_network_save/save_net530000.ckpt")
	judge = Referee.referee()
	
	def buttonClicked():
		global color
		if(radiobutton1.isChecked()):
			color = 1
			print 123
		elif(radiobutton2.isChecked()):
			color = 0.5
			print 123
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
		button2 = QPushButton(widget)
		button2.setText("Finish Game")
		button2.move(150,160)
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


























