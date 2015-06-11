#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from ui_mainform import MainForm
from cells import *

def main():
    app = QApplication(sys.argv)
    mainform = MainForm(Grid(3,3))
    mainform.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
