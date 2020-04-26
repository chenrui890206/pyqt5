from PyQt5.Qt import *
from PIL import Image
import sys

class Label(QLabel):
    def mousePressEvent(self, evt):
        # 将控件提升到最上层
        self.raise_()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("层级关系调整")
window.resize(500, 500)

label1 = Label(window)
label1.setText("标签1")
label1.resize(200, 200)
label1.setStyleSheet("background-color: red;")

label2 = Label(window)
label2.setText("标签2")
label2.resize(200, 200)
label2.setStyleSheet("background-color: green;")
# label2.move(200, 200)
label2.move(100, 100)

# 将控件降低到最底层
# label2.lower()
# 将控件提升到最上层
# label1.raise_()

# 让label2放在label1下面
# label2.stackUnder(label1)

window.show()

sys.exit(app.exec_())