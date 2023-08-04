'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("gol")
        self.label = QLabel()
        self.label.setPixmap(QPixmap("cheirinho.jpg"))
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)

janela = MainWindow()
janela.resize(500, 300)
janela.show()
app.exec()'''


#2
'''from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 002")
        
        self.label = QLabel("Número:", self)
        self.label.setGeometry(10, 10, 80, 30)
        
        self.input = QLineEdit(self)
        self.input.setGeometry(70, 10, 80, 30)

        self.botao = QPushButton("Par ou Impar?", self)
        self.botao.setGeometry(200, 10, 80, 30) # x, y, largura, altura
        self.botao.clicked.connect(self.imprimir)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(30, 60, 300, 60)
       
    def imprimir(self):
        try:
            num = int(self.input.text())
            
            if num % 2 == 0:
                self.result_label.setText(f"Este numero é {num} par")
                
            else:
                self.result_label.setText(f"Este numero é {num} impar")
        except ValueError:
            self.result_label.setText("Este valor não existe, Tente novamente")
        
        
app = QApplication(sys.argv)

janela = MainWindow()
janela.setFixedSize(300, 150)
janela.show()
app.exec()'''

#3
'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 003")

        self.label1 = QLabel("Número 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.label2 = QLabel("Número 2:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(220, 20, 70, 50)
        self.button.clicked.connect(self.calcular_soma)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 90, 280, 30)

    def calcular_soma(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            soma = num1 + num2
            
            self.result_label.setText(f"A soma é: {soma}")
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.resize(300, 150)
window.show()

app.exec()

    '''
#4 
'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 004")
        
        # 1 BIMESTRE
        self.label1 = QLabel("Bimestre 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)
        # 2 BIMESTRE
        self.label2 = QLabel("Bimestre 2:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)
        #  3 BIMESTRE
        self.label3 = QLabel("Bimestre 3:", self)
        self.label3.setGeometry(10, 90, 80, 30)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)
        # 4 BIMESTRE
        
        self.label4 = QLabel("Bimestre 4:", self)
        self.label4.setGeometry(10, 130, 80, 30)
        
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100, 130, 80, 30)
        # RESULTADO
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(70, 180, 280, 30)
        # BOTÃO
        
        self.button = QPushButton("Calcular Media", self)
        self.button.setGeometry(250, 10, 100, 50)
        self.button.clicked.connect(self.calcular_media)

    def calcular_media(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            num3 = int(self.input3.text())
            num4 = int(self.input4.text())
            
            media = (num1 + num2 + num3 + num4)/4
            
            self.result_label.setText(f"A media é {media}")
            
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(400, 250)
window.show()

app.exec()
'''

#5 
'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 005")
        

        self.label1 = QLabel("Metros:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(60, 10, 80, 30)
     
        self.result_label = QLabel(self)
        self.result_label.setGeometry(30, 60, 280, 30)
        
        self.label = QLabel(f"Metros para Centimetros", self)
        self.label.setGeometry(180, 0, 200, 30)
        
        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(200, 30, 80, 30)
        self.button.clicked.connect(self.calcular_metro)

    def calcular_metro(self):
        try:
            num = int(self.input1.text())
            metroCentrimetro = num*100
            
            self.result_label.setText(f"{num} Metro(s) são {metroCentrimetro} Centimetros")
            
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(350, 140)
window.show()

app.exec()'''

#6
'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 006")
        

        self.label1 = QLabel("Raio:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(60, 10, 80, 30)
     
        self.result_label = QLabel(self)
        self.result_label.setGeometry(30, 60, 280, 30)
        
        self.label = QLabel(f"Area do circulo", self)
        self.label.setGeometry(200, 0, 200, 30)
        
        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(200, 30, 80, 30)
        self.button.clicked.connect(self.calcular_area)

    def calcular_area(self):
        try:
            raio = int(self.input1.text())
            area = 3.14*(raio**2)
            
            self.result_label.setText(f"A area do circulo é {area}")
            
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(350, 140)
window.show()

app.exec()
'''

#7 
'''from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 007")
        

        self.label1 = QLabel("Lado:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(60, 10, 80, 30)
     
        self.result_label = QLabel(self)
        self.result_label.setGeometry(30, 60, 280, 30)
        
        self.label = QLabel(f"Area do Quadrado", self)
        self.label.setGeometry(190, 0, 200, 30)
        
        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(200, 30, 80, 30)
        self.button.clicked.connect(self.calcular_areaQuadra)

    def calcular_areaQuadra(self):
        try:
            lado = int(self.input1.text())
            areaQuadrado = (lado**2)*2
            
            self.result_label.setText(f"A area do quadrado é {areaQuadrado}")
            
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(350, 140)
window.show()

app.exec()
'''

#8
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 008")
        

        self.label1 = QLabel("Ganho por horas:", self)
        self.label1.setGeometry(10, 10, 300, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(180, 10, 80, 30)
        
        self.label1 = QLabel("Horas Trabalhadas no mês:", self)
        self.label1.setGeometry(10, 50, 300, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(180, 50, 80, 30)
     
        self.result_label = QLabel(self)
        self.result_label.setGeometry(30, 90, 280, 30)
        
        self.label = QLabel(f"Recebido por mês", self)
        self.label.setGeometry(290, 0, 200, 30)
        
        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(300, 30, 80, 30)
        self.button.clicked.connect(self.calcular_mesRecebido)

    def calcular_mesRecebido(self):
        try:
            ganhoHoras = int(self.input1.text())
            horasMes = int(self.input1.text())
            
            soma = ganhoHoras * horasMes 
            
            self.result_label.setText(f"Você ganha por mês: {soma} R$")
            
        except ValueError:
            self.result_label.setText(f"Este valor não existe, Tente novamente")
            
app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(400, 140)
window.show()

app.exec()



