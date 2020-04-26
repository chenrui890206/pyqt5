from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("菜单")
window.resize(500, 500)

btn = QPushButton(window)
btn.setParent(window)
btn.setText("xxx")
btn.setIcon(QIcon("position.png"))

# 1.新建菜单
menu = QMenu(btn)

# 子菜单 最近打开

open_recent_menu = QMenu(menu)
open_recent_menu.setTitle("最近打开")
# open_recent_menu.setIcon()


# 行为动作
# new_action = QAction()
# new_action.setText("新建")
# new_action.setIcon(QIcon("xxx.png"))

# 2.新建行为，icon，名称，所属菜单
new_action = QAction(QIcon("position.png"), "新建", menu)
new_action.triggered.connect(lambda :print("新建文件"))

open_action = QAction(QIcon("position.png"), "打开", menu)
open_action.triggered.connect(lambda :print("打开文件"))

exit_action = QAction("退出", menu)
exit_action.triggered.connect(lambda :print("退出程序"))

file_action = QAction("Python-GUI编程-PyQt5")

# 3.将元素加入菜单（行为，子菜单，分割线等）
menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(exit_action)

# 4.给按钮绑定菜单
btn.setMenu(menu)

window.show()

sys.exit(app.exec_())
