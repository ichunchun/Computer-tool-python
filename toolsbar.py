import sys
from PySide6.QtWidgets import QMainWindow, QApplication,QCompleter
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from toolbar_ui import Ui_MainWindow
from functions import *
import webbrowser


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        completer = QCompleter(["ip change", "auto change", "name change", "autodesk fix", "orange"])
        self.lineEdit.setCompleter(completer)
        self.pushButton.clicked.connect(lambda: self.Run())
        room,offset,start,row = read_ini()
        Net_IP,Net_gateway,PC_name = calc_ip()

        if room == '201' or room == '216' or room == '501' or room == '308':
            label_text = Net_IP + '   |   ' + PC_name
            self.label.setText(label_text)
        else:
            label_text = "One Key To Any Where!"
            self.label.setText(label_text)
        
        self.setWindowFlag(Qt.FramelessWindowHint) #无边框
        self.setAttribute(Qt.WA_TranslucentBackground) #背景透明

    def Run(self):
        self.words = self.lineEdit.text()
        if self.words == "ip change":
            print('hello')
        elif "qq.com" in self.words or "youku.com" in self.words or "mgtv.com" in self.words or "bilibili.com" in self.words:
            url = vip_film() + self.lineEdit.text()  # 要打开的网址
            print(url)
            webbrowser.open(url)
        else:
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
