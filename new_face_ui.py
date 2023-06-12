# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_face.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import computer_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(68, 58, 145);\n"
"border-radius:20px;")
        self.pushButton_close = QPushButton(self.widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(175, 12, 14, 14))
        self.pushButton_close.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:7px;")
        self.pushButton_left = QPushButton(self.widget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setGeometry(QRect(130, 12, 14, 14))
        self.pushButton_left.setStyleSheet(u"image: url(:/image/Chevron Left.png);")
        self.pushButton_right = QPushButton(self.widget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setGeometry(QRect(150, 12, 14, 14))
        self.pushButton_right.setStyleSheet(u"image: url(:/image/Chevron Right.png);")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(1, 50, 198, 250))
        self.stackedWidget.setStyleSheet(u"")
        self.page_manual = QWidget()
        self.page_manual.setObjectName(u"page_manual")
        self.widget_3 = QWidget(self.page_manual)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1, 10, 198, 150))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(68, 58, 145, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_3.setPalette(palette)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_4.setPalette(palette1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_manualchange = QPushButton(self.page_manual)
        self.pushButton_manualchange.setObjectName(u"pushButton_manualchange")
        self.pushButton_manualchange.setGeometry(QRect(10, 180, 180, 50))
        palette2 = QPalette()
        brush2 = QBrush(QColor(245, 190, 82, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_manualchange.setPalette(palette2)
        self.pushButton_manualchange.setStyleSheet(u"QPushButton {\n"
"\n"
"	\n"
"	background-color: rgb(245, 190, 82);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"\n"
"	background-color: rgb(255, 85, 0);\n"
"}")
        self.stackedWidget.addWidget(self.page_manual)
        self.page_auto = QWidget()
        self.page_auto.setObjectName(u"page_auto")
        self.widget_2 = QWidget(self.page_auto)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(1, 20, 198, 130))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label.setPalette(palette3)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_2.setPalette(palette4)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.pushButton_autochange = QPushButton(self.page_auto)
        self.pushButton_autochange.setObjectName(u"pushButton_autochange")
        self.pushButton_autochange.setGeometry(QRect(10, 180, 180, 50))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_autochange.setPalette(palette5)
        self.pushButton_autochange.setStyleSheet(u"QPushButton {\n"
"\n"
"	\n"
"	background-color: rgb(245, 190, 82);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"\n"
"	background-color: rgb(255, 85, 0);\n"
"}")
        self.stackedWidget.addWidget(self.page_auto)
        self.page_function = QWidget()
        self.page_function.setObjectName(u"page_function")
        self.widget_4 = QWidget(self.page_function)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(1, 20, 198, 210))
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(26, 20, 60, 60))
        self.pushButton.setStyleSheet(u"background-color: rgb(245, 190, 82);\n"
"border-radius:10px;")
        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(114, 20, 60, 60))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(245, 190, 82);\n"
"border-radius:10px;")
        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(114, 100, 60, 60))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(245, 190, 82);\n"
"border-radius:10px;")
        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(26, 100, 60, 60))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(245, 190, 82);\n"
"border-radius:10px;")
        self.stackedWidget.addWidget(self.page_function)

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_close.setText("")
        self.pushButton_left.setText("")
        self.pushButton_right.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Computer_Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IP_Address", None))
        self.pushButton_manualchange.setText(QCoreApplication.translate("MainWindow", u"Manual Change", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"201E6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"192.168.33.211", None))
        self.pushButton_autochange.setText(QCoreApplication.translate("MainWindow", u"Auto Change", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

