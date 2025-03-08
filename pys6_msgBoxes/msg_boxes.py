from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
import os
import sys

class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)

    def set_custom_icon(self, icon):
        self.setIconPixmap(icon.pixmap(50,50))
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)
    
    def set_yes_not_buttons(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

def resource_path(relative_path):
            """Obtener la ruta absoluta a un recurso, funciona para ejecutables y scripts."""
            try:
                # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)    

def correct_msg_box(title, text):
    iconcorrect = resource_path("pys6_msgBoxes/icons/icons8-correcto-48.png")
    icon = QIcon(iconcorrect)
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def warning_msg_box(title, text):
    iconwarning = resource_path("pys6_msgBoxes/icons/icons8-advert48 (1).png")
    icon = QIcon(iconwarning)
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def error_msg_box(title, text):
    iconerror = resource_path("pys6_msgBoxes/icons/icons8-error-48.png")
    icon = QIcon(iconerror)
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def warning_check_msg_box(title, text):
    iconwarningcheck = resource_path("pys6_msgBoxes/icons/icons8-vender-48.png")
    icon = QIcon(iconwarningcheck)
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.set_yes_not_buttons()
    resp = msgbox.exec()
    return resp

