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
points_label = QLabel("Очки: 0")
points = 50
line = QVBoxLayout()
main_win.resize(400,400)
line.addWidget(text)
line.addWidget(winner)
line.addWidget(winner1)
line.addWidget(points_label)
line.addWidget(bt)
main_win.setLayout(line)

def show_numbers():
    global points
    number1 = randint(0, 9)
    number2 = randint(0, 9)
    winner.setText(str(number1))
    winner1.setText(str(number2))
    if number1 == number2:
        
        points -=10
        text.setText("Ви виграли! Зіграйте знову")
        points += 40
    else:
        points -=10
        text.setText("Ви програли! Зіграйте знову")
        points -= 20

        
    points_label.setText(f"Очки: {points}")

bt.clicked.connect(show_numbers)

main_win.show()
app.exec_()
