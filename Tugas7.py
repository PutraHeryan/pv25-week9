from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QInputDialog, QWidget
)


class InputDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Demo")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.list_input = QLineEdit(self)
        self.list_input.setPlaceholderText("Choose from list")
        self.list_button = QPushButton("Choose from list", self)
        self.list_button.clicked.connect(self.show_list_dialog)

        list_layout = QHBoxLayout()
        list_layout.addWidget(self.list_button)
        list_layout.addWidget(self.list_input)
        self.main_layout.addLayout(list_layout)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter your name")
        self.name_button = QPushButton("get name", self)
        self.name_button.clicked.connect(self.show_name_dialog)

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_button)
        name_layout.addWidget(self.name_input)
        self.main_layout.addLayout(name_layout)

        self.int_input = QLineEdit(self)
        self.int_input.setPlaceholderText("Enter an integer")
        self.int_button = QPushButton("Enter an integer", self)
        self.int_button.clicked.connect(self.show_int_dialog)

        int_layout = QHBoxLayout()
        int_layout.addWidget(self.int_button)
        int_layout.addWidget(self.int_input)
        self.main_layout.addLayout(int_layout)

    def show_list_dialog(self):
        languages = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "Select Input Dialog", "List of languages:", languages, 0, False)
        if ok and item:
            self.list_input.setText(item)

    def show_name_dialog(self):
        name, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and name:
            self.name_input.setText(name)

    def show_int_dialog(self):
        number, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Enter a number:", 0, -2147483648, 2147483647, 1)
        if ok:
            self.int_input.setText(str(number))


if __name__ == "__main__":
    app = QApplication([])
    window = InputDialogDemo()
    window.resize(400, 150)
    window.show()
    app.exec()