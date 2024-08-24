from PyQt5.QtWidgets import QApplication
App = QApplication([])

App.setStyleSheet("""
    QPushButton {  
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: darkgreen; 
        color:black;
    }
    QSpinBox, QListWidget{
        padding: 5px;
        font-size: 14px;
        border-radius: 10px;
        padding: 10px 20px;
    }

    QRadioButton {
        font-size: 14px;
        padding: 5px;
        font-family: tahoma;
        margin-top: 10px;
    }

 

    QGroupBox {
        font-size: 18px;
        border: 2px solid #4CAF50; /* Green border */
        border-radius: 10px;
    }
    QRadioButton:hover {
        color:darkblue;
    }
    
    
    QListWidget{
        padding: 5px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 10px;
        border: 2px solid #4CAF50;
        background-color: grey;
        color:black;
    }

    
""")
