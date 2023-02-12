from PyQt6.QtWidgets import *
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(320, 300, 300, 300)
        self.setWindowTitle("Калькулятор")
        self.Firstwindow = QLineEdit()
        self.SeconfWindow = QLineEdit()
        self.Pbotomsum = QPushButton('+', self)
        self.Pbotomsum.clicked.connect(self.Summ)
        self.Pbotommin = QPushButton('-', self)
        self.Pbotommin.clicked.connect(self.Min)
        self.Pbotomdev = QPushButton('/', self)
        self.Pbotomdev.clicked.connect(self.Dev)
        self.Pbotommul = QPushButton('*', self)
        self.Pbotommul.clicked.connect(self.Mul)
        self.Qint = QLCDNumber(8)
        self.Qint.display(0)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.Qint.setMaximumSize(100, 50)

        self.grid.addWidget(self.Firstwindow, 1, 1)
        self.grid.addWidget(self.SeconfWindow, 1, 3)
        self.grid.addWidget(self.Qint, 2, 2)
        self.grid.addWidget(self.Pbotomdev, 3, 1)
        self.grid.addWidget(self.Pbotommul, 3, 3)
        self.grid.addWidget(self.Pbotomsum, 4, 1)
        self.grid.addWidget(self.Pbotommin, 4, 3)

    def Summ(self):
        First = int(self.Firstwindow.text())
        Second = int(self.SeconfWindow.text())
        self.Qint.display(First + Second)
    def Min(self):
        First = int(self.Firstwindow.text())
        Second = int(self.SeconfWindow.text())
        self.Qint.display(First - Second)
    def Dev(self):
        First = int(self.Firstwindow.text())
        Second = int(self.SeconfWindow.text())
        self.Qint.display(First / Second)
    def Mul(self):
        First = int(self.Firstwindow.text())
        Second = int(self.SeconfWindow.text())
        self.Qint.display(First * Second)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())