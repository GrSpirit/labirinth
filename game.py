#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from cells import Grid

class Point(object):
    """docstring for Point"""
    def __init__(self, x=0, y=0):
        super(Point, self).__init__()
        self.x = x
        self.y = y        

class Game(object):
    """docstring for Game"""
    def __init__(self):
        super(Game, self).__init__()
        self.grid = Grid()
        self.start_pos = Point()
        self.target_pos = Point()
        
    def loadMap(self, file_name):
        with open(file_name, 'r') as map_file:
            # Read size
            s = map_file.readline()
            (width, height) = map(lambda x: int(x), s.strip().split(' '))

            # Read start position
            s = map_file.readline()
            (self.start_pos.x, self.start_pos.y) = map(lambda x: int(x), s.strip().split(' '))

            # Read target position
            s = map_file.readline()
            (self.target_pos.x, self.target_pos.y) = map(lambda x: int(x), s.strip().split(' '))

            # Read map
            s = map_file.read().replace('\n', '').replace(' ', '')
            self.grid = Grid(width, height)
            self.grid.load_cells(s)
        