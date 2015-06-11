#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPen, QColor
from PyQt5.Qt import *
from cells import *

class MainForm(QWidget):
    """docstring for MainForm"""
    def __init__(self, grid):
        super(MainForm, self).__init__()
        self.grid = grid

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self.resize(320, 240)
        
        self.cell_height = 20
        self.cell_width = 20

        self.scene = QGraphicsScene()
        self.pen = QPen(Qt.green)
        self.wall_pen = QPen(Qt.black)
        self.wall_pen.setWidth(2)

        self.scene.addLine(0,0,0,20, self.pen)
        view = QGraphicsView()
        view.resize(self.size())
        view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        #view.setScene(self.scene)

        commandEdit = QLineEdit()
        commandEdit.setFont(QFont("Courier"))
        commandEdit.returnPressed.connect(self.drawGrid)

        mainLayout.addWidget(view)
        mainLayout.addWidget(commandEdit)

    def drawGrid(self):
        for h in range(self.grid.height):
            for w in range(self.grid.width):
                x1 = w * self.cell_width
                y1 = h * self.cell_height
                x2 = (w + 1) * self.cell_width
                y2 = (h + 1) * self.cell_height
                #self.scene.addRect(x, y, self.cell_width, self.cell_height, self.pen)

                pen = self.wall_pen if self.grid.cells[h][w].left_wall.is_on else self.pen
                self.scene.addLine(x1, y1, x1, y2, pen)

                pen = self.wall_pen if self.grid.cells[h][w].right_wall.is_on else self.pen
                self.scene.addLine(x2, y1, x2, y2, pen)

                pen = self.wall_pen if self.grid.cells[h][w].top_wall.is_on else self.pen
                self.scene.addLine(x1, y1, x2, y1, pen)

                pen = self.wall_pen if self.grid.cells[h][w].bot_wall.is_on else self.pen
                self.scene.addLine(x1, y2, x2, y2, pen)





