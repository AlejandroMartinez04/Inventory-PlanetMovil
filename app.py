from PySide6.QtWidgets import QApplication
from controller.login_window import login_window
from controller.main_window import ListProducWindows

if __name__ == "__main__":
    app = QApplication([])
    window = ListProducWindows()
    window.show()

    app.exec()