from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from view.edit_product_window import EditProductForm
from model.products import update_product, select_product_by_id_search_priceInt
from pys6_msgBoxes import msg_boxes

class EditProductWindow(QWidget, EditProductForm):

    def __init__(self, parent=None, codigo_barras=None):
        self.codigo_barras = codigo_barras
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_inputs()
        self.parent = parent
        self.cancelProductButton.clicked.connect(self.close)
        self.editProductButton.clicked.connect(self.edit_product)
        self.titleLineEdit.returnPressed.connect(self.editProductButton.click)
        self.priceSaleLineEdit_2.returnPressed.connect(self.editProductButton.click)
        self.priceSaleLineEdit.returnPressed.connect(self.editProductButton.click)
        self.providerLineEdit.returnPressed.connect(self.editProductButton.click)

    def populate_inputs(self):
        data = select_product_by_id_search_priceInt(self.codigo_barras)
        data_normal = data[0]
        self.titleLineEdit.setText(str(data_normal[0]))
        self.amountSpinBox.setValue(int(data_normal[1]))
        self.priceSaleLineEdit_2.setText(str(data_normal[2]))
        self.priceSaleLineEdit.setText(str(data_normal[3]))
        self.barcodeLineEdit.setText(str(data_normal[4]))
        self.providerLineEdit.setText(str(data_normal[5]))

    def check_inputs(self):
        name = self.titleLineEdit.text()
        amount = self.amountSpinBox.value()
        princeInt = self.priceSaleLineEdit_2.text()
        priceOut = self.priceSaleLineEdit.text()
        barcode = self.barcodeLineEdit.text()

        errors_count = 0

        if name == "":
            msg_boxes.warning_msg_box('Aviso!','El campo nombre es obligatorio')
            # print("El campo nombre es obligatorio")
            errors_count += 1
        if amount == "":
            msg_boxes.warning_msg_box('Aviso!','El campo cantidad es obligatorio')
            # print("El campo cantidad es obligatorio")
            errors_count += 1
        if princeInt == "":
            msg_boxes.warning_msg_box('Aviso!','El campo precio ingreso es obligatorio')
            # print("El campo precio ingreso es obligatorio")    
            errors_count += 1    
        if priceOut == "":
            msg_boxes.warning_msg_box('Aviso!','El campo precio venta es obligatorio')
            # print("El campo precio venta es obligatorio")    
            errors_count += 1
        if barcode == "":
            msg_boxes.warning_msg_box('Aviso!','El campo codigo de barras es obligatorio')
            # print("El campo codigo de barras es obligatorio")    
            errors_count += 1

        if errors_count == 0:
            return True

    def edit_product(self):
        name = self.titleLineEdit.text()
        amount = self.amountSpinBox.value()
        priceInt = self.priceSaleLineEdit_2.text()
        priceInt_without_format = int(priceInt.replace(",", ""))
        priceInt_format = self.agregar_punto_miles(priceInt_without_format)
        priceOut = self.priceSaleLineEdit.text()
        priceOut_without_format = int(priceOut.replace(",", ""))
        priceOut_format = self.agregar_punto_miles(priceOut_without_format)
        provider = self.providerLineEdit.text()

        # eliminar self.codigobarras al final del array para dejar original
        data = [name, amount, priceInt_format, priceOut_format, provider]

        if update_product(self.codigo_barras, data) and self.check_inputs():
            msg_boxes.correct_msg_box('Correcto!','Producto actualizado con exito')
            self.parent.refresh_table_from_child_win()
            self.close()

        # if update_product(data) and self.check_inputs():
        #     msg_boxes.correct_msg_box('Correcto!','Producto actualizado con exito')
        #     self.parent.refresh_table_from_child_win()
        #     self.close()

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado