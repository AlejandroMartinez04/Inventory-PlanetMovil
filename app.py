from PySide6.QtWidgets import QApplication
from controller.main_window import ListProducWindows

if __name__ == "__main__":
    app = QApplication()
    window = ListProducWindows()
    window.showMaximized()
    window.show()

    app.exec()
    