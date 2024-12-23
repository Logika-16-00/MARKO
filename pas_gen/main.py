import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from calendarr.ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generation)
    
    def generation(self):
        signs = ''
        if self.ui.checkBox.isChecked():
            signs += '!@#$%^&*(){}"|<>?.,;:" '
        if self.ui.checkBox_2.isChecked():
            signs += 'qwertyuiopasdfghjklzxcvbnm'
        if self.ui.checkBox_3.isChecked():
            signs += '12345678890'
        res = ''
        number = random.randint(8,12)
        for i in range(number):
            res += random.choice(signs)
        self.ui.label.setText(res)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()