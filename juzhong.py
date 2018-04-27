import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
#QtGui.QDesktopWidget类提供了用户的桌面信息，其中就有屏幕的大小。
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(250,150)     #因为这个类是QWidget的子类所以对象就是一个窗口
        self.center()
        self.setWindowTitle('Center')
        self.show()
    def center(self):
        qr = self.frameGeometry()                           #self是创建的窗口，这样可以得到窗口的大小
        cp= QDesktopWidget().availableGeometry().center()   #获取到显示器的分辨率，然后得到了中间点的位置存储到cp中
        qr.moveCenter(cp)                                   #qr窗口移动到中心点
        self.move(qr.topLeft())                             #self还是窗口，self.move是窗口移动，，，然后把窗口的坐上角移动到qr的矩形的左上角上，这样就居中了我们自己的窗口。

if __name__=='__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
