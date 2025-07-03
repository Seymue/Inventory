#ui.ui_mainwindow.py

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 615)
        MainWindow.setStyleSheet(u"background-color: #1E1E1E; ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 0))
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #1E1E1E; ")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 400))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.findText = QLineEdit(self.widget_4)
        self.findText.setObjectName(u"findText")
        self.findText.setStyleSheet(u"color: white;")

        self.verticalLayout_2.addWidget(self.findText)

        self.findButton = QPushButton(self.widget_4)
        self.findButton.setObjectName(u"findButton")
        self.findButton.setStyleSheet(u"""
                    QPushButton {
                        background-color: #007ACC;
                        color: white;
                        padding: 6px 15px;
                        border-radius: 4px;
                        font-family: 'Segoe UI';
                        font-size: 9pt;
                    }
                    QPushButton:hover {
                        background-color: #0099FF;
                    }
                    QPushButton:pressed {
                        background-color: #005A9E;
                        padding-top: 9px;
                        padding-bottom: 7px;
                    }
                    QPushButton:disabled {
                        background-color: #3D3D40;
                        color: #7A7A7A;
                    }
                """)

        self.verticalLayout_2.addWidget(self.findButton)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 100))
        self.widget_5.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.addButton = QPushButton(self.widget_5)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"""
                    QPushButton {
                        background-color: #27AE60;
                        color: white;
                        border: none;
                        padding: 5px 10px;
                        border-radius: 4px;
                        font-family: 'Segoe UI';
                        font-size: 8pt;
                    }
                    QPushButton:hover {
                        background-color: #2ECC71;
                    }
                    QPushButton:pressed {
                        background-color: #219653;
                        padding-top: 9px;
                        padding-bottom: 7px;
                    }
                    QPushButton:disabled {
                        background-color: #3D3D40;
                        color: #7A7A7A;
                    }
                """)

        self.verticalLayout_3.addWidget(self.addButton)

        self.editButton = QPushButton(self.widget_5)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setStyleSheet(u"""
                    QPushButton {
                        background-color: #F39C12;
                        color: white;
                        border: none;
                        padding: 5px 10px;
                        border-radius: 4px;
                        font-family: 'Segoe UI';
                        font-size: 8pt;
                    }
                    QPushButton:hover {
                        background-color: #F1C40F;
                    }
                    QPushButton:pressed {
                        background-color: #F39C12;
                        padding-top: 9px;
                        padding-bottom: 7px;
                    }
                    QPushButton:disabled {
                        background-color: #3D3D40;
                        color: #7A7A7A;
                    }
                """)

        self.verticalLayout_3.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.widget_5)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u" ")
        self.deleteButton.setStyleSheet(u"""
                    QPushButton {
                        background-color: #C0392B;
                        color: white;
                        border: none;
                        padding: 5px 10px;
                        border-radius: 4px;
                        font-family: 'Segoe UI';
                        font-size: 8pt;
                    }
                    QPushButton:hover {
                        background-color: #E74C3C;
                    }
                    QPushButton:pressed {
                        background-color: #A93226;
                        padding-top: 9px;
                        padding-bottom: 7px;
                    }
                    QPushButton:disabled {
                        background-color: #3D3D40;
                        color: #7A7A7A;
                    }
                """)

        self.verticalLayout_3.addWidget(self.deleteButton)


        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView = QTableView(self.widget_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"""
                    QTableView {
                        background-color: #252526;
                        gridline-color: #3C3C3C;
                        border-radius: 5px;
                        border: 1px solid #3C3C3C;
                        font-family: 'Segoe UI';
                        font-size: 9pt;
                        color: #CCCCCC;
                    }
                    QTableView QTableCornerButton::section {
                        background-color: #2D2D30;
                        border: none;
                        border-bottom: 1px solid #3C3C3C;
                        border-right: 1px solid #3C3C3C;
                    }
                    QHeaderView::section {
                        background-color: #2D2D30;
                        color: #FFFFFF;
                        padding: 8px;
                        border: none;
                        font-weight: bold;
                    }
                    QTableView::item {
                        padding: 8px;
                        border-bottom: 1px solid #3C3C3C;
                    }
                    QTableView::item:selected {
                        background-color: #094771;
                        color: white;
                    }
                    QScrollBar:vertical {
                        background: #252526;
                        width: 12px;
                        margin: 0px;
                    }
                    QScrollBar::handle:vertical {
                        background: #3D3D40;
                        min-height: 20px;
                        border-radius: 6px;
                    }
                    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                        background: none;
                    }
                """)

        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.findButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

