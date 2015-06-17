#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
#from PyQt5.QtWidgets import QApplication, qApp
import gettext
from PyQt4.QtGui import QApplication, qApp
from ui_mainform import MainForm

#basepath = os.path.abspath(os.path.dirname(sys.argv[0]))
basepath = os.path.abspath(os.path.dirname(__file__))
localedir = os.path.join(basepath, 'locale')
lang = gettext.translation('main', localedir=localedir, languages=['ru'])
lang.install('main')

def main():
    mainform = MainForm()
    mainform.show()
    qApp.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(main())
