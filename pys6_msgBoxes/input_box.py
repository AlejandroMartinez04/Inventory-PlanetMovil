from PySide6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialogButtonBox
from PySide6.QtGui import QIcon
import os
import sys

class InputBox(QDialog):
    def __init__(self, title, label):
        super().__init__()
        self.setWindowTitle(title)
        self.setLayout(QVBoxLayout())

        self.label = QLabel(label, self)
        self.layout().addWidget(self.label)

        self.line_edit = QLineEdit(self)
        self.line_edit.setEchoMode(QLineEdit.Password)
        self.layout().addWidget(self.line_edit)

        button_box = self.create_button_box()
        self.layout().addWidget(button_box)

    def create_button_box(self):
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        return button_box

    def set_custom_icon(self, icon):
        self.setWindowIcon(icon)

    def textValue(self):
        return self.line_edit.text()
    

def resource_path(relative_path):
            """Obtener la ruta absoluta a un recurso, funciona para ejecutables y scripts."""
            try:
                # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)    

def input_msg_box(title, label):

    icon1product = resource_path("assets/newicons/icons8-enviar-48.png")

    icon = QIcon(icon1product)
    msgbox = InputBox(title, label)
    msgbox.set_custom_icon(icon)
    result = msgbox.exec()
    value = msgbox.textValue() if result else None
    return value
