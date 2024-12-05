from PyQt5.QtCore import QEvent
<<<<<<< HEAD
from PyQt5.QtWidgets import QApplication,QInputDialog, QFileDialog
=======
from PyQt5.QtWidgets import QApplication,QInputDialog,QMessageBox
>>>>>>> 74e5a7dedb0229dcc2583d649f10139a7dc2c3fa
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
<<<<<<< HEAD
import os


=======
from PyQt5.QtWidgets import QFileDialog
import os
>>>>>>> 74e5a7dedb0229dcc2583d649f10139a7dc2c3fa

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = None

        # self.image = Image.open("Губка_БОБ_персонаж.png")
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_right.clicked.connect(self.rotate_right)
<<<<<<< HEAD
        self.ui.btn_bw.clicked.connect(self.bw_image)
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_sharp.clicked.connect(self.sharp_image)
        self.ui.btn_dir.clicked.connect(self.showfiles)


    def update_image(self):
        self.ui.label.hide()
        self.image.save("Губка_БОБ_персонаж_copy.png")
        pixmap = QPixmap("Губка_БОБ_персонаж_copy.png")
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pixmap.scaled(w, h)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()
    
=======
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_bw.clicked.connect(self.bw_image)
        self.ui.btn_sharp.clicked.connect(self.sharpen_image)
        self.ui.btn_dir.clicked.connect(self.show_files)
        self.ui.listWidget.itemClicked.connect(self.show_picture)
        self.ui.btn_save.clicked.connect(self.save_image)
        # self.image = Image.open("")
    def update_image(self,image = None):
        self.ui.label.hide()
        if image:
            pixmap = QPixmap(image)
            w, h = self.ui.label.width(), self.ui.label.height()
            pixmap = pixmap.scaled(w, h)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.show()


>>>>>>> 74e5a7dedb0229dcc2583d649f10139a7dc2c3fa
    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.update_image()
        self.image.save("copy.png")
        self.update_image("copy.png")


    
    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.update_image()
        self.image.save("copy.png")
        self.update_image("copy.png")



    def flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def bw_image(self):
        self.image = self.image.convert("L")
        self.update_image()
        self.image.save("copy.png")
        self.update_image("copy.png")


    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.update_image()
        self.image.save("copy.png")
        self.update_image("copy.png")



    def choose_dir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory(self)

        print(workdir)
    def filter(self,files,ext):
        res = []
        for file in files:
            for e in ext:
                if file.endswith(e):
                    res.append(file)
        return res    

    def show_files(self):
        ext = ["png","jpg","PNG","JPG"]
        self.choose_dir()
        if workdir:
            all_files = os.listdir(workdir)
            print(all_files)
            filter_files = self.filter(all_files,ext)
            print(filter_files)
            self.ui.listWidget.clear()
            for file in filter_files:
                self.ui.listWidget.addItem(file)

    def save_image(self):
        if self.image:
            save_path, _ = QFileDialog.getSaveFileName(self,"Зберегти файл",workdir, "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
            if save_path:
                self.image.save(save_path)
                QMessageBox.information(self,"Успіх","Зображення успішно збережено!")
            else:
                QMessageBox.warning(self,"Увага","Файл для зображення не обрано.")
        else:
            QMessageBox.warning(self,"Увага","Немає зображення для збереження")
                
            

    def show_picture(self):
        if self.ui.listWidget.currentRow() >= 0:
            filename = self.ui.listWidget.currentItem().text()
            global image_path
            image_path = os.path.join(workdir,filename)
            self.image = Image.open(image_path)
            self.update_image(image_path)


<<<<<<< HEAD
    def bw_image(self):
        self.image = self.image.convert("L")
        self.update_image()

    def flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def sharp_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.update_image()

    def chose_dir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory(self,"Виберіть папку")

    def filter(self,files,ext):
        res = []
        for file in files:
            for e in ext:
                if file.endswith(e):
                    res.append(file)
        return res
    
    def showfiles(self):
        ext = [".png",".jpg"]
        self.chose_dir()
        all_files = os.listdir()
        print(all_files)
        print("____________________________________________________")
        filter_files = self.filter(all_files,ext)
        print(filter_files)
        self.ui.listWidget.clear()
        for file in filter_files:
            self.ui.listWidget.addItem(file)




=======
        
>>>>>>> 74e5a7dedb0229dcc2583d649f10139a7dc2c3fa
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()


