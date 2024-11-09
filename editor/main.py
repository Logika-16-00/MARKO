from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PyQt5.QtWidgets import QFileDialog
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = Image.open("Губка_БОБ_персонаж.png")
        self.update_image()
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_right.clicked.connect(self.rotate_right)
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_bw.clicked.connect(self.bw_image)
        self.ui.btn_sharp.clicked.connect(self.sharpen_image)
        # self.image = Image.open("")
    def update_image(self):
        self.ui.label.hide()
        self.image.save("Губка_БОБ_персонаж_copy.png")
        pixmap = QPixmap("Губка_БОБ_персонаж_copy.png")
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pixmap.scaled(w, h)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()


    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.update_image()

    
    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.update_image()


    def flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def bw_image(self):
        self.image = self.image.convert("L")
        self.update_image()

    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.update_image()


    def choose_dir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory(self)

        print(workdir)
    def filter(self,files,ext):
        res = []
        for file in files:
            for e in ext:
                if file.endswitch(e):
                    res.append(file)
        return res        
        
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()



