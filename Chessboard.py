# -*- coding: utf-8 -*- 
import pygame
import sys
from PyQt4.QtGui import *

class Chessboard:

	def __init__(self):
		self.grid_size = 26
		self.start_x, self.start_y = 30, 50
		self.edge_size = self.grid_size / 2 
		self.grid_count = 15
		self.piece = 1
		self.winner = None
		self.game_over = False
		self.nowstep = 0

		self.grid = [[0 for i in range(15)] for j in range(15)]

	def handle_key_event(self, e):
		origin_x = self.start_x - self.edge_size
		origin_y = self.start_y - self.edge_size
		size = (self.grid_count - 1) * self.grid_size + self.edge_size * 2
		pos = e.pos
		if origin_x <= pos[0] <= origin_x + size and origin_y <= pos[1] <= origin_y + size:
			if not self.game_over:
				x = pos[0] - origin_x
				y = pos[1] - origin_y
				r = int(y // self.grid_size)
				c = int(x // self.grid_size)
				if self.set_piece(r,c):
					self.check_win(r, c)
	
	def set_piece(self, r, c):
		if self.grid[r][c] == 0:
			self.grid[r][c] = self.piece
			self.nowstep = r*15+c

			if self.piece == 1:
				self.piece = 0.5
			else:
				self.piece = 1

			return True
		return False

	def check_win(self, r, c):
		n_count = self.get_continuous_count(r, c, -1, 0)
		s_count = self.get_continuous_count(r, c, 1, 0)

		e_count = self.get_continuous_count(r, c, 0, 1)
		w_count = self.get_continuous_count(r, c, 0, -1)

		se_count = self.get_continuous_count(r, c, 1, 1)
		nw_count = self.get_continuous_count(r, c, -1, -1)

		ne_count = self.get_continuous_count(r, c, -1, 1)
		sw_count = self.get_continuous_count(r, c, 1, -1)

		if (n_count + s_count + 1 >= 5) or (e_count + w_count + 1 >= 5) or (se_count + nw_count + 1 >= 5) or (ne_count + sw_count + 1 >= 5):
			self.winner = self.grid[r][c]
			self.game_over = True
	
	def check_three(self,r,c):
		if self.grid[r][c] != 0:
			return False

		self.grid[r][c] = 1
		piece = 1
		count = 0
		print piece
		print count
		for i in range (5):
			if r-i>=0 and r-i+4<15 and c>=0 and c<15:
				if self.grid[r-i][c]==0  and self.grid[r-i+1][c]==piece and self.grid[r-i+2][c]==piece and self.grid[r-i+3][c]==piece and self.grid[r-i+4][c]==0:
					count += 1
		print count			
		for i in range (5):
			if r-i>=0 and r-i+4<15 and c-i>=0 and c-i+4<15:
				if self.grid[r-i][c-i]==0  and self.grid[r-i+1][c-i+1]==piece and self.grid[r-i+2][c-i+2]==piece and self.grid[r-i+3][c-i+3]==piece and self.grid[r-i+4][c-i+4]==0:
					count += 1
		print count			
		for i in range (5):
			if r>=0 and r<15 and c-i>=0 and c-i+4<15:
				if self.grid[r][c-i]==0  and self.grid[r][c-i+1]==piece and self.grid[r][c-i+2]==piece and self.grid[r][c-i+3]==piece and self.grid[r][c-i+4]==0:
					count += 1
		print count			
		for i in range (5):
			if r+i-4>=0 and r+i<15 and c-i>=0 and c-i+4<15:
				if self.grid[r+i][c-i]==0  and self.grid[r+i-1][c-i+1]==piece and self.grid[r+i-2][c-i+2]==piece and self.grid[r+i-3][c-i+3]==piece and self.grid[r+i-4][c-i+4]==0:
					count += 1
		
		print count
		
		for i in range (4):
			if r-i-1>=0 and r-i+4<15 and c>=0 and c<15:
				if self.grid[r-i-1][c]==0  and self.grid[r-i][c]==piece and self.grid[r-i+1][c]==piece and self.grid[r-i+2][c]==0 and self.grid[r-i+3][c]==piece and self.grid[r-i+4][c]==0:
					count += 1
				if self.grid[r-i-1][c]==0  and self.grid[r-i][c]==piece and self.grid[r-i+1][c]==0 and self.grid[r-i+2][c]==piece and self.grid[r-i+3][c]==piece and self.grid[r-i+4][c]==0:
					count += 1
		print count			
		for i in range (4):
			if r-i-1>=0 and r-i+4<15 and c-i-1>=0 and c-i+4<15:
				if self.grid[r-i-1][c-i-1]==0  and self.grid[r-i][c-i]==piece and self.grid[r-i+1][c-i+1]==piece and self.grid[r-i+2][c-i+2]==0 and self.grid[r-i+3][c-i+3]==piece and self.grid[r-i+4][c-i+4]==0:
					count += 1
				if self.grid[r-i-1][c-i-1]==0  and self.grid[r-i][c-i]==piece and self.grid[r-i+1][c-i+1]==0 and self.grid[r-i+2][c-i+2]==piece and self.grid[r-i+3][c-i+3]==piece and self.grid[r-i+4][c-i+4]==0:
					count += 1
		print count			
		for i in range (4):
			if r>=0 and r<15 and c-i-1>=0 and c-i+4<15:
				if self.grid[r][c-i-1]==0 and self.grid[r][c-i]==piece  and self.grid[r][c-i+1]==piece and self.grid[r][c-i+2]==0 and self.grid[r][c-i+3]==piece and self.grid[r][c-i+4]==0:
					count += 1
				if self.grid[r][c-i-1]==0 and self.grid[r][c-i]==piece  and self.grid[r][c-i+1]==0 and self.grid[r][c-i+2]==piece and self.grid[r][c-i+3]==piece and self.grid[r][c-i+4]==0:
					count += 1
		print count			
		for i in range (4):
			if r+i-4>=0 and r+i+1<15 and c-i-1>=0 and c-i+4<15:
				if self.grid[r+i+1][c-i-1]==0  and self.grid[r+i][c-i]==piece  and self.grid[r+i-1][c-i+1]==piece and self.grid[r+i-2][c-i+2]==0 and self.grid[r+i-3][c-i+3]==piece and self.grid[r+i-4][c-i+4]==0:
					count += 1
				if self.grid[r+i+1][c-i-1]==0  and self.grid[r+i][c-i]==piece  and self.grid[r+i-1][c-i+1]==0 and self.grid[r+i-2][c-i+2]==piece and self.grid[r+i-3][c-i+3]==piece and self.grid[r+i-4][c-i+4]==0:
					count += 1	

		print count
		self.grid[r][c] = 0
		if count > 1:
			print 789
			return False

		return True
					
	def get_continuous_count(self, r, c, dr, dc):
		piece = self.grid[r][c]
		result = 0
		i = 1
		while True:
			new_r = r + dr * i
			new_c = c + dc * i
			if 0 <= new_r < self.grid_count and 0 <= new_c < self.grid_count:
				if self.grid[new_r][new_c] == piece:
					result += 1
				else:
					break
			else:
				break
			i += 1
		return result

	def draw(self, screen):
		# 棋盤底色
		pygame.draw.rect(screen, (185, 122, 87),
						 [self.start_x - self.edge_size, self.start_y - self.edge_size,
						  (self.grid_count - 1) * self.grid_size + self.edge_size * 2, (self.grid_count - 1) * self.grid_size + self.edge_size * 2], 0)

		for r in range(self.grid_count):
			y = self.start_y + r * self.grid_size
			pygame.draw.line(screen, (0, 0, 0), [self.start_x, y], [self.start_x + self.grid_size * (self.grid_count - 1), y], 2)

		for c in range(self.grid_count):
			x = self.start_x + c * self.grid_size
			pygame.draw.line(screen, (0, 0, 0), [x, self.start_y], [x, self.start_y + self.grid_size * (self.grid_count - 1)], 2)

		for r in range(self.grid_count):
			for c in range(self.grid_count):
				#print r,c,self.grid[r][c]
				piece = self.grid[r][c]
				if piece == 0:
					#print "@@"
					x = self.start_x + c * self.grid_size
					y = self.start_y + r * self.grid_size
					if r==3 and c==3:
						pygame.draw.circle(screen, (0, 0, 0), [x, y], self.grid_size // 4)
					elif r==3 and c==11:
						pygame.draw.circle(screen, (0, 0, 0), [x, y], self.grid_size // 4)
					elif r==11 and c==3:
						pygame.draw.circle(screen, (0, 0, 0), [x, y], self.grid_size // 4)
					elif r==11 and c==11:
						pygame.draw.circle(screen, (0, 0, 0), [x, y], self.grid_size // 4)
					elif r==7 and c==7:
						pygame.draw.circle(screen, (0, 0, 0), [x, y], self.grid_size // 4)
				elif piece != 0:
					if piece == 1:
						color = (0, 0, 0)
						x = self.start_x + c * self.grid_size
						y = self.start_y + r * self.grid_size
						pygame.draw.circle(screen, color, [x, y], self.grid_size // 2)
						pygame.draw.circle(screen, (10,10,10), [x-4, y-4], self.grid_size // 3)
						pygame.draw.circle(screen, (20,20,20), [x-4, y-4], self.grid_size // 4)
						pygame.draw.circle(screen, (30,30,30), [x-4, y-4], self.grid_size // 5)
						pygame.draw.circle(screen, (40,40,40), [x-4, y-4], self.grid_size // 6)
						pygame.draw.circle(screen, (50,50,50), [x-4, y-4], self.grid_size // 7)
						pygame.draw.circle(screen, (60,60,60), [x-4, y-4], self.grid_size // 8)
					else:
						color = (200, 200, 200)
						x = self.start_x + c * self.grid_size
						y = self.start_y + r * self.grid_size
						pygame.draw.circle(screen, color, [x, y], self.grid_size // 2)
						pygame.draw.circle(screen, (210,210,210), [x-1, y-1], self.grid_size // 2-1)
						pygame.draw.circle(screen, (220,220,220), [x-2, y-2], self.grid_size // 2-2)
						pygame.draw.circle(screen, (230,230,230), [x-3, y-3], self.grid_size // 2-3)
						pygame.draw.circle(screen, (240,240,240), [x-3, y-3], self.grid_size // 2-4)
						pygame.draw.circle(screen, (250,250,250), [x-3, y-3], self.grid_size // 2-5)
						pygame.draw.circle(screen, (255,255,255), [x-3, y-3], self.grid_size // 2-6)

					






























