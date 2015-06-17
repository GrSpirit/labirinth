#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QFont, QPen, QColor
#from PyQt5.Qt import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4 import QtCore
from cells import TextException
from config import config
from game import Game

class MessageType():
    Error = QMessageBox.Critical


class MainForm(QWidget):
    """docstring for MainForm"""
    def __init__(self):
        super(MainForm, self).__init__()
        self.game = Game()

        # Settings
        self.cell_height = config.cell_height
        self.cell_width = config.cell_width
        self.point_size = config.point_size

        # Graphic scene
        self.scene = QGraphicsScene()
        self.pen = QPen(Qt.green)
        self.wall_pen = QPen(Qt.black)
        self.wall_pen.setWidth(2)
        self.start_pen = QPen(Qt.black)
        self.current_pen = QPen(Qt.red)
        self.current_pen.setWidth(2)
        self.target_pen = QPen(Qt.green)
        self.target_pen.setWidth(2)

        # Graphic view
        view = QGraphicsView()
        view.resize(self.size())
        view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        view.setScene(self.scene)

        # Commands
        self.commandEdit = QLineEdit()
        self.commandEdit.setFont(QFont("Courier"))
        loadButton = QPushButton(_("Load"))
        loadButton.clicked.connect(self.loadFile)
        loadShortcut = QShortcut(QKeySequence.Open, self)
        loadShortcut.activated.connect(self.loadFile)

        commandLayout = QHBoxLayout()
        commandLayout.addWidget(self.commandEdit)
        commandLayout.addWidget(loadButton)

        # Help text
        helpText = QLabel("{}\n{}\n{}\n{}\n{}".format(_("Commands:"), _("U = up"), _("D = down"), _("L = left"), _("R = right")))

        # Layout
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        helpLayout = QVBoxLayout()
        topLayout.addWidget(view)
        topLayout.addLayout(helpLayout)
        helpLayout.addWidget(helpText)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(commandLayout)
        self.setLayout(mainLayout)
        self.resize(320, 240)
        
        # Setup timer
        self.timer = QTimer(self)
        self.timer.setInterval(config.timer_interval)
        self.timer.timeout.connect(self.next_step)
        self.commandEdit.returnPressed.connect(self.start)

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

        
        # Start position
        (x, y) = (self.game.start_cell.x, self.game.start_cell.y)
        x = x * self.cell_width + (self.cell_width - self.point_size) / 2
        y = y * self.cell_height + (self.cell_height - self.point_size) / 2
        self.scene.addEllipse(x, y, self.point_size, self.point_size, self.start_pen)
        
        # Target position
        (x, y) = (self.game.target_cell.x, self.game.target_cell.y)
        x = x * self.cell_width + (self.cell_width - self.point_size) / 2
        y = y * self.cell_height + (self.cell_height - self.point_size) / 2
        self.scene.addEllipse(x, y, self.point_size, self.point_size, self.target_pen)

        # Current position
        (x, y) = (self.game.current_cell.x, self.game.current_cell.y)
        x = x * self.cell_width + (self.cell_width - self.point_size) / 2
        y = y * self.cell_height + (self.cell_height - self.point_size) / 2
        self.scene.addEllipse(x, y, self.point_size, self.point_size, self.current_pen)

    def loadFile(self):
        #file_name = QFileDialog.getOpenFileName(self, "Open map", '', 'Map file (*.map)')[0]
        file_name = QFileDialog.getOpenFileName(self, _("Open map"), '', _('Map file ({})').format('*.map'))
        if file_name == '': return
        self.game.loadMap(file_name)
        self.drawGrid()

    def showMessage(self, text, msg_type):
        msg_box = QMessageBox(self)
        msg_box.setText(text)
        msg_box.setIcon(msg_type)
        msg_box.show()

    def start(self):
        try:
            self.game.play(self.commandEdit.text())
            self.timer.start()
        except TextException as e:
            self.showMessage(e.message, MessageType.Error)
        except:
            self.showMessage(_("Unknown error"), MessageType.Error)

    def stop(self, message=''):
        self.timer.stop()
        msg_box = QMessageBox()
        if self.game.is_win():
            msg_box.setText(_("WIN!!!"))
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setText(_('LOSE'))
            if message:
                msg_box.setInformativeText(message)
            msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec_()
        self.game.reset()

    def next_step(self):
        try:
            if not self.game.next():
                self.stop()
            self.drawGrid()
        except TextException as e:
            self.stop(e.message)
        except:
            self.stop(_("Unknown error"))

