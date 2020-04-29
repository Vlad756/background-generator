from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys
import os
from PIL import Image, UnidentifiedImageError


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.commandLinkButton.clicked.connect(self.do_convert)

    def get_path(self):
        return self.ui.lineEdit.text()

    def get_directory(self):
        return self.ui.lineEdit_2.text()

    def get_value(self):
        return int(self.ui.lineEdit_3.text())

    def do_convert(self):
        try:
            if not os.path.exists(self.get_path()):
                print("directory doesn't exists")
        except FileNotFoundError:
            self.ui.show_popup("FileNotFoundError", "Check correct dir name")
        if not os.path.exists(self.get_directory()):
            os.makedirs(self.get_directory())
        try:
            self.ui.progressBar.setValue(0)
            add = 100 / len(os.listdir(self.get_path()))
            value = self.ui.progressBar.value()
            for filename in os.listdir(self.get_path()):
                img = Image.open(f'{self.get_path()}/{filename}')
                img.thumbnail((self.get_value(), self.get_value()))
                img.save(f'{self.get_directory()}/{filename}')
                value += add
                self.ui.progressBar.setValue(int(value))
        except UnidentifiedImageError:
            self.ui.show_popup("UnidentifiedImageError",
                               "Should be only imgs in dir")
        except ZeroDivisionError:
            self.ui.show_popup("No pics in dir", "add some pics")
        except FileNotFoundError:
            self.ui.show_popup("FileNotFoundError", "Check correct dir name")


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
