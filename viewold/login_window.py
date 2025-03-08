# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class FormLogin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(312, 326)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(312, 326))
        Form.setMaximumSize(QSize(312, 326))
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 20, 231, 101))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        icon = QIcon()
        icon.addFile(u"./assets/newicons/icons8-usuario-masculino-en-c\u00edrculo-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))
        self.pushButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 291, 225))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cancelarBtn = QPushButton(self.gridLayoutWidget)
        self.cancelarBtn.setObjectName(u"cancelarBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancelarBtn.sizePolicy().hasHeightForWidth())
        self.cancelarBtn.setSizePolicy(sizePolicy1)
        self.cancelarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/newicons/icons8-cancelar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelarBtn.setIcon(icon1)

        self.gridLayout.addWidget(self.cancelarBtn, 4, 2, 1, 1)

        self.enviarBtn = QPushButton(self.gridLayoutWidget)
        self.enviarBtn.setObjectName(u"enviarBtn")
        sizePolicy1.setHeightForWidth(self.enviarBtn.sizePolicy().hasHeightForWidth())
        self.enviarBtn.setSizePolicy(sizePolicy1)
        self.enviarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./assets/newicons/icons8-enviar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enviarBtn.setIcon(icon2)

        self.gridLayout.addWidget(self.enviarBtn, 4, 3, 1, 1)

        self.userLine = QLineEdit(self.gridLayoutWidget)
        self.userLine.setObjectName(u"userLine")
        sizePolicy1.setHeightForWidth(self.userLine.sizePolicy().hasHeightForWidth())
        self.userLine.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.userLine, 1, 3, 1, 1)

        self.pwLine = QLineEdit(self.gridLayoutWidget)
        self.pwLine.setObjectName(u"pwLine")
        sizePolicy1.setHeightForWidth(self.pwLine.sizePolicy().hasHeightForWidth())
        self.pwLine.setSizePolicy(sizePolicy1)
        self.pwLine.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pwLine, 3, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)


        self.retranslateUi(Form)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Inicio sesion", None))
        self.label.setText(QCoreApplication.translate("Form", u"inicio sesion", None))
        self.pushButton.setText("")
        self.cancelarBtn.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.enviarBtn.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
    # retranslateUi

