from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from view.new_product_window import NewProductForm
from model.products import insert_product
from pys6_msgBoxes import msg_boxes

class NewProductWindow(QWidget, NewProductForm):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.parent = parent
        self.AddProductButton.clicked.connect(self.add_product)
        self.cancelProductButton.clicked.connect(self.close)
        self.priceSaleLineEdit.returnPressed.connect(self.AddProductButton.click)
        self.priceSaleLineEdit_2.returnPressed.connect(self.AddProductButton.click)
        self.providerLineEdit.returnPressed.connect(self.AddProductButton.click)


    def check_input(self):
        code = self.barcodeLineEdit.text()
        name = self.titleLineEdit.text()
        amount = self.amountSpinBox.value()
        priceOut = self.priceSaleLineEdit.text()
        priceInt = self.priceSaleLineEdit_2.text()
        provider = self.providerLineEdit.text()

        errors_count = 0

        if code == "":
            msg_boxes.error_msg_box('Error!','El campo codigo de barras es obligatorio')
            errors_count += 1
        if name == "":
            msg_boxes.error_msg_box('Error!','El campo nombre es obligatorio')
            errors_count += 1
        if amount == "":
            msg_boxes.error_msg_box('Error!','El campo cantidad es obligatorio')
            errors_count += 1
        if priceOut == "":
            msg_boxes.error_msg_box('Error!','El campo precio venta es obligatorio')
            errors_count += 1
        if priceInt == "":
            msg_boxes.error_msg_box('Error!','El campo precio es obligatorio')
            errors_count += 1    
        if provider == "":
            msg_boxes.error_msg_box('Error!','El campo proveedor es obligatorio')
            errors_count += 1  

        if errors_count == 0:
            return True

    def write_barcode(self, texto):
        archivo = open("credentials.txt", "a")  
        archivo.write(texto + "\n")
        archivo.close()

    def add_product(self):
        code = self.barcodeLineEdit.text()
        name = self.titleLineEdit.text()
        amount = self.amountSpinBox.value()
        priceInt = self.priceSaleLineEdit_2.text()
        priceInt_format = self.agregar_punto_miles(priceInt)
        priceOut = self.priceSaleLineEdit.text()
        priceOut_format = self.agregar_punto_miles(priceOut)
        profits = int(priceOut) - int(priceInt)
        provider = self.providerLineEdit.text()

        if self.check_input():
            data = (code, name, amount, priceInt_format, priceOut_format, profits, provider)
            if insert_product(data):
                self.clean_inputs()
                self.parent.refresh_table_from_child_win()
                msg_boxes.correct_msg_box('Correcto!','Producto agregado con exito')

    def clean_inputs(self):
        self.titleLineEdit.clear()
        self.amountSpinBox.setValue(0)
        self.priceSaleLineEdit.clear()
        self.priceSaleLineEdit_2.clear()
        self.providerLineEdit.clear()
        self.barcodeLineEdit.clear()

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado