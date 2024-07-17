class Widget():
    def __init__(self,title_text,x_num,y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
    def print_info(self):
        print("Дані про віджет",self.x,self.y,self.title)
class Button(Widget):
    def __init__(self,title_text,x_num,y_num,is_clicked):
        super().__init__(title_text,x_num,y_num)
        self.clicked = is_clicked
    def click(self):
        self.clicked = True
        print("Молодець")
bt1 = Button('пр',23,32,False)
bt1.print_info()
a = input()
if a == 'Так':
    bt1.click()
else:
    print("dfg")
