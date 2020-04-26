from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QMainWindow()
# 懒加载
# 用到的时候, 才会创建
window.statusBar()
window.setWindowTitle("信息提示")
window.resize(500, 500)

# 设置带帮助按钮的窗口
window.setWindowFlags(Qt.WindowContextHelpButtonHint)

# 当鼠标停留在窗口控件身上之后, 在状态栏提示的一段文本
window.setStatusTip("这是窗口")
# 获取状态栏文本
print(window.statusTip())

label = QLabel(window)
label.setText("社会我顺哥")

# 鼠标悬停提示
label.setToolTip("这是一个提示标签")
# 获取鼠标悬停提示文本
print(label.toolTip())
# 设置文本显示时长ms
label.setToolTipDuration(2000)
# 获取文本显示时长ms
print(label.toolTipDuration())

# 只有设置了WindowContextHelpButtonHint并点击才会看到
label.setWhatsThis("这是啥? 这是标签")

window.show()

sys.exit(app.exec_())
