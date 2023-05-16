from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QSpacerItem, \
    QSizePolicy, QInputDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon: Battle of Champions")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)


        widget1 = QLabel("Welcome to Pokemon: Battle of Champions!\nPlayer one, please enter your name.", self)
        widget1.setAlignment(Qt.AlignCenter)  # Align the text to the center

        spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout.addSpacerItem(spacer1)
        layout.addWidget(widget1)

        self.button = QPushButton("Enter Name:", self)
        spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.clicked.connect(self.show_input_dialog)

        layout.addWidget(self.button)
        layout.addSpacerItem(spacer2)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

    def show_input_dialog(self):
        text, ok = QInputDialog.getText(self, "User Input", "Enter your name:")
        if ok and text:
            print("User entered:", text)

    def update_text(self, new_text):
        self.label.setText(new_text)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
