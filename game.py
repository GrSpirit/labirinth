#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from cells import Grid, Point, TextException

class InvalidCommand(TextException):
    """docstring for InvalidCommand"""
    def __init__(self, message):
        super(InvalidCommand, self).__init__(message)
        
class Game(object):
    """Game"""
    synonyms = {
        'up': ['u', 'U'],
        'left': ['l', 'L'],
        'right': ['r', 'R'],
        'down': ['d', 'D']
    }
    def __init__(self):
        super(Game, self).__init__()
        self.grid = Grid()
        self.start_pos = Point()
        self.target_pos = Point()
        self.current_cell = None
        
        # Define actions
        self.actions = {
            'up': self.action_up,
            'down': self.action_down,
            'left': self.action_left,
            'right': self.action_right
        }

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
            self.current_cell = self.grid.cells[self.start_pos.y][self.start_pos.x]
   
    def play(self, command_str):
        self.command_str = command_str
        self.command_ptr = 0
        self.current_cell = self.grid.cells[self.start_pos.y][self.start_pos.x]

    def action_name(cmd):
        for key, syn in Game.synonyms.items():
            if cmd in syn:
                return key
        raise InvalidCommand("Unknown command: " + cmd)

    def action_up(self):
        self.current_cell = self.current_cell.top_cell

    def action_down(self):
        self.current_cell = self.current_cell.bot_cell

    def action_left(self):
        self.current_cell = self.current_cell.left_cell

    def action_right(self):
        self.current_cell = self.current_cell.right_cell

    def is_win(self):
        return self.current_cell == self.target_pos

    def is_finish(self):
        return self.command_ptr >= len(self.command_str)

    def next(self):
        cmd = self.command_str[self.command_ptr]
        self.actions[Game.action_name(cmd)]()
        self.command_ptr += 1
        return not self.is_finish()


def test():
    game = Game()
    game.actions['u']()