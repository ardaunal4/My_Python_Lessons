from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()    
        self.setGeometry(50, 50, 1080, 640)
        self.setWindowTitle("PyQt5 App")
        self.radioButton()
        self.combo_box()
        self.check_box()
        self.progressBar()
        self.show()
    
    def radioButton(self):
        self.method1 = QRadioButton("method1", self)
        self.method2 = QRadioButton("method2", self)
        self.method3 = QRadioButton("method3", self)
        
        self.method1.move(50, 40)
        self.method2.move(50, 60)
        self.method3.move(50, 80)
        
        self.method1.setChecked(True)
        
        button = QPushButton("Radio Button", self)
        button.move(50, 100)
        button.clicked.connect(self.radio_button_func)

    def radio_button_func(self):
        
        if self.method1.isChecked():
            print("method1")
        elif self.method2.isChecked():
            print("method2")
        elif self.method3.isChecked():
            print("method3")
        else:
            print("Choose one of the methods")
    def combo_box(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 40)
        self.combo.addItem("method1")
        self.combo.addItem("method2")
        self.combo.addItems(["method3", "method4"])

        button = QPushButton("Combo Button", self)
        button.move(150, 70)
        button.clicked.connect(self.combo_func)
    
    def combo_func(self):
        print(self.combo.currentText())
    
    def check_box(self):
        self.save = QCheckBox("Save", self)
        self.save.move(250, 40)
        
        button = QPushButton("save", self)
        button.move(250, 70)
        button.clicked.connect(self.check_func)
        
    def check_func(self):
        if self.save.isChecked():
            print("save")
        else:
            print("not saved")
    
    def progressBar(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(400, 40, 200, 25)
        self.pbar.setValue(0)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(500)
    
    def handleTimer(self):
        value = self.pbar.value()
        step = 5
        if value < 100:
            value = value + step
            self.pbar.setValue(value)
        else:
            self.timer.stop()

window = Window()
