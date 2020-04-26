from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("最小尺寸最大尺寸限定")
# window.resize(500, 500)

# 设置固定大小，不能改变
window.setFixedSize(500, 500)

# 设置最小尺寸
# window.setMinimumSize(200, 200)

# 设置最大尺寸
# window.setMaximumSize(500, 500)

# 设置最小宽度
# window.setMinimumWidth(500)

# 设置最小高度
# window.setMinimumHeight(600)

# 设置最大宽度
# window.setMaximumWidth(800)

# 设置最大高度
# window.setMaximumHeight(800)

# window.resize(1000, 1000)

window.show()

sys.exit(app.exec_())