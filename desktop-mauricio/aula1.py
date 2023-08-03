'''from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Professor Maurício")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()'''

#1
'''from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vai ficar pior")
        self.setFixedSize(QSize(600,400))
        self.lbl = QLabel("Hello World")
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()'''

#2
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit , QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXERCÍCIO 2")
        self.setFixedSize(1000,800)
        self.button=QPushButton("Botão", self)
        self.button.setGeometry(190,10,100,70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        num = 18
        if num % 2 == 0:
            self.result_label.setText(f"Este número é par: {num}")
        else:
            self.result_label.setText(f"Este número é ímpar: {num}")
            
            
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()

