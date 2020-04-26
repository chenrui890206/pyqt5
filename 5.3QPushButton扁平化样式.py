from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("透明度")
window.resize(500, 500)

# 构造方法：图标，标题，父对象
btn = QPushButton(QIcon("position.png"), "xxx", window)

btn.setStyleSheet("background-color: red;")

# 设置扁平化，设置后会取消背景色
btn.setFlat(True)

# 获取是否扁平化
print(btn.isFlat())

window.show()

sys.exit(app.exec_())
