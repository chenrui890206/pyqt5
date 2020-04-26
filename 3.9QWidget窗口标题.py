from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.resize(500, 500)

# 设置标题
window.setWindowTitle("社会我顺哥,人狠话不多")

# 拿到标题
print(window.windowTitle())

window.show()

sys.exit(app.exec_())