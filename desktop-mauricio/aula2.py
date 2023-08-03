from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
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
app.exec()