#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import io

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, value, leftNode=None, rightNode=None):
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
    def __init__(self, string):
        super(Expression, self).__init__()
        self.string = string
        self.istr = io.StringIO(string)
        self.next = self.istr.read(1)
        self.token = ''

    def build(self):
        self.root = self.read_add()

    def read_next(self):
        self.token = self.next
        self.next = self.istr.read(1)

        # Skip spaces
        while self.token = ' ':
	        self.token = self.next
	        self.next = self.istr.read(1)

        if self.token.isalnum():
	        while self.next.isalnum():
	        	self.token += self.next
	        	self.next = self.istr.read(1)

        return self.token

    def read_add(self):
    	node = self.read_mult()
    	while self.token in ['+', '-']:
    		x = self.token
    		node = TreeNode(x, node, self.read_mult())
    	return node

    def read_mult(self):
    	self.read_next()
    	node = TreeLeaf(self.token)
    	self.read_next()
    	while self.token in ['*', '/']:
    		x = self.token
    		self.read_next()
    		if self.token.isalnum():
    			node = TreeNode(x, node, TreeLeaf(self.token))
    			self.read_next()
    		else:
    			raise Exception()

    	return node


def print_tree(node):
	if isinstance(node, TreeLeaf)
	print_tree(node.left, node.right)

def test():
	ex = Expression("a+b*2+4*d")
	ex.build()
