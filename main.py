import random
import sqlite3
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QRect
from PyQt5.uic import loadUi


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.c = []
        loadUi("main.ui", self)
        self.init_data()
        self.init_ui()

    def init_data(self):
        connection = sqlite3.connect("coffee.sqlite")
        self.result = [data for data in connection.execute("select * from coffees").fetchall()]
        connection.close()

    def init_ui(self):
        for d in self.result:
            d = ', '.join(map(str, d))
            label = QLabel(d, self)
            label.setFixedSize(800, 20)
            self.verticalLayout.addWidget(label)


def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()


if __name__ == '__main__':
    main()
