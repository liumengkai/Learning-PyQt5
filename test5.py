import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtCore import QCoreApplication
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn=QPushButton('Quit',self)           #创建一个按钮，第一个是按钮的文本，第二个是按钮的父类
        qbtn.clicked.connect(QCoreApplication.instance().quit)    #这段代码让按钮quit和动作退出程序联系起来
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit button')
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
