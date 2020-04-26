from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("窗口状态")
window.resize(500, 500)

# 获取窗口状态
print(window.windowState() == Qt.WindowNoState)
"""
Qt.WindowNoState：无状态
Qt.WindowMinimized：最小化
Qt.WindowMaximized：最大化
Qt.WindowFullScreen：全屏
Qt.WindowActive：活动窗口
"""


# 设置最大化
window.setWindowState(Qt.WindowMaximized)

window.show()

sys.exit(app.exec_())