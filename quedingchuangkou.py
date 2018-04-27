from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
import sys
from PyQt5 import QtGui
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message',"Are you sure to close?",QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if (reply==QMessageBox.No):
           event.ignore()
        if(reply==QMessageBox.Yes):
           event.accept()
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())