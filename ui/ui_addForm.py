# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addForm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddForm(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(852, 202)
        Dialog.setStyleSheet(u"backround-color: white;")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.acceptButton = QPushButton(self.widget)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setGeometry(QRect(730, 150, 101, 31))
        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(640, 150, 81, 31))
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 10, 151, 21))
        self.nameLabel.setStyleSheet(u"backround-color: white;")
        self.number_inventory = QLabel(self.widget)
        self.number_inventory.setObjectName(u"number_inventory")
        self.number_inventory.setGeometry(QRect(170, 10, 131, 21))
        self.number_inventory.setStyleSheet(u"backround-color: white;")
        self.office_number_Label = QLabel(self.widget)
        self.office_number_Label.setObjectName(u"office_number_Label")
        self.office_number_Label.setGeometry(QRect(470, 10, 91, 21))
        self.office_number_Label.setStyleSheet(u"backround-color: white;")
        self.typeLabel = QLabel(self.widget)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setGeometry(QRect(310, 10, 81, 21))
        self.typeLabel.setStyleSheet(u"backround-color: white;")
        self.quantityLabel = QLabel(self.widget)
        self.quantityLabel.setObjectName(u"quantityLabel")
        self.quantityLabel.setGeometry(QRect(400, 10, 61, 21))
        self.quantityLabel.setStyleSheet(u"backround-color: white;")
        self.departament_number_Label = QLabel(self.widget)
        self.departament_number_Label.setObjectName(u"departament_number_Label")
        self.departament_number_Label.setGeometry(QRect(570, 10, 81, 21))
        self.departament_number_Label.setStyleSheet(u"backround-color: white;")
        self.commentLabel = QLabel(self.widget)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setGeometry(QRect(660, 10, 161, 21))
        self.commentLabel.setStyleSheet(u"backround-color: white;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 151, 31))
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 40, 131, 31))
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 40, 81, 31))
        self.comboBox.setStyleSheet(u"backround-color: white;")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(400, 40, 61, 31))
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(470, 40, 91, 31))
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(570, 40, 81, 31))
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(660, 40, 161, 31))

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</p></body></html>", None))
        self.number_inventory.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u043e\u043c\u0435\u0440 \u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.office_number_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430</p></body></html>", None))
        self.typeLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0422\u0438\u043f</p></body></html>", None))
        self.quantityLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043b-\u0432\u043e</p></body></html>", None))
        self.departament_number_Label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.commentLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439</p></body></html>", None))
    # retranslateUi

