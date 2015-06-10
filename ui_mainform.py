#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    """docstring for MainForm"""
    def __init__(self):
        super(MainForm, self).__init__()

        mainLayout = QVBoxLayout()
        self.resize(320, 240)
               
        view = QGraphicsView()
        view.resize(self.size())

        commandEdit = QLineEdit()
        commandEdit.setFont(QFont("Courier"))
        commandEdit.returnPressed.connect(self.close)
        

        mainLayout.addWidget(view)
        mainLayout.addWidget(commandEdit)
        self.setLayout(mainLayout)



