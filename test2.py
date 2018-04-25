import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
if __name__=='__main__':                       #当你选中了这个模块直接运行时候模块名为main()，当时被导入时候模块不被运行
    #每一行pyqt5应用程序必须创建一个应用程序对象。
    app=QApplication(sys.argv)
    #QWidget不见是pyqt5所有用户界面对象的基类。他为QWidget提供默认的构造函数，默认构造函数没有父类。
    w=QWidget()
    #resize()方法调整窗口大小
    w.resize(250,150)
    #move()方法移动窗口在屏幕上的为位置到x=300,y=300坐标
    w.move(300,300)
    #设置窗口的标题
    w.setWindowTitle('Simple')
    #显示在屏幕上
    w.show()


    #系统exit（）方法确保应用程序干净的推出
    #exec_()方法有下划线。因为执行是一个Python关键字。因此，exec_()
    sys.exit(app.exec_())

