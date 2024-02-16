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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class FormLogin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(312, 229)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(312, 229))
        Form.setMaximumSize(QSize(312, 229))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 271, 205))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.UserLabel = QLabel(self.verticalLayoutWidget)
        self.UserLabel.setObjectName(u"UserLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UserLabel.sizePolicy().hasHeightForWidth())
        self.UserLabel.setSizePolicy(sizePolicy1)
        self.UserLabel.setAlignment(Qt.AlignBottom|Qt.AlignJustify)

        self.verticalLayout.addWidget(self.UserLabel)

        self.userLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.userLineEdit.setObjectName(u"userLineEdit")

        self.verticalLayout.addWidget(self.userLineEdit)

        self.PassLabel = QLabel(self.verticalLayoutWidget)
        self.PassLabel.setObjectName(u"PassLabel")
        sizePolicy1.setHeightForWidth(self.PassLabel.sizePolicy().hasHeightForWidth())
        self.PassLabel.setSizePolicy(sizePolicy1)
        self.PassLabel.setAlignment(Qt.AlignBottom|Qt.AlignJustify)

        self.verticalLayout.addWidget(self.PassLabel)

        self.passLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.passLineEdit.setObjectName(u"passLineEdit")
        self.passLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.btnCancelar = QPushButton(self.verticalLayoutWidget)
        self.btnCancelar.setObjectName(u"btnCancelar")
        sizePolicy1.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnCancelar)

        self.btnEnviar = QPushButton(self.verticalLayoutWidget)
        self.btnEnviar.setObjectName(u"btnEnviar")
        sizePolicy1.setHeightForWidth(self.btnEnviar.sizePolicy().hasHeightForWidth())
        self.btnEnviar.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnEnviar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, -10, 121, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Inicio sesion", None))
        self.UserLabel.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.PassLabel.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnEnviar.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.label.setText(QCoreApplication.translate("Form", u"inicio sesion", None))
    # retranslateUi

