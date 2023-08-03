from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

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


def correct_msg_box(title, text):
    icon = QIcon('pys6_msgBoxes/icons/icons8-correcto-48.png')
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def warning_msg_box(title, text):
    icon = QIcon('pys6_msgBoxes/icons/icons8-advert48 (1).png')
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def error_msg_box(title, text):
    icon = QIcon('pys6_msgBoxes/icons/icons8-error-48.png')
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.exec()


def warning_check_msg_box(title, text):
    icon = QIcon('pys6_msgBoxes/icons/icons8-vender-48.png')
    msgbox = MsgBox(title, text)
    msgbox.set_custom_icon(icon)
    msgbox.set_yes_not_buttons()
    resp = msgbox.exec()
    return resp

