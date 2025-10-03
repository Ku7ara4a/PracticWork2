import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from PageCode import Ui_MainWindow
from Secret import Ui_SideWindow
class SideWindow(QMainWindow, Ui_SideWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.secret)
    def secret(self):
        swindow.show()
app = QApplication(sys.argv)
swindow = SideWindow()
window = MainWindow()
window.show()
app.exec()