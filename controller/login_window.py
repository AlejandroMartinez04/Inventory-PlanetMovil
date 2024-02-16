from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from view.login_window import FormLogin
from pys6_msgBoxes import msg_boxes

class login_window(QWidget, FormLogin):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.btnEnviar.clicked.connect(self.check_input)
        self.btnCancelar.clicked.connect(self.close)
        
        self.userLineEdit.returnPressed.connect(self.check_input)
        self.passLineEdit.returnPressed.connect(self.check_input)

    def check_input(self):
        username = self.userLineEdit.text()
        password = self.passLineEdit.text()

        errors_count = 0

        if username == "" or password == "":
            msg_boxes.error_msg_box('Aviso!','El campo usuario y contraseña son obligatorios')
            errors_count += 1 

        if username == "administrador" and password == "password":
            self.close()
            self.open_admin_view()
        elif username == 'empleado' and password =='clave':
            self.close()
            self.open_employee_view()    
        else: 
            msg_boxes.error_msg_box('Error!','Credenciales incorrectas')
            self.clean_inputs()

        if errors_count == 0:
            return True

    def clean_inputs(self):
        self.userLineEdit.clear()
        self.passLineEdit.clear()

    def open_admin_view(self):
        from controller.main_window import ListProducWindows
        window = ListProducWindows()
        window.show()

    def open_employee_view(self):
        from controller.employee_window import ListProducWindowEmployee
        window = ListProducWindowEmployee()
        window.show()