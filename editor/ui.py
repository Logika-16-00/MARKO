# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(707, 584)
        MainWindow.setStyleSheet("background-color: lightblue;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.btn_dir.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_dir.setObjectName("btn_dir")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(150, 490, 101, 51))
        self.btn_left.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(260, 490, 101, 51))
        self.btn_right.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_right.setObjectName("btn_right")
        self.btn_flip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_flip.setGeometry(QtCore.QRect(370, 490, 101, 51))
        self.btn_flip.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_flip.setObjectName("btn_flip")
        self.btn_sharp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sharp.setGeometry(QtCore.QRect(480, 490, 101, 51))
        self.btn_sharp.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_sharp.setObjectName("btn_sharp")
        self.btn_bw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bw.setGeometry(QtCore.QRect(590, 490, 101, 51))
        self.btn_bw.setStyleSheet("background-color: rgb(123, 199, 87);\n"
"color: rgb(255, 255, 255);\n"
"border_radius: 20px;")
        self.btn_bw.setObjectName("btn_bw")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 131, 471))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 70, 541, 401))
        self.label.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_dir.setText(_translate("MainWindow", "Папка"))
        self.btn_left.setText(_translate("MainWindow", "Вліво"))
        self.btn_right.setText(_translate("MainWindow", "Вправо"))
        self.btn_flip.setText(_translate("MainWindow", "Дзеркало"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість"))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
