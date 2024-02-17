from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from view.login_window import FormLogin
from pys6_msgBoxes import msg_boxes
from model.people import select_by_id

class login_window(QWidget, FormLogin):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.enviarBtn.clicked.connect(self.check_input)
        self.cancelarBtn.clicked.connect(self.close)
        
        self.userLine.returnPressed.connect(self.check_input)
        self.pwLine.returnPressed.connect(self.check_input)

    def check_input(self):
        username = self.userLine.text()
        password = self.pwLine.text()

        errors_count = 0

        if username == "" or password == "":
            msg_boxes.error_msg_box('Aviso!','El campo usuario y contraseña son obligatorios')
            errors_count += 1 

        persona = self.select_person_by_id(username)
        # print(persona)
        user = persona[0]
        pw = persona[1]
        type = persona[2]

        if username == user and password == pw and type == 'empleado':
            self.close()
            self.open_employee_view() 
        elif username == user and password == pw and type == 'admin':
            self.close()
            self.open_admin_view()    
        else: 
            msg_boxes.error_msg_box('Error!','Credenciales incorrectas')
            self.clean_inputs()

        if errors_count == 0:
            return True

    def select_person_by_id(self, id):
        data = select_by_id(id)
        return data

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