# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(939, 210)
        Dialog.setStyleSheet(u"background-color: #2D2D30;   \n"
"color: #FFFFFF;    \n"
"font-family: 'Segoe UI';          ")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 110))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nameLabel = QLabel(self.widget_4)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setStyleSheet(u"color: white;")
        self.nameLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.number_inventory_Label = QLabel(self.widget_4)
        self.number_inventory_Label.setObjectName(u"number_inventory_Label")
        self.number_inventory_Label.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.number_inventory_Label)

        self.typeLabel = QLabel(self.widget_4)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setMaximumSize(QSize(80, 16777215))
        self.typeLabel.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.typeLabel)

        self.quantityLabel = QLabel(self.widget_4)
        self.quantityLabel.setObjectName(u"quantityLabel")
        self.quantityLabel.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.quantityLabel)

        self.office_number_Label = QLabel(self.widget_4)
        self.office_number_Label.setObjectName(u"office_number_Label")
        self.office_number_Label.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.office_number_Label)

        self.departament_number_Label = QLabel(self.widget_4)
        self.departament_number_Label.setObjectName(u"departament_number_Label")
        self.departament_number_Label.setMaximumSize(QSize(85, 16777215))
        self.departament_number_Label.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.departament_number_Label)

        self.commentLabel = QLabel(self.widget_4)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.commentLabel)


        self.verticalLayout.addWidget(self.widget_4)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nameText = QLineEdit(self.widget_5)
        self.nameText.setObjectName(u"nameText")
        self.nameText.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.nameText)

        self.number_inventory_Text = QLineEdit(self.widget_5)
        self.number_inventory_Text.setObjectName(u"number_inventory_Text")
        self.number_inventory_Text.setMinimumSize(QSize(150, 0))
        self.number_inventory_Text.setMaximumSize(QSize(16777215, 16777215))
        self.number_inventory_Text.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.number_inventory_Text)

        self.typeText = QLineEdit(self.widget_5)
        self.typeText.setObjectName(u"typeText")
        self.typeText.setMaximumSize(QSize(100, 16777215))
        self.typeText.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.typeText)

        self.quantityText = QLineEdit(self.widget_5)
        self.quantityText.setObjectName(u"quantityText")
        self.quantityText.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.quantityText)

        self.office_number_Text = QLineEdit(self.widget_5)
        self.office_number_Text.setObjectName(u"office_number_Text")
        self.office_number_Text.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.office_number_Text)

        self.departament_number_Text = QLineEdit(self.widget_5)
        self.departament_number_Text.setObjectName(u"departament_number_Text")
        self.departament_number_Text.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;\n"
"")

        self.horizontalLayout_3.addWidget(self.departament_number_Text)

        self.commentText = QLineEdit(self.widget_5)
        self.commentText.setObjectName(u"commentText")
        self.commentText.setStyleSheet(u"background-color: #3D3D40;   \n"
"color: #FFFFFF;              \n"
" border: 1px solid #555555;   \n"
"border-radius: 3px;          \n"
"padding: 5px;")

        self.horizontalLayout_3.addWidget(self.commentText)


        self.verticalLayout.addWidget(self.widget_5)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 4)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")

        self.gridLayout.addWidget(self.widget_7, 2, 0, 2, 2)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(500, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cancelButton = QPushButton(self.widget_2)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setStyleSheet(u"background-color: #3D3D40;  \n"
"color:white;\n"
"\n"
"   ")

        self.horizontalLayout_4.addWidget(self.cancelButton)

        self.acceptButton = QPushButton(self.widget_2)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setStyleSheet(u"background-color: #3D3D40;  \n"
"color:white;")

        self.horizontalLayout_4.addWidget(self.acceptButton)


        self.gridLayout.addWidget(self.widget_2, 1, 3, 1, 1)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout.addWidget(self.widget_6, 2, 2, 2, 2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</p></body></html>", None))
        self.number_inventory_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u043e\u043c\u0435\u0440 \u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.typeLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0422\u0438\u043f</p></body></html>", None))
        self.quantityLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043b-\u0432\u043e</p></body></html>", None))
        self.office_number_Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430</p></body></html>", None))
        self.departament_number_Label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.commentLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439</p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

