from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject设置对象名字()
        self.QObject设置对象属性()

    def QObject设置对象名字(self):
        obj0 = QObject()
        # 1.设置对象名字
        obj0.setObjectName("这是Obj0")
        # 2.获取对象名字
        print(obj0.objectName())

    def QObject设置对象属性(self):
        obj1 = QObject()
        obj1.setProperty("key", "value")
        # 1.获取对象的属性值
        print(obj1.property("key"))
        # 2.获取一个对象中所有通过setProperty()设置的属性名称
        obj1.setProperty("key123", "value123")
        print(obj1.dynamicPropertyNames())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
