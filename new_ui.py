import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from new_face_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint) #无边框
        self.setAttribute(Qt.WA_TranslucentBackground) #圆角背景透明

        self.current_page_index = 0 # 定义为类成员变量
        self.pushButton_left.clicked.connect(self.button_clicked)
        self.pushButton_right.clicked.connect(self.button_clicked1)
        self.pushButton_close.clicked.connect(lambda: self.close())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def button_clicked(self):
        pages = [self.page_auto, self.page_manual, self.page_function] # 添加所有需要循环的页面
        
        self.current_page_index = (self.current_page_index + 1) % len(pages) # 计算下一个页面的索引，实现循环效果
        self.stackedWidget.setCurrentWidget(pages[self.current_page_index])

    def button_clicked1(self):
        pages = [self.page_auto, self.page_manual, self.page_function] # 添加所有需要循环的页面
    
        self.current_page_index = (self.current_page_index - 1) % len(pages) # 计算下一个页面的索引，实现循环效果
        self.stackedWidget.setCurrentWidget(pages[self.current_page_index])
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())