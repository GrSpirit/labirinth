#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser

LOCALE = {
    'en': 'English',
    'ru': 'Русский'
}

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
    def default_section(self):
        if 'Default' not in self.parser: 
            self.parser['Default'] = {}
            self.save()
        return self.parser['Default']

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
    
    @property
    def locale(self):
        if 'locale' not in self.default_section:
            self.default_section['locale'] = 'ru'
            self.save()
        return self.default_section['locale']
    
    @property
    def domain(self):
        if 'domain' not in self.default_section:
            self.default_section['domain'] = 'main'
            self.save()
        return self.default_section['domain']

    @property
    def timer_interval(self):
        if 'timer' not in self.default_section:
            self.default_section['timer'] = '500'
            self.save()
        return int(self.default_section['timer'])

    
    
config = Config()
