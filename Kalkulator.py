import functools
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, \
    QLineEdit, QGridLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 900, 900)
        self.setFixedSize(450, 450)
        self.setWindowTitle('Przyciski 0-9')

    # 0,0 0,1 0,2 | 7 8 9
    # 1,0 1,1 1,2 | 4 5 6
    # 2,0 2,1 2,2 | 1 2 3
    # 3,0 2,1 2,2 |   0


        gridLayout = QGridLayout(self)

        for i in range(0, 10, 1):

            self.btn = QPushButton(str(i), self)
            self.btn.setFixedHeight(100)
            self.btn.setFont(QFont('Segoe', 40, QFont.Bold))
            if i == 0:
                gridLayout.addWidget(self.btn, 3, 0, 1, 3)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '0'))
            if i == 1:
                gridLayout.addWidget(self.btn, 2, 0)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '1'))
            if i == 2:
                gridLayout.addWidget(self.btn, 2, 1)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '2'))
            if i == 3:
                gridLayout.addWidget(self.btn, 2, 2)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '3'))
            if i == 4:
                gridLayout.addWidget(self.btn, 1, 0)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '4'))
            if i == 5:
                gridLayout.addWidget(self.btn, 1, 1)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '5'))
            if i == 6:
                gridLayout.addWidget(self.btn, 1, 2)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '6'))
            if i == 7:
                gridLayout.addWidget(self.btn, 0, 0)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '7'))
            if i == 8:
                gridLayout.addWidget(self.btn, 0, 1)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '8'))
            if i == 9:
                gridLayout.addWidget(self.btn, 0, 2)
                self.btn.clicked.connect(functools.partial(self.showMsgBox, '9'))

        self.show()


    def showMsgBox(self, i):
        msg = QMessageBox()
        msg.setText('Button '+i)
        msg.setWindowTitle('Message Box')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

