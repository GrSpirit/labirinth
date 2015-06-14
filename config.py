#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser

class Config(object):
    """docstring for Config"""
    def __init__(self, config_file='labirinth.ini'):
        super(Config, self).__init__()
        self.config_file = config_file
        self.parser = ConfigParser()
        self.parser.read(self.config_file)

    def save(self):
        with open(self.config_file, 'w') as ofile:
            self.parser.write(ofile)

    @property
    def view_section(self):
        if 'View' not in self.parser: 
            self.parser['View'] = {}
            self.save()
        return self.parser['View']

    @property
    def cell_width(self):
        if 'cell_width' not in self.view_section: 
            self.view_section['cell_width'] = '20'
            self.save()
        return int(self.view_section['cell_width'])

    @property
    def cell_height(self):
        if 'cell_height' not in self.view_section: 
            self.view_section['cell_height'] = '20'
            self.save()
        return int(self.view_section['cell_height'])

    @property
    def point_size(self):
        if 'point_size' not in self.view_section: 
            self.view_section['point_size'] = '12'
            self.save()
        return int(self.view_section['point_size'])
    
    
    

config = Config()
