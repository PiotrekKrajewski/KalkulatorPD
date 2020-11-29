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

    # 0,0 0,1 0,2
    # 1,0 1,1 1,2
    # 2,0 2,1 2,2
    # 3,0 2,1 2,2

        #buttonNumber = 0

        #for i in range(0, 3, 1):
            #for j in range(0, 3, 1):

        gridLayout = QGridLayout(self)
        #tmpName = 'button'+str(buttonNumber)
        button0 = QPushButton('0', self)
        button0.setFixedHeight(80)
        button0.setFont(QFont('Segoe', 40, QFont.Bold))

        button1 = QPushButton('1', self)
        button1.setFixedHeight(80)
        button1.setFont(QFont('Segoe', 40, QFont.Bold))

        button2 = QPushButton('2', self)
        button2.setFixedHeight(80)
        button2.setFont(QFont('Segoe', 40, QFont.Bold))

        button3 = QPushButton('3', self)
        button3.setFixedHeight(80)
        button3.setFont(QFont('Segoe', 40, QFont.Bold))

        button4 = QPushButton('4', self)
        button4.setFixedHeight(80)
        button4.setFont(QFont('Segoe', 40, QFont.Bold))

        button5 = QPushButton('5', self)
        button5.setFixedHeight(80)
        button5.setFont(QFont('Segoe', 40, QFont.Bold))

        button6 = QPushButton('6', self)
        button6.setFixedHeight(80)
        button6.setFont(QFont('Segoe', 40, QFont.Bold))

        button7 = QPushButton('7', self)
        button7.setFixedHeight(80)
        button7.setFont(QFont('Segoe', 40, QFont.Bold))

        button8 = QPushButton('8', self)
        button8.setFixedHeight(80)
        button8.setFont(QFont('Segoe', 40, QFont.Bold))

        button9 = QPushButton('9', self)
        button9.setFixedHeight(80)
        button9.setFont(QFont('Segoe', 40, QFont.Bold))

        gridLayout.addWidget(button9, 0, 2)
        gridLayout.addWidget(button8, 0, 1)
        gridLayout.addWidget(button7, 0, 0)
        gridLayout.addWidget(button6, 1, 2)
        gridLayout.addWidget(button5, 1, 1)
        gridLayout.addWidget(button4, 1, 0)
        gridLayout.addWidget(button3, 2, 2)
        gridLayout.addWidget(button2, 2, 1)
        gridLayout.addWidget(button1, 2, 0)
        gridLayout.addWidget(button0, 3, 0, 1, 3)


        #buttonNumber = buttonNumber + 1

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

