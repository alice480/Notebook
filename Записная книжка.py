import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('book.ui', self)
        self.name = ''
        self.number = ''
        self.line = ''
        self.pushButton.clicked.connect(self.print_text)

    def print_text(self):
        self.name = self.lineEdit.text()
        self.number = self.lineEdit_2.text()
        self.line = self.name + ' ' + self.number
        self.listWidget.addItem(self.line)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Записная книжка")
    sys.exit(app.exec())