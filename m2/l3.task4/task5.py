from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Лотерея')
bt = QPushButton("Випробувати удачу")
text = QLabel("Натисніть,щоб взяти участь")
winner = QLabel("?")
winner1 = QLabel("?")
line = QVBoxLayout()
main_win.resize(400,400)
line.addWidget(text)
line.addWidget(winner)
line.addWidget(winner1)
line.addWidget(bt)
main_win.setLayout(line)

def show_numbers():
    number1 = randint(0, 9)
    number2 = randint(0, 9)
    winner.setText(str(number1))
    winner1.setText(str(number2))
    if number1 == number2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")

bt.clicked.connect(show_numbers)

main_win.show()
app.exec_()