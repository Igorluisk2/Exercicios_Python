#DESENVOLVER UM PROGRAMA QUE SOLICITE AO USUÁRIO AS SEGUINTES INFORMAÇÕES: NOME, TELEFONE, ENDEREÇO, SEXO
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QCheckBox, QDialog
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela primária")
        self.setFixedSize(800, 400)
        
        
        self.button=QPushButton("ABRIR JANELA 2",self)
        self.button.clicked.connect(self.otaJanela)
        self.button.setGeometry(300,70,200,200)        
        
        
    def otaJanela(self):
        self.secondary_window=SecondaryWindow()
        self.secondary_window.show()
        
        
class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Janela Secundária")
        self.setGeometry(200,200,500,300)
        
        layout=QVBoxLayout()
        
        label=QLabel("                                        O PITICO ESCORREGOU")
        layout.addWidget(label)
        
        image_label=QLabel(self)
        pixmap= QPixmap("deyvin")       
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        
        close_button=QPushButton("Fechar",self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
