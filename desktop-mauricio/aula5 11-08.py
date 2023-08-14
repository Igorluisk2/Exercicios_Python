# import brazilcep
# import sys
# from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Buscador de Endereço")
#         self.setGeometry(100, 100, 400, 200)

# endereco = brazilcep.get_address_from_cep("79008280")
# print(endereco)

# app = QApplication(sys.argv)

# window = Mainwindow()

# window.show()

# sys.exit(app.exec_())


import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class AddressFinderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscador de Endereço")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.cep_input = QLineEdit(self)
        layout.addWidget(QLabel("Digite o CEP:"))
        layout.addWidget(self.cep_input)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        search_button = QPushButton("Buscar", self)
        search_button.clicked.connect(self.search_address)
        layout.addWidget(search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def search_address(self):
        cep = self.cep_input.text().strip().replace("-", "")
        if len(cep) == 8 and cep.isdigit():
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            data = response.json()

            if "erro" not in data:
                address = f"Endereço: {data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}"
                self.result_label.setText(address)
            else:
                self.result_label.setText("CEP não encontrado.")
        else:
            self.result_label.setText("CEP inválido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddressFinderApp()
    window.show()
    sys.exit(app.exec_())



# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
# from brazilcep.search import Search

# class AddressFinderApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Buscador de Endereço")
#         self.setGeometry(100, 100, 400, 200)

#         layout = QVBoxLayout()

#         self.cep_input = QLineEdit(self)
#         layout.addWidget(QLabel("Digite o CEP:"))
#         layout.addWidget(self.cep_input)

#         self.result_label = QLabel(self)
#         layout.addWidget(self.result_label)

#         search_button = QPushButton("Buscar", self)
#         search_button.clicked.connect(self.search_address)
#         layout.addWidget(search_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def search_address(self):
#         cep = self.cep_input.text().strip().replace("-", "")
#         if len(cep) == 8 and cep.isdigit():
#             search = Search()
#             address = search.by_cep(cep)

#             if address is not None:
#                 formatted_address = f"Endereço: {address.street}, {address.neighborhood}, {address.city} - {address.state}"
#                 self.result_label.setText(formatted_address)
#             else:
#                 self.result_label.setText("CEP não encontrado.")
#         else:
#             self.result_label.setText("CEP inválido.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AddressFinderApp()
#     window.show()
#     sys.exit(app.exec_())
