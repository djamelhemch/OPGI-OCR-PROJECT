# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(585, 272)
        Dialog.setMinimumSize(QSize(32, 32))
        Dialog.setBaseSize(QSize(32, 32))
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        self.label2 = QLabel(Dialog)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(10, 120, 131, 16))
        self.dipositor_name = QLineEdit(Dialog)
        self.dipositor_name.setObjectName(u"dipositor_name")
        self.dipositor_name.setGeometry(QRect(10, 50, 561, 41))
        self.label1 = QLabel(Dialog)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(10, 30, 231, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 281, 21))
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setPixmap(QPixmap(u"E:/PROTEC FILES/Protec Ressources/Standard Logo Files protec/Monochrome on Transparent.png"))
        self.btn_next = QPushButton(Dialog)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(410, 230, 75, 31))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(500, 230, 75, 31))
        self.nb_docs = QSpinBox(Dialog)
        self.nb_docs.setObjectName(u"nb_docs")
        self.nb_docs.setGeometry(QRect(10, 150, 151, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"Nombre de documents", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Nom de d\u00e9positaire", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Made by PROTEC All rights reserved", None))
        self.btn_next.setText(QCoreApplication.translate("Dialog", u"Suivant", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Annuler", None))
    # retranslateUi

