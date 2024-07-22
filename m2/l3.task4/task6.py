from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint
money  = 0
def click():
    global money
    money = money + 1
    money.setText(str(money)+"$")
    
app = QApplication([])
win1 = QWidget()
win1.resize(500,250)
win1.move(250,150)
win1.setWindowTitle("Clicker")

text = QLabel("Money:")
money = QLabel("0")
button = QPushButton("Click")
button.clicked.connect(click)
line = QVBoxLayout()
line.addWidget(button)
line.addWidget(text)
line.addWidget(money)
win1.setLayout(line)
win1.show()
app.exec_()