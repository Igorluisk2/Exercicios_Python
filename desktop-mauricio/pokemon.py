from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pokedex")
        
        self.button_pikachu = QPushButton('Pikachu')
        self.button_charizard = QPushButton('Charizard')
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600,400)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_pikachu)
        layout.addWidget(self.button_charizard)
        layout.addWidget(self.image_frame)
        
        self.button_pikachu.clicked.connect(self.display_pikachu)
        self.button_charizard.clicked.connect(self.display_charizard)
        
        self.setLayout(layout)
    
    def display_pikachu(self):
        pixmap = QPixmap('pikachubr.jpg')
        self.image(pixmap)
    
    def display_charizard(self):
        pixmap = QPixmap('deyv.jpg')
        self.image(pixmap)
        
    def image(self, pixmap):
        scale_pixmap = pixmap.scaled(600,400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
    

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()