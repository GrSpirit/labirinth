#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, qApp
from ui_mainform import MainForm
from cells import *

def main():
    mainform = MainForm(Grid(3,3))
    mainform.show()
    qApp.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(main())
