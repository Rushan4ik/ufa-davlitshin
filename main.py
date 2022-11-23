import random
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QRect
from PyQt5.uic import loadUi


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.c = []
        loadUi("UI.ui", self)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(800, 800)
        self.pushButton.clicked.connect(self.handle)

    def handle(self):
        x, y = random.randint(200, 800), random.randint(200, 800)
        r = random.randint(1, 200)
        self.c.append(QRect(x - r, y - r, r, r))
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        for rect in self.c:
            r, g, b = 255, 255, 0
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(rect)
        painter.end()


def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()


if __name__ == '__main__':
    main()
