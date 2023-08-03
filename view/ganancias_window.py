# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ganancias_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class gananciastWindow(object):
    def setupUi(self, gananciastWindow):
        if not gananciastWindow.objectName():
            gananciastWindow.setObjectName(u"gananciastWindow")
        gananciastWindow.resize(1221, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gananciastWindow.sizePolicy().hasHeightForWidth())
        gananciastWindow.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(gananciastWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gananciaslabel = QLabel(gananciastWindow)
        self.gananciaslabel.setObjectName(u"gananciaslabel")
        self.gananciaslabel.setFrameShape(QFrame.Box)


        self.gridLayout_3.addWidget(self.gananciaslabel, 0, 0, 1, 2)

        self.label = QLabel(gananciastWindow)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendarWidget = QCalendarWidget(gananciastWindow)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.calendarWidget)

        self.label_2 = QLabel(gananciastWindow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_2)

        self.gananciasLineEdit = QLineEdit(gananciastWindow)
        self.gananciasLineEdit.setObjectName(u"gananciasLineEdit")
        sizePolicy.setHeightForWidth(self.gananciasLineEdit.sizePolicy().hasHeightForWidth())
        self.gananciasLineEdit.setSizePolicy(sizePolicy)
        self.gananciasLineEdit.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.gananciasLineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.gananciasLineEdit)

        self.label_3 = QLabel(gananciastWindow)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_3)

        self.ventasLineEdit = QLineEdit(gananciastWindow)
        self.ventasLineEdit.setObjectName(u"ventasLineEdit")
        sizePolicy.setHeightForWidth(self.ventasLineEdit.sizePolicy().hasHeightForWidth())
        self.ventasLineEdit.setSizePolicy(sizePolicy)
        self.ventasLineEdit.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.ventasLineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.ventasLineEdit)

        self.verGanButton = QPushButton(gananciastWindow)
        self.verGanButton.setObjectName(u"verGanButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verGanButton.sizePolicy().hasHeightForWidth())
        self.verGanButton.setSizePolicy(sizePolicy1)
        self.verGanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.verGanButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.verGanButton.setText(u"VER")
        icon = QIcon()
        icon.addFile(u"./assets/newicons/icons8-b\u00fasqueda-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verGanButton.setIcon(icon)
        self.verGanButton.setFlat(False)

        self.verticalLayout.addWidget(self.verGanButton)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(gananciastWindow)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)


        self.retranslateUi(gananciastWindow)

        QMetaObject.connectSlotsByName(gananciastWindow)
    # setupUi

    def retranslateUi(self, gananciastWindow):
        gananciastWindow.setWindowTitle(QCoreApplication.translate("gananciastWindow", u"Ganancias", None))
        self.gananciaslabel.setStyleSheet(QCoreApplication.translate("gananciastWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.gananciaslabel.setText(QCoreApplication.translate("gananciastWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">GANANCIAS</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("gananciastWindow", u"Tabla de ganancias", None))
        self.calendarWidget.setStyleSheet(QCoreApplication.translate("gananciastWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_2.setText(QCoreApplication.translate("gananciastWindow", u"Ganancias por dia:", None))
        self.label_3.setText(QCoreApplication.translate("gananciastWindow", u"Ventas por dia:", None))
        self.tableWidget.setStyleSheet(QCoreApplication.translate("gananciastWindow", u"font: 700 11pt \"Segoe UI\";", None))
    # retranslateUi

