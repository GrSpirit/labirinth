#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from cells import Grid, Point, TextException
#import gettext
#_ = gettext.gettext

action_synonyms = {
    'up': ['u', 'U', 'в', 'В'],
    'left': ['l', 'L', 'л', 'Л'],
    'right': ['r', 'R', 'п', 'П'],
    'down': ['d', 'D', 'н', 'Н']
}

def action_name(cmd):
    for key, syn in action_synonyms.items():
        if cmd in syn:
            return key
    return ''


class UnknownCommand(TextException):
    """docstring for InvalidCommand"""
    def __init__(self, message):
        super(InvalidCommand, self).__init__(message)
        

class EmptyCommandStrError(TextException):
    """docstring for EmptyCommandStrError"""
    def __init__(self):
        super(EmptyCommandStrError, self).__init__(_("Empty command string"))


class EmptyGridError(TextException):
    """docstring for EmptyGridError"""
    def __init__(self):
        super(EmptyGridError, self).__init__(_("Empty grid"))


class Game(object):
    """Game"""
    def __init__(self):
        super(Game, self).__init__()
        self.grid = Grid()
        self.start_cell = None
        self.target_cell = None
        self.current_cell = None
        
        # Define actions
        self.actions = {
            'up': self.action_up,
            'down': self.action_down,
            'left': self.action_left,
            'right': self.action_right
        }

    def reset(self):
        self.current_cell = self.start_cell

    def loadMap(self, file_name):
        with open(file_name, 'r') as map_file:
            # Read size
            s = map_file.readline()
            (width, height) = map(lambda x: int(x), s.strip().split(' '))

            # Read start position
            start_point = Point()
            s = map_file.readline()
            (start_point.x, start_point.y) = map(lambda x: int(x), s.strip().split(' '))
 
            # Read target position
            target_point = Point()
            s = map_file.readline()
            (target_point.x, target_point.y) = map(lambda x: int(x), s.strip().split(' '))

            # Read map
            s = map_file.read().replace('\n', '').replace(' ', '')
            self.grid = Grid(width, height)
            self.grid.load_cells(s)
            self.start_cell = self.grid.cells[start_point.y][start_point.x]
            self.current_cell = self.start_cell
            self.target_cell = self.grid.cells[target_point.y][target_point.x]
   
    def play(self, command_str):
        self.command_str = command_str.strip()
        if len(self.command_str) == 0:
            raise EmptyCommandStrError()
        self.command_ptr = 0

        if self.grid.width == 0 or self.grid.height == 0:
            raise EmptyGridError()
        self.current_cell = self.start_cell

    def action_up(self):
        self.current_cell = self.current_cell.top_cell

    def action_down(self):
        self.current_cell = self.current_cell.bot_cell

    def action_left(self):
        self.current_cell = self.current_cell.left_cell

    def action_right(self):
        self.current_cell = self.current_cell.right_cell

    def is_win(self):
        return self.current_cell == self.target_cell

    def is_finish(self):
        return self.command_ptr >= len(self.command_str)

    def next(self):
        cmd = self.command_str[self.command_ptr]
        action = action_name(cmd)
        if not action:
            raise UnknownCommand(_("Unknown command: '{}'").format(cmd))
        self.actions[](action)
        self.command_ptr += 1
        return not self.is_finish()


def test():
    game = Game()
    game.actions['u']()