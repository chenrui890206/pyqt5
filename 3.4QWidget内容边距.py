from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("内容边距的设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("社会我顺哥, 人狠话不多")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan;")

# 设置内容边距(左, 上, 右, 下)
label.setContentsMargins(100, 200, 0, 0)

# 获取内容边距(左, 上, 右, 下)
print(label.getContentsMargins())

# 获取内容区域(左, 上, 右, 下)
print(label.contentsRect())

window.show()

sys.exit(app.exec_())