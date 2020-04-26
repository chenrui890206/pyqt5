from PyQt5.Qt import *
from PIL import Image
import sys


class Window(QWidget):
    # 方式一：重写contextMenuEvent，鼠标右键调用此方法
    def contextMenuEvent(self, evt):
        print("默认上下文菜单调用这个方法")
        menu = QMenu(self)

        # 子菜单 最近打开

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")
        # open_recent_menu.setIcon()

        # 行为动作 新建  打开  分割线 退出
        # new_action = QAction()
        # new_action.setText("新建")
        # new_action.setIcon(QIcon("xxx.png"))
        new_action = QAction(QIcon("xxx.png"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建文件"))

        open_action = QAction(QIcon("xxx.png"), "打开", menu)
        open_action.triggered.connect(lambda: print("打开文件"))

        exit_action = QAction("退出", menu)
        exit_action.triggered.connect(lambda: print("退出程序"))

        file_action = QAction("Python-GUI编程-PyQt5")

        menu.addAction(new_action)
        menu.addAction(open_action)
        open_recent_menu.addAction(file_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()
        menu.addAction(exit_action)

        # point
        menu.exec_(evt.globalPos())
        # menu.exec_(evt.pos())

app = QApplication(sys.argv)
window = Window()

window.setWindowTitle("右键菜单")
window.resize(500, 500)

def show_menu(point):
    menu = QMenu(window)

    # 子菜单 最近打开

    open_recent_menu = QMenu(menu)
    open_recent_menu.setTitle("最近打开")
    # open_recent_menu.setIcon()

    # 行为动作 新建  打开  分割线 退出
    # new_action = QAction()
    # new_action.setText("新建")
    # new_action.setIcon(QIcon("xxx.png"))
    new_action = QAction(QIcon("xxx.png"), "新建", menu)
    new_action.triggered.connect(lambda: print("新建文件"))

    open_action = QAction(QIcon("xxx.png"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))

    exit_action = QAction("退出", menu)
    exit_action.triggered.connect(lambda: print("退出程序"))

    file_action = QAction("Python-GUI编程-PyQt5")

    menu.addAction(new_action)
    menu.addAction(open_action)
    open_recent_menu.addAction(file_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()
    menu.addAction(exit_action)

    # 坐标由局部转为全局
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)

"""
设置右键菜单策略
Qt.DefaultContextMenu：调用对象方法contextMenuEvent()
Qt.CustomContextMenu：发射信号给槽函数，传递point坐标
"""
#
window.setContextMenuPolicy(Qt.CustomContextMenu)

# 方式二：发射信号给槽函数，传递point坐标
window.customContextMenuRequested.connect(show_menu)

window.show()

sys.exit(app.exec_())
