import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from computer_ui import Ui_MainWindow
from functions import *

cfp = configparser.ConfigParser()
cfp.read("Config.ini")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) #无边框
        # self.setAttribute(Qt.WA_TranslucentBackground) #圆角背景透明

        Net_IP,Net_gateway,PC_name = calc_ip()
        # print(PC_name)
        print(get_computer_name())
        self.label.setText(get_computer_name())
        self.label_2.setText(get_ip_addresses())
        self.pushButton_3.setText("Change to\n\n{PC_name}\n\n{Net_IP}".format(PC_name=PC_name, Net_IP=Net_IP))
        self.pushButton_close.clicked.connect(lambda: self.close())
        self.pushButton_3.clicked.connect(lambda: change(self))
        self.pushButton_4.clicked.connect(lambda: save_mac(self))

        def save_mac(self):
            get_text()
            self.pushButton_4.setText("Save Already\n\n请勿重复点击")
            self.pushButton_4.setEnabled(False)

        def change(self):
            auto_modify()
            self.pushButton_3.setText("Changed Already\n\n{PC_name}\n\n{Net_IP}".format(PC_name=PC_name, Net_IP=Net_IP))
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
