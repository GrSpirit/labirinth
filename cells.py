#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class NoCellError(Exception):
	def __init__(self, message):
		super(NoCellError, self).__init__()
		self.message = message

class FaceWallError(object):
	"""docstring for FaceWallError"""
	def __init__(self, message):
		super(FaceWallError, self).__init__()
		self.message = message
		

class Wall(object):
	"""Wall between cells"""
	def __init__(self, is_on=False):
		super(Wall, self).__init__()
		self.is_on = is_on

class VWall(Wall):
	"""VWall is a vertical wall"""
	def __init__(self, is_on=False, left_cell=None, right_cell=None):
		super(VWall, self).__init__(is_on)
		self.left_cell = left_cell
		self.right_cell = right_cell
		
class HWall(Wall):
	"""HWall is a horizontal wall"""
	def __init__(self, is_on=False, top_cell=None, bot_cell=None):
		super(HWall, self).__init__(is_on)
		self.top_cell = top_cell
		self.bot_cell = bot_cell

class Cell(object):
	"""Cell on the map"""
	def __init__(self, left_wall=None, right_wall=None, top_wall=None, bot_wall=None):
		super(Cell, self).__init__()
		self.left_wall = left_wall
		self.right_wall = right_wall
		self.top_wall = top_wall
		self.bot_wall = bot_wall

	@property
	def left_wall(self):
	    return self.__left_wall

	@left_wall.setter
	def left_wall(self, wall):
		self.__left_wall = wall
		if wall: wall.right_cell = self
	
	@property
	def right_wall(self):
	    return self.__right_wall

	@right_wall.setter
	def right_wall(self, wall):
		self.__right_wall = wall
		if wall: wall.left_cell = self

	@property
	def top_wall(self):
	    return self.__top_wall

	@top_wall.setter
	def top_wall(self, wall):
		self.__top_wall = wall
		if wall: wall.bot_cell = self

	@property
	def bot_wall(self):
	    return self.__bot_wall

	@bot_wall.setter
	def bot_wall(self, wall):
		self.__bot_wall = wall
		if wall: wall.top_cell = self
		
	def test_left_wall(self):
		return self.left_wall.is_on if self.left_wall else True

	def test_right_wall(self):
		return self.right_wall.is_on if self.right_wall else True

	def test_top_wall(self):
		return self.top_wall.is_on if self.top_wall else True

	def test_bot_wall(self):
		return self.bot_wall.is_on if self.bot_wall else True

	@property
	def left_cell(self):
		if self.test_left_wall():
			raise FaceWallError('Faced the left wall')
		if self.left_wall.left_cell is None:
			raise NoCellError('No left cell')
		return self.left_wall.left_cell 

	@property
	def right_cell(self):
		if self.test_right_wall():
			raise FaceWallError('Faced the right wall')
		if self.right_wall.right_cell is None:
			raise NoCellError('No right cell')
		return self.right_wall.right_cell 
	
	@property
	def top_cell(self):
		if self.test_top_wall():
			raise FaceWallError('Faced the top wall')
		if self.top_wall.top_cell is None:
			raise NoCellError('No top cell')
		return self.top_wall.top_cell 
	
	@property
	def bot_cell(self):
		if self.test_bot_wall():
			raise FaceWallError('Faced the bot wall')
		if self.bot_wall.bot_cell is None:
			raise NoCellError('No bot cell')
		return self.bot_wall.bot_cell 
	

class Grid(object):
	"""Grid of cells"""
	def __init__(self, width=0, height=0):
		super(Grid, self).__init__()
		self.width = width
		self.height = height
		if width > 0 and height > 0:
			self._init_cells()
		else:
			self.cells = []

	def _init_cells(self):
		self.cells = [[Cell() for x in range(self.width)] for y in range(self.height)]
		for h in range(self.height):
			for w in range(self.width):
				cell = self.cells[h][w]
				cell.left_wall = self.cells[h][w - 1].right_wall if w > 0 else VWall(True)
				cell.right_wall = VWall(w == self.width - 1)
				cell.top_wall = self.cells[h - 1][w].bot_wall if h > 0 else HWall(True)
				cell.bot_wall = HWall(h == self.height - 1)

	def load_cells(self, grid_map):
		for x in range(len(grid_map)):
			h = x // (self.width + self.width + 1)
			#if (x // (self.width + h // 2) % 2) == 0:
			if ((x - h) // self.width) == (h * 2):
				w = (x - h) % (self.width)
				print('1) h=', h, 'w=', w)
				if h < self.height:
					self.cells[h][w].top_wall.is_on = grid_map[x] != '0'
				else:
					self.cells[h - 1][w].bot_wall.is_on = grid_map[x] != '0'
			else: 
				w = (x - h) % (self.width) + (((x - h) // self.width + 1) % 2) * self.width
				print('2) h=', h, 'w=', w)
				if w < self.width:
					self.cells[h][w].left_wall.is_on = grid_map[x] != '0'
				else:
					self.cells[h][w - 1].right_wall.is_on = grid_map[x] != '0'
			
		

def cells_test():
	cell = Cell(top_wall=Wall(True))
	print(cell.test_left_wall())
	grid = Grid(3, 3)
	grid.load_cells("111100100010010001001111")

	for r in grid.cells:
		for c in r:
			print(c.left_wall.is_on)

