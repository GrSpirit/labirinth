#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import io

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, value, left_node=None, right_node=None):
        super(TreeNode, self).__init__()
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


class TreeLeaf(TreeNode):
    """docstring for TreeLeaf"""
    def __init__(self, value):
        super(TreeLeaf, self).__init__(value)

      
class Expression(object):
    """Alegbraic Expression"""
    #command_type = {
    #    'action': ['up', 'down', 'left', 'right'],
    #    'calc': ['+', '*']
    #}
    def __init__(self):
        super(Expression, self).__init__()

    def build(self, string):
        self.string = string
        self._istr = io.StringIO(string)
        self._next = self._istr.read(1)
        self._token = ''
        self.root = self.read_add()

    def read_next(self):
        self._token = self._next
        self._next = self._istr.read(1)

        # Skip spaces
        while self._token == ' ':
	        self._token = self._next
	        self._next = self._istr.read(1)

        if self._token.isalnum():
	        while self._next.isalnum():
	        	self._token += self._next
	        	self._next = self._istr.read(1)

        return self._token

    def read_add(self):
    	node = self.read_mult()
    	while self._token in ['+', '-']:
    		x = self._token
    		node = TreeNode(x, node, self.read_mult())
    	return node

    def read_mult(self):
    	self.read_next()
    	node = TreeLeaf(self._token)
    	self.read_next()
    	while self._token in ['*', '/']:
    		x = self._token
    		self.read_next()
    		if self._token.isalnum():
    			node = TreeNode(x, node, TreeLeaf(self._token))
    			self.read_next()
    		else:
    			raise Exception()

    	return node


def print_tree(node):
	if isinstance(node, TreeLeaf):
		return node.value
	else:
		return str.format("({0}{2}{1})", print_tree(node.left_node), print_tree(node.right_node), node.value)

def test():
	ex = Expression("   л + р*2 + п*в  ")
	ex.build()
	print(print_tree(ex.root))

def build(string):
	ex = Expression()
	ex.build(string)
	return ex.root