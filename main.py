import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn.clicked.connect(self.run)

    def run(self):
        text1 = self.Edit1.toPlainText().split('\n')
        text2 = self.Edit2.toPlainText().split('\n')
        if len(text1) + len(text2) == 0:
            return 0
        n = 0
        for i in range(len(text1)):
            i -= n
            if len(text1[i].replace(' ', '')) == 0:
                del text1[i]
                n += 1
            text1[i] = text1[i].split('#')[0].replace(' ', '')
        n = 0
        for i in range(len(text2)):
            i -= n
            if len(text2[i].replace(' ', '')) == 0:
                del text2[i]
                n += 1
            text2[i] = text2[i].split('#')[0].replace(' ', '')

        cnt = 0
        for i in text1:
            if i in text2:
                cnt += 1
        for i in text2:
            if i in text1:
                cnt += 1
        statusbar_text = cnt / (len(text1) + len(text2)) * 100
        self.statusbar.showMessage(str(statusbar_text) + '%')
        if self.doubleSpinBox.value() <= statusbar_text:
            self.statusbar.setStyleSheet("background-color : red")
        else:
            self.statusbar.setStyleSheet("background-color : green")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
