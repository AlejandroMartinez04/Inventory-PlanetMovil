# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class EditProductForm(object):
    def setupUi(self, editProductWindow):
        if not editProductWindow.objectName():
            editProductWindow.setObjectName(u"editProductWindow")
        editProductWindow.resize(405, 488)
        editProductWindow.setMinimumSize(QSize(405, 488))
        editProductWindow.setMaximumSize(QSize(405, 488))
        self.EditarProductolabel = QLabel(editProductWindow)
        self.EditarProductolabel.setObjectName(u"EditarProductolabel")
        self.EditarProductolabel.setGeometry(QRect(10, 10, 381, 20))
        self.EditarProductolabel.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.EditarProductolabel.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(editProductWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 52, 61, 21))
        self.label_2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.titleLineEdit = QLineEdit(editProductWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 22))
        self.titleLineEdit.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.amountSpinBox = QSpinBox(editProductWindow)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(30, 140, 51, 22))
        self.amountSpinBox.setMaximum(1000)

        self.priceSaleLineEdit_2 = QLineEdit(editProductWindow)
        self.priceSaleLineEdit_2.setObjectName(u"priceSaleLineEdit_2")
        self.priceSaleLineEdit_2.setGeometry(QRect(30, 210, 111, 22))

        self.label_3 = QLabel(editProductWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 21))
        self.priceSaleLineEdit = QLineEdit(editProductWindow)
        self.priceSaleLineEdit.setObjectName(u"priceSaleLineEdit")
        self.priceSaleLineEdit.setGeometry(QRect(30, 280, 111, 22))

        self.label_5 = QLabel(editProductWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 250, 101, 21))
        self.barcodeLineEdit = QLineEdit(editProductWindow)
        self.barcodeLineEdit.setObjectName(u"barcodeLineEdit")
        self.barcodeLineEdit.setGeometry(QRect(30, 350, 200, 22))
        self.barcodeLineEdit.setReadOnly(True)
        
        self.label_6 = QLabel(editProductWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 320, 101, 21))
        
        self.editProductButton = QPushButton(editProductWindow)
        self.editProductButton.setObjectName(u"editProductButton")
        self.editProductButton.setGeometry(QRect(210, 420, 111, 31))
        self.editProductButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editProductButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.editProductButton.setText(u"GUARDAR")
        icon = QIcon()
        icon.addFile(u"./assets/newicons/icons8-enviar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editProductButton.setIcon(icon)
        self.editProductButton.setFlat(False)
        self.cancelProductButton = QPushButton(editProductWindow)
        self.cancelProductButton.setObjectName(u"cancelProductButton")
        self.cancelProductButton.setGeometry(QRect(90, 420, 111, 31))
        self.cancelProductButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelProductButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.cancelProductButton.setText(u"CANCELAR")
        icon1 = QIcon()
        icon1.addFile(u"./assets/newicons/icons8-cancelar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelProductButton.setIcon(icon1)
        self.cancelProductButton.setFlat(False)
        
        self.label_7 = QLabel(editProductWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 180, 101, 21))

        self.retranslateUi(editProductWindow)

        QMetaObject.connectSlotsByName(editProductWindow)
    # setupUi

    def retranslateUi(self, editProductWindow):
        editProductWindow.setWindowTitle(QCoreApplication.translate("editProductWindow", u"Editar producto", None))
        self.EditarProductolabel.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p align=\"center\">EDITAR PRODUCTO</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Nombre</span></p></body></html>", None))
        self.label_3.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Cantidad</span></p></body></html>", None))
        self.priceSaleLineEdit.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_5.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_5.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p>Precio venta</p><p><br/></p></body></html>", None))
        self.barcodeLineEdit.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_6.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Codigo barras</span></p></body></html>", None))
        self.amountSpinBox.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.priceSaleLineEdit_2.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("editProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p>Precio ingreso</p><p><br/></p></body></html>", None))
    # retranslateUi

