from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __innit__(self):
        super().__init__()
        self.setWindowTitle("Escolha seu Pokemon")
        self.setGeometry(100,100,300,150)
        
        self.button = QPushButton("Pokemon 1 ",self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.mostrar)
        
        self.button2 = QPushButton("Pokemon 2 ", self)
        self.button2.setGeometry(190,100,100,70)
        self.button2.clicked.connect(self.mostrar2)
        
    def mostrar(self):
        self.label=QLabel()
        self.label.setPixmap(QPixmap("pikachubr"))
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)
    
    def mostrar2(self):
        self.label=QLabel()
        self.label.setPixmap(QPixmap("Missing number"))
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)
        

app=QApplication(sys.argv)
janela=MainWindow()
'''janela.resize(500.300)'''
janela.show()
app.exec()