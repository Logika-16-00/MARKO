from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Crazy people")


text_qt = QLabel("В якому році канал отримав золоту кнопку від YouTube?")
btn1 = QRadioButton("2005")
btn2 = QRadioButton("2015")
btn3 = QRadioButton("2010")
btn4 = QRadioButton("2020")
line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line.addWidget(text_qt, alignment = Qt.AlignCenter)
line1.addWidget(btn1,alignment = Qt.AlignCenter)
line1.addWidget(btn2,alignment = Qt.AlignCenter)
line2.addWidget(btn3,alignment = Qt.AlignCenter)
line2.addWidget(btn4,alignment = Qt.AlignCenter)
line.addLayout(line1)
line.addLayout(line2)
def show_win():
    window_win = QMessageBox()
    window_win.setText("Правильно! Ви виграли гіроскутер")
    window_win.exec_()
def show_lose():
    window_lose = QMessageBox()
    window_lose.setText("Ні, в 2015 році. Ви виграли фірмовий плакат")
    window_lose.exec_()
btn2.clicked.connect(show_win)
btn1.clicked.connect(show_lose)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)
window.setLayout(line)

window.show()
app.exec_()