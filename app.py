from PySide6.QtWidgets import QApplication
from controller.login_window import login_window

if __name__ == "__main__":
    app = QApplication([])
    window = login_window()
    window.show()

    app.exec()