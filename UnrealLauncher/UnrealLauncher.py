import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QPushButton, QLineEdit, QDialog
from PyQt5 import uic

import unreal_stylesheet


class UnrealUi(QDialog):
    def __init__(self):
        super(UnrealUi, self).__init__()

        unreal_stylesheet.setup() # Matches the UE5 style

        uic.loadUi("C:\\GitRepo\\UnrealTools\\UnrealLauncher\\UnrealLauncher.ui", self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnrealUi()
    window.show()
    app.exec_()
