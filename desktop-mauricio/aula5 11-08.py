import brazilcep
import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca CEP")

endereco = brazilcep.get_address_from_cep("79008280")
print(endereco)

app = QApplication(sys.argv)

window = Mainwindow()

window.show()

sys.exit(app.exec_())
