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

# 获取图标
print(btn.icon())

# 获取图标大小
print(btn.iconSize())

window.show()

sys.exit(app.exec_())
