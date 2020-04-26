from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("窗口标志[*]")
window.resize(500, 500)

"""
是否可用

"""

btn = QPushButton(window)
btn.setText("button")

# 设置控件不可用
btn.setEnabled(False)

# 获取是否可用状态
print(btn.isEnabled())

# 设置控件是否显示
btn.setVisible(True)

"""
setHidden(),hide(),show()最终都是调用setVisible()方法
如果控件被遮挡则无法看到
"""

# 设置控件是否隐藏
btn.setHidden(True)

# 隐藏控件不显示
btn.hide()

# 显示控件
btn.show()

# 判定控件是否隐藏
print(btn.isHidden())

# 获取控件最终状态是否可见
print(btn.isVisible())

# 如果能随着widget控件的显示和隐藏, 而同步变化, 则返回True
print(btn.isVisibleTo(window))

btn.destroyed.connect(lambda : print("按钮被释放了"))

# 关闭控件的同时删除该控件
btn.setAttribute(Qt.WA_DeleteOnClose, True)

# 关闭控件
btn.close()


# 窗口处于编辑状态，显示星号
window.setWindowModified(True)

# 是否在编辑状态
print(window.isWindowModified())

# 窗口是否是活跃窗口
print(window.isActiveWindow())

window.show()

sys.exit(app.exec_())