# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_product_window.ui'
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

class NewProductForm(object):
    def setupUi(self, newProductWindow):
        if not newProductWindow.objectName():
            newProductWindow.setObjectName(u"newProductWindow")
        newProductWindow.resize(405, 414)
        newProductWindow.setTabletTracking(False)
        newProductWindow.setMinimumSize(QSize(405, 414))
        newProductWindow.setMaximumSize(QSize(405, 414))
        self.label = QLabel(newProductWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newProductWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 21))
        self.titleLineEdit = QLineEdit(newProductWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 90, 351, 22))

        self.amountSpinBox = QSpinBox(newProductWindow)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(30, 150, 51, 22))
        self.amountSpinBox.setMaximum(1000)

        self.priceSaleLineEdit_2 = QLineEdit(newProductWindow)
        self.priceSaleLineEdit_2.setObjectName(u"priceSaleLineEdit_2")
        self.priceSaleLineEdit_2.setGeometry(QRect(30, 220, 100, 22))

        self.label_3 = QLabel(newProductWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 122, 61, 21))

        self.priceSaleLineEdit = QLineEdit(newProductWindow)
        self.priceSaleLineEdit.setObjectName(u"priceSaleLineEdit")
        self.priceSaleLineEdit.setGeometry(QRect(30, 290, 100, 22))
        
        self.label_5 = QLabel(newProductWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 260, 91, 21))
        self.AddProductButton = QPushButton(newProductWindow)
        self.AddProductButton.setObjectName(u"AddProductButton")
        self.AddProductButton.setGeometry(QRect(200, 350, 111, 31))
        self.AddProductButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddProductButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.AddProductButton.setText(u"GUARDAR")
        icon = QIcon()
        icon.addFile(u"./assets/newicons/icons8-enviar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddProductButton.setIcon(icon)
        self.AddProductButton.setFlat(False)
        self.cancelProductButton = QPushButton(newProductWindow)
        self.cancelProductButton.setObjectName(u"cancelProductButton")
        self.cancelProductButton.setGeometry(QRect(80, 350, 111, 31))
        self.cancelProductButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelProductButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.cancelProductButton.setText(u"CANCELAR")
        icon1 = QIcon()
        icon1.addFile(u"./assets/newicons/icons8-cancelar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelProductButton.setIcon(icon1)
        self.cancelProductButton.setFlat(False)
        self.label_7 = QLabel(newProductWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 190, 101, 21))
        

        self.retranslateUi(newProductWindow)

        QMetaObject.connectSlotsByName(newProductWindow)
    # setupUi

    def retranslateUi(self, newProductWindow):
        newProductWindow.setWindowTitle(QCoreApplication.translate("newProductWindow", u"Nuevo producto", None))
        self.label.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">NUEVO PRODUCTO</span></p></body></html>", None))
        self.label_2.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_2.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Nombre</span></p></body></html>", None))
        self.titleLineEdit.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Cantidad</span></p></body></html>", None))
        self.priceSaleLineEdit.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_5.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_5.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>Precio venta</p></body></html>", None))
        self.amountSpinBox.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>Precio ingreso<br/></p></body></html>", None))
        self.priceSaleLineEdit_2.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
    # retranslateUi

