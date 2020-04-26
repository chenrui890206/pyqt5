from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("父子关系学习")
window.resize(500, 500)

label1 = QLabel(window)
# label1.setParent()
label1.setText("标签1")
label1.move(200, 200)

label2 = QLabel(window)
# label1.setParent()
label2.setText("标签2")
label2.move(50, 50)

label3 = QLabel(window)
# label1.setParent()
label3.setText("标签3")
label3.move(100, 100)

# 获取坐标点位置的控件
# print(window.childAt(255, 255))

# 获取父类
# print(label2.parentWidget())

# 所有子控件组成的边界矩形
print(window.childrenRect())

window.show()

sys.exit(app.exec_())