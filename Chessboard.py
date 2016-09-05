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
				if self.set_piece(r, c):
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
					else:
						color = (255, 255, 255)

					x = self.start_x + c * self.grid_size
					y = self.start_y + r * self.grid_size
					pygame.draw.circle(screen, color, [x, y], self.grid_size // 2)





























