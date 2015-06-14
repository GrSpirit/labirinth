#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPen, QColor
from PyQt5.Qt import *
from cells import *
from config import config
from game import Game

class MainForm(QWidget):
    """docstring for MainForm"""
    def __init__(self, grid):
        super(MainForm, self).__init__()
        self.game = Game()

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self.resize(320, 240)
        
        self.cell_height = config.cell_height
        self.cell_width = config.cell_width

        self.scene = QGraphicsScene()
        self.pen = QPen(Qt.green)
        self.wall_pen = QPen(Qt.black)
        self.wall_pen.setWidth(2)

        self.scene.addLine(0,0,0,20, self.pen)
        view = QGraphicsView()
        view.resize(self.size())
        view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        view.setScene(self.scene)

        self.commandEdit = QLineEdit()
        self.commandEdit.setFont(QFont("Courier"))
        self.commandEdit.returnPressed.connect(self.drawGrid)
        loadButton = QPushButton("Load")
        loadButton.clicked.connect(self.loadFile)

        commandLayout = QHBoxLayout()
        commandLayout.addWidget(self.commandEdit)
        commandLayout.addWidget(loadButton)

        mainLayout.addWidget(view)
        mainLayout.addLayout(commandLayout)
        self.commandEdit.setFocus()

    def drawGrid(self):
        self.scene.clear()
        grid = self.game.grid
        for h in range(grid.height):
            for w in range(grid.width):
                x1 = w * self.cell_width
                y1 = h * self.cell_height
                x2 = (w + 1) * self.cell_width
                y2 = (h + 1) * self.cell_height
                #self.scene.addRect(x, y, self.cell_width, self.cell_height, self.pen)

                pen = self.wall_pen if grid.cells[h][w].left_wall.is_on else self.pen
                self.scene.addLine(x1, y1, x1, y2, pen)

                pen = self.wall_pen if grid.cells[h][w].right_wall.is_on else self.pen
                self.scene.addLine(x2, y1, x2, y2, pen)

                pen = self.wall_pen if grid.cells[h][w].top_wall.is_on else self.pen
                self.scene.addLine(x1, y1, x2, y1, pen)

                pen = self.wall_pen if grid.cells[h][w].bot_wall.is_on else self.pen
                self.scene.addLine(x1, y2, x2, y2, pen)

    def loadFile(self):
        file_name = QFileDialog.getOpenFileName(self, "Open map", '', 'Map file (*.map)')[0]
        if file_name == '':
            return
        self.game.loadMap(file_name)
        self.drawGrid()



