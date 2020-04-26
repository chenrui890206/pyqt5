from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("图标")
window.resize(500, 500)

# 从路径获取图标
icon = QIcon("position.png")
window.setWindowIcon(icon)

# 拿到QIcon
print(window.windowIcon())

window.show()

sys.exit(app.exec_())