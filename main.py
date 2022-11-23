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
        rad = random.randint(1, 200)
        r, g, b = [random.randint(0, 255) for i in range(3)]
        self.c.append(((r, g, b), QRect(x - rad, y - rad, rad, rad)))
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        for color, rect in self.c:
            r, g, b = color
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
