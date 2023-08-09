'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout,QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHECK BOX")
        self.label=QLabel("CLIQUE E ACEITE É ISSO")
        self.ck=QCheckBox("ACEITO!!!!")
        self.label2=QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        
        container=QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)            
    
    def state(self, s):
        if s == 2:
            self.label2.setText("NÃO!!")
        else:
            self.label2.setText("some daqui")    
    
app=QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec()'''

#exerc

'''from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QCheckBox
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro")
        self.setFixedSize(500, 600)
        
        # Nome
        self.label = QLabel("Nome:", self)
        self.label.setGeometry(10,10,200,30)
        
        self.input = QLineEdit(self)
        self.input.setGeometry(70,10,100,30)
        # Telefone
        
        self.label2 = QLabel("Telefone:", self)
        self.label2.setGeometry(10,50,200,30)
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(70,50,100,30)
        # Endereço
        
        self.label3 = QLabel("Endereço:", self)
        self.label3.setGeometry(10,90,200,30)
        
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(70,90,100,30)
        # Botão
        
        self.botao = QPushButton("Submeter",self)
        self.botao.setGeometry(0, 570, 500, 24)
        # self.botao.clicked.connect(self.imprimir)
        # CheckBox
        
        self.check = QCheckBox("Sexo:")
        self.check.setGeometry(10, 130, 100, 30)
        
        layout = QVBoxLayout()
        layout.addWidget(self.check)
        # layout.addWidget()
        # layout.addWidget()
        
    # def imprimir(self):
        
    #     nome = str(self.input.text())
        
    #     self.label.setText(nome)
        
'''
'''app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()


-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.label = QLabel("Aceita casar comigo ?")
        self.ck = QCheckBox("Aceito")
        self.ck2 = QCheckBox("NÃO ACEITO")
        self.label2 = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        layout.addWidget(self.ck2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)
        self.ck2.stateChanged.connect(self.state2)
        
    def state(self, s):
        print(s)
        if s == 2:
            self.label2.setText("ACEITO")
            self.ck2.setChecked(False)
        else:
            self.ck2.setChecked(True)
            
    def state2(self, s):
        print(s)
        if s == 2:
            self.label2.setText("NÃO ACEITO")
            self.ck.setChecked(False)
        else:
            self.ck.setChecked(True)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.label = QLabel("Aceita casar comigo ?")
        self.ck = QCheckBox("Aceito")
        self.ck2 = QCheckBox("NÃO ACEITO")
        self.label2 = QLabel()
        
        self.ck.setTristate(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        layout.addWidget(self.ck2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)
        self.ck2.stateChanged.connect(self.state2)
        
    def state(self, s):
        print(s)
        if s == 2:
            self.label2.setText("ACEITO")
        elif s == 0:
            self.label2.setText("ACEITO NAO")
        else:
            self.label2.setText("ACEITO mais o menos")
        
          
            
    def state2(self, s):
        print(s)
        if s == 2:
            self.label2.setText("NÃO ACEITO")
           

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()