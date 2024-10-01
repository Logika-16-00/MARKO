from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from notes import Ui_MainWindow
import json


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make.clicked.connect(self.add_note)
        self.ui.list_1.itemClicked.connect(self.show_note)
        self.ui.btn_save.clicked.connect(self.save_note)
        self.ui.btn_add.clicked.connect(self.add_tag)
        self.ui.btn_search_2.clicked.connect(self.change_theme)
        for note in notes.keys():
            self.ui.list_1.addItem(note)
    def show_note(self,item):
        self.ui.list2.clear()
        self.ui.textEdit.clear()
        note_name = item.text()
        if note_name in notes:
            self.ui.list2.addItems(notes[note_name]["теги"])
            self.ui.textEdit.setText(notes[note_name]["текст"])
        print(notes.keys())

    def add_note(self):
        note_name, ok = QInputDialog.getText(self, "Додати замітку","Назва замітки")
        if ok and note_name != "":
            notes[note_name] = {"теги":[],"текст": ""}
            self.ui.list_1.addItem(note_name)
        self.write_to_file()

    def add_tag(self):
        if self.ui.list_1.currentItem():
            tag_name, ok = QInputDialog.getText(self, "Додати тег","Назва тегу")
            if ok and tag_name != "":
                print("111111111111")

    def write_to_file(self):
        with open("notes/notes.json","w",encoding="utf-8" ) as file:
            json.dump(notes,file,ensure_ascii=False)

    def save_note(self):
        if self.ui.list_1.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            notes[note_name]["текст"] = self.ui.textEdit.toPlainText()
        self.write_to_file()
        
    def change_theme(self):
        if self.ui.btn_search_2.text()=="Змінити стиль":
            self.ui.btn_search_2.setText("GO BACK")
            self.ui.btn_search.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_add.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_save.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_make.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.list_1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.list2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_delete.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_detach.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")
            self.ui.btn_search_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(55, 25, 42);\n""color: white;")


        elif self.ui.btn_search_2.text()=="GO BACK":
            self.ui.btn_search_2.setText("Змінити стиль")
            self.ui.btn_add.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_search.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_save.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_make.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.list_1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.list2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_delete.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_detach.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
            self.ui.btn_search_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(25, 53, 24);\n""color: lightblue;")
        
with open("notes/notes.json","r",encoding="utf-8" ) as file:
    notes = json.load(file)

print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()