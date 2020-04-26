from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("透明度")
window.resize(500, 500)

# 构造方法：图标，标题，父对象
btn = QPushButton(QIcon("position.png"), "xxx", window)
# btn.setParent(window)
# btn.setText("xxx")
# btn.setIcon(QIcon("position.png"))

window.show()

sys.exit(app.exec_())
