from PyQt5.QtWidgets import QListWidget,QPushButton , QFormLayout ,QLineEdit,QWidget,QHBoxLayout,QVBoxLayout

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton ("Очистити")
btn_back = QPushButton ("Назад")

form = QFormLayout()

line_ans = QLineEdit("")
line_correct = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3= QLineEdit("")
form.addRow("Введіть запитання:",line_ans)
form.addRow("Введіть правильну відповідь:",line_correct)
form.addRow("Введіть неправильну відповідь 1:",line_false1)
form.addRow("Введіть неправильну відповідь 2:",line_false2)
form.addRow("Введіть неправильну відповідь 3:",line_false3)

wdgt_edit = QWidget()

wdgt_edit.setLayout(form)


list_q = QListWidget()

line1 = QHBoxLayout()
line1.addWidget(list_q)
line1.addWidget(wdgt_edit)
line2 = QHBoxLayout()
line2.addWidget(btn_add)
line2.addWidget(btn_back)
line2.addWidget(btn_clear)

main_menu_line = QVBoxLayout()
main_menu_line.addLayout(line1)
main_menu_line.addLayout(line2)