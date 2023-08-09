from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QCloseEvent
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escolha a forma geométrica")

        layout = QVBoxLayout()
        label = QLabel("Escolha a forma geométrica:")
        layout.addWidget(label)

        self.square_button = QPushButton("Quadrado")
        self.square_button.clicked.connect(self.open_square_window)
        layout.addWidget(self.square_button)

        self.circle_button = QPushButton("Círculo")
        self.circle_button.clicked.connect(self.open_circle_window)
        layout.addWidget(self.circle_button)

        self.rectangle_button = QPushButton("Retângulo")
        self.rectangle_button.clicked.connect(self.open_rectangle_window)
        layout.addWidget(self.rectangle_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_square_window(self):
        self.square_window = SquareWindow()
        self.square_window.show()

    def open_circle_window(self):
        self.circle_window = CircleWindow()
        self.circle_window.show()

    def open_rectangle_window(self):
        self.rectangle_window = RectangleWindow()
        self.rectangle_window.show()


class SquareWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quadrado")

        layout = QVBoxLayout()
        label = QLabel("Informe o lado do quadrado:")
        layout.addWidget(label)

        self.side_input = QLineEdit()
        layout.addWidget(self.side_input)

        calculate_button = QPushButton("Calcular área")
        calculate_button.clicked.connect(self.calculate_area)
        layout.addWidget(calculate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_area(self):
        side = float(self.side_input.text())
        area = side ** 2
        self.result_label.setText(f"A área do quadrado é: {area}")


class CircleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Círculo")

        layout = QVBoxLayout()
        label = QLabel("Informe o raio do círculo:")
        layout.addWidget(label)

        self.radius_input = QLineEdit()
        layout.addWidget(self.radius_input)

        calculate_button = QPushButton("Calcular área")
        calculate_button.clicked.connect(self.calculate_area)
        layout.addWidget(calculate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_area(self):
        radius = float(self.radius_input.text())
        area = 3.14 * radius ** 2
        self.result_label.setText(f"A área do círculo é: {area}")


class RectangleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retângulo")

        layout = QVBoxLayout()
        label1 = QLabel("Informe a base do retângulo:")
        layout.addWidget(label1)

        self.base_input = QLineEdit()
        layout.addWidget(self.base_input)

        label2 = QLabel("Informe a altura do retângulo:")
        layout.addWidget(label2)

        self.height_input = QLineEdit()
        layout.addWidget(self.height_input)

        calculate_button = QPushButton("Calcular área")
        calculate_button.clicked.connect(self.calculate_area)
        layout.addWidget(calculate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_area(self):
        base = float(self.base_input.text())
        height = float(self.height_input.text())
        area = base * height
        self.result_label.setText(f"A área do retângulo é: {area}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())