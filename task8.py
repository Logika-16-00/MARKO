from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(600,300)
window.setWindowTitle("Crazy people")


text_qt = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
btn1 = QRadioButton("PewDiePie")
btn2 = QRadioButton("Рет і Лінк")
btn3 = QRadioButton("SlivkiShow")
btn4 = QRadioButton("TheBrianMaps")
btn5 = QRadioButton("Mister Max")
btn6 = QRadioButton("EeOneGuy")
line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line.addWidget(text_qt, alignment = Qt.AlignCenter)
line1.addWidget(btn1,alignment = Qt.AlignCenter)
line1.addWidget(btn2,alignment = Qt.AlignCenter)
line2.addWidget(btn3,alignment = Qt.AlignCenter)
line2.addWidget(btn4,alignment = Qt.AlignCenter)
line3.addWidget(btn5,alignment = Qt.AlignCenter)
line3.addWidget(btn6,alignment = Qt.AlignCenter)
line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
def show_win():
    window_win = QMessageBox()
    window_win.setText("Ви виграли зустріч з творцями каналу!")
    window_win.exec_()
def show_lose():
    window_lose = QMessageBox()
    window_lose.setText("Пощастить іншим разом!")
    window_lose.exec_()
btn1.clicked.connect(show_win)
btn2.clicked.connect(show_lose)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)
btn5.clicked.connect(show_lose)
btn6.clicked.connect(show_lose)
window.setLayout(line)

window.show()
app.exec_()