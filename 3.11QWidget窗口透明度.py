from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("透明度")
window.resize(500, 500)

# 设置透明度0-1
window.setWindowOpacity(0.4)

# 拿到透明度
print(window.windowOpacity())

window.show()

sys.exit(app.exec_())