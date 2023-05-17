from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QSpacerItem, \
    QSizePolicy, QInputDialog, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon: Battle of Champions")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)


        self.label = QLabel("Welcome to Pokemon: Battle of Champions!\nPlayer one, please enter your name.", self)
        self.label.setAlignment(Qt.AlignCenter)

        spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout.addSpacerItem(spacer1)
        layout.addWidget(self.label)

        line_edit = QLineEdit(self)
        layout.addWidget(line_edit)

        self.button = QPushButton("Enter Input:", self)
        spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.clicked.connect(lambda: self.handle_input(line_edit.text()))

        layout.addWidget(self.button)
        layout.addSpacerItem(spacer2)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

    def handle_input(self, input_text):
        # Process the input text here
        print("User input:", input_text)
    def update_text(self, new_text):
        self.label.setText(new_text)




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
