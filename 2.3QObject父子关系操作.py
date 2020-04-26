from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject父子关系操作()

    def QObject父子关系操作(self):
        obj0 = QObject()
        obj1 = QObject()
        # 1.设置父类的两种方式
        obj1.setParent(obj0)
        obj2 = QObject(obj0)
        obj2.setObjectName("222")
        obj3 = QObject(obj2)
        obj3.setObjectName("333")
        print(obj0)
        print(obj1)
        print(obj2)
        print(obj3)
        print("-------------------")
        # 2.查看父对象
        # print(obj1.parent())
        # 3.查看所有子对象
        # print(obj0.children())
        # 4.查询特定子类，1：类型，2：objectName，3：Qt.FindChildrenRecursively（默认）递归查找，Qt.FindDirectChildrenOnly只查找子对象
        # print(obj0.findChild(QObject,"333",Qt.FindDirectChildrenOnly))
        # 5.查询指定的多个子类，1：类型，2：objectName，3：Qt.FindChildrenRecursively（默认）递归查找，Qt.FindDirectChildrenOnly只查找子对象
        print(obj0.findChildren(QObject,"333",Qt.FindChildrenRecursively))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
