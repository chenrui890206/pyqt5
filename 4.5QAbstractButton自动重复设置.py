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

# 设置自动重复
btn.setAutoRepeat(True)

# 设置初次检测延迟ms
btn.setAutoRepeatDelay(2000)

# 设置自动重复检测间隔ms
btn.setAutoRepeatInterval(1000)

# 获取是否自动重复
print(btn.autoRepeat())

# 获取自动重复检测间隔ms
print(btn.autoRepeatInterval())

# 获取初次检测延迟ms
print(btn.autoRepeatDelay())

window.show()

sys.exit(app.exec_())
