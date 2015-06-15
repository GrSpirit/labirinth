#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#from PyQt5.QtWidgets import QApplication, qApp
from cells import *
import gettext
import os

basepath = os.path.abspath(os.path.dirname(sys.argv[0]))
localedir = os.path.join(basepath, 'locale')
lang = gettext.translation('main', localedir=localedir, languages=['ru'])
lang.install('main')
#_ = gettext.gettext

from PyQt4.QtGui import QApplication, qApp
from ui_mainform import MainForm

def main():
    mainform = MainForm(Grid(3,3))
    mainform.show()
    qApp.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(main())
