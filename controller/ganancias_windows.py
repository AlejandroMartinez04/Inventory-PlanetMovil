from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QSizePolicy
from PySide6.QtCore import Qt
from view.ganancias_window import gananciastWindow
from model.sells import select_all_sells, select_sell_by_date
from pys6_msgBoxes import msg_boxes
from datetime import datetime

class GananciasWindow(QWidget, gananciastWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.parent = parent

        self.calendarWidget.selectionChanged.connect(self.on_date_selected)
        self.verGanDiaButton.clicked.connect(self.on_date_selected)
        # self.cancelGanButton.clicked.connect(self.close)
        self.verGanMenButton.clicked.connect(self.search_ganancia_mensual)
        

        self.table_config2()
        self.populate_table2(select_all_sells())
        self.populate_combobox()

        date = self.on_date_selected()
        self.search_sell_by_date(date)


    def table_config2(self):
        column_headers = ("Fecha", "Codigo", "Tipo pago", "Venta neta" ,"Ganancia neta", "Detalle venta")
        self.tableWidget.setColumnCount(len(column_headers))
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setColumnWidth(0, 95)
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 90)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(4, 110)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        # self.tableWidget.verticalHeader().hide()

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(5, QHeaderView.Stretch)  

    def populate_table2(self, data):

        self.tableWidget.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        total_ventas = self.venta_por_dia()
        ganancia_total = self.ganancia_por_dia()
        self.ventasLineEdit.setText(total_ventas)
        self.gananciasLineEdit.setText(ganancia_total)

        for row in range(len(data)):
            self.tableWidget.setRowHeight(row, 150)
    
    def on_date_selected(self):
        selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        dates = self.search_sell_by_date(selected_date)
        return dates
    
    def search_sell_by_date(self, date):
        data = select_sell_by_date(date)
        self.populate_table2(data)

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado

    def venta_por_dia(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, self.tableWidget.columnCount() - 3)
            if item is not None:
                value_str= item.text()
                value = int(value_str.replace(",", ""))
                total += value
        total_format = self.agregar_punto_miles(total)
        return total_format
        
    def ganancia_por_dia(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, self.tableWidget.columnCount() - 2)
            if item is not None:
                value_str= item.text()
                value = int(value_str.replace(",", ""))
                total += value
        total_format = self.agregar_punto_miles(total)
        return total_format

    def populate_combobox(self):
        cd_option = ("","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
        self.comboBoxMensual.addItems(cd_option)

    def obtener_fecha_con_mes(self, numero_mes):
        year = datetime.now().year

        if 1 <= numero_mes <= 12:
            fecha = f"{year}-{numero_mes:02d}"  # Utiliza :02d para asegurarte de que el mes tenga 2 dígitos
            return fecha
        else:
            return None


    def search_ganancia_mensual(self):
        suma = 0
        option_selected = self.comboBoxMensual.currentText()
        if option_selected != '':
            fecha_mes_numero = self.obtener_numero_mes(option_selected)
            fecha_anio_mes = self.obtener_fecha_con_mes(fecha_mes_numero)
            datos_ganancia_mensual = select_sell_by_date(fecha_anio_mes)
            
            for sublista in datos_ganancia_mensual:
                # Verifica que la sublista tenga al menos 5 elementos antes de acceder a la posición 4
                if len(sublista) >= 5:
                    dato = sublista[4]
                    dato_str = str(dato)
                    value = int(dato_str.replace(",", ""))
                    suma += value
            total_format_ganancias = self.agregar_punto_miles(suma)
            self.MensualLineEdit.setText(total_format_ganancias)
            return total_format_ganancias
        else:
            msg_boxes.warning_msg_box('Aviso', 'Debe seleccionar un mes')
            # print('Debe seleccionar un mes')
            return None
        
            

    def obtener_numero_mes(self, mes):
        meses = {
            'Enero': 1,
            'Febrero': 2,
            'Marzo': 3,
            'Abril': 4,
            'Mayo': 5,
            'Junio': 6,
            'Julio': 7,
            'Agosto': 8,
            'Septiembre': 9,
            'Octubre': 10,
            'Noviembre': 11,
            'Diciembre': 12
        }
        if mes in meses:
            return meses[mes]
        else:
            return None