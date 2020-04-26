from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("窗口标志")
window.resize(500, 500)

"""
窗口样式：
Qt.Widget：窗口，带边框和标题栏；有父控件则为空白控件
Qt.Window：窗口，带边框和标题栏
Qt.Dialog：对话窗口
Qt.Sheet：窗口或部件Macintosh表单
Qt.Drawer：窗口或部件Macintosh抽屉
Qt.Popup：弹出式顶层窗口
Qt.Tool：工具窗口
Qt.ToolTip：提示窗口，没有标题栏和窗口边框
Qt.SplashScreen：欢迎窗口，是QSplashScreen构造函数的默认值
Qt.SubWindow：子窗口

顶层窗口外观标志：
Qt.MSWindowsFixedSizeDialogHint：窗口无法调整大小
Qt.FramelessWindowHint：窗口无边框
Qt.CustomizeWindowHint：有边框但无标题栏和按钮，不能移动和拖动
Qt.WindowTitleHint：添加标题栏和一个关闭按钮
Qt.WindowSystemMenuHint：添加系统目录和一个关闭按钮
Qt.WindowMaximizeButtonHint：激活最大化和关闭按钮，禁止最小化按钮
Qt.WindowMinimizeButtonHint：激活最小化和关闭按钮，禁止最大化按钮
Qt.WindowMinMaxButtonsHint：激活最小化，最大化和关闭按钮
Qt.WindowCloseButtonHint：添加一个关闭按钮
Qt.WindowContextHelpButtonHint：添加问号和关闭按钮，同对话框
Qt.WindowStaysOnTopHint：窗口始终处于所有程序顶层位置
Qt.WindowStaysOnBottomHint：窗口始终处于所有程序底层位置
"""

# 设置窗口用于在顶层
window.setWindowFlags(Qt.WindowStaysOnTopHint)

window.show()

sys.exit(app.exec_())