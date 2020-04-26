from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject对象删除()

    def QObject对象删除(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda: print("obj1被释放了"))
        obj2.destroyed.connect(lambda: print("obj2被释放了"))
        obj3.destroyed.connect(lambda: print("obj3被释放了"))

        # del obj2
        # 1.deleteLater会在下一次消息循环中才会删除，并且连同所有下级对象一起删除
        obj2.deleteLater()
        # print(obj1.children())
        print(obj2)
        # 才会真正的去释放相关的对象


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
