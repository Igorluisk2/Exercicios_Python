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


'''from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fazemos Programa") 
        self.setFixedSize(900, 600)
        self.lbl = QLabel("Fazemos Programa, cobramos barato")
        fonte = self.lbl.font()
        fonte.setPointSize(40)
        self.lbl.setFont(fonte)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)
                
        # self.setWindowTitle("Ola Mundo")
        # botao = QPushButton("Eu sou um botão")
        # self.setCentralWidget(botao)
        # botao.clicked.connect(self.imprimir)
       
#     def imprimir(self):
#         print("Bruno")
        
app = QApplication(sys.argv)

janela = MainWindow()
janela.resize(900, 600)
janela.show()
app.exec()'''

'''from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio 2") 
        self.button = QPushButton("Botão",self)
        self.button.setGeometry(190,10,500,70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,200,30)
        
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        numero = 5
        if numero % 2 == 0:
            self.result_label.setText(f"Este numero é {numero} par")
        else:
            self.result_label.setText(f"Este numero é {numero} impar")        
app = QApplication(sys.argv)

janela = MainWindow()
janela.resize(900, 600)
janela.show()
app.exec()'''


from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercicio 3") 
        self.button = QPushButton("Botão",self)
        self.button.setGeometry(190,10,500,70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,200,30)
        
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        numero = 5
        if numero % 2 == 0:
            self.result_label.setText(f"Este numero é {numero} par")
        else:
            self.result_label.setText(f"Este numero é {numero} impar")        
app = QApplication(sys.argv)

janela = MainWindow()
janela.resize(900, 600)
janela.show()
app.exec()