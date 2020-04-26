from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("按钮")

# 定义图标
icon = QIcon("position.png")

# 设置图标
btn.setIcon(icon)

# 设置图标大小
size = QSize(50, 50)
btn.setIconSize(size)

btn.pressed.connect(lambda :print("按钮被点击了"))

# 设置快捷键为Alt+b
# btn.setText("a&bc")

# 设置快捷键
btn.setShortcut("Alt+b")

window.show()

sys.exit(app.exec_())
