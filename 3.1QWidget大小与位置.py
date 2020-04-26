from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.resize(200, 200)
window.move(100, 100)

"""
父控件：
位置相对于桌面
子控件：
位置相对于父控件
******************
控件显示完毕之后, 具体的位置或者尺寸数据才会正确
******************

x()：框架左顶点到父控件的横向距离
y()：框架左顶点到父控件的纵向距离
y()：框架左顶点到父控件的纵向距离
pos()：x()，y()
width()：内容区域宽度
height()：内容区域高度
size()：width()，height()
frameSize()：带外边框的width()，带外边框的height()
rect()：0，0，width()和height()
geometry()：内容区的左顶点到父控件的横向距离，内容区顶点到父控件的纵向距离，width()，height()
setGeometry()：设置内容区的左顶点到父控件的横向距离，内容区顶点到父控件的纵向距离，width()，height()
frameGeometry()：框架左顶点到父控件的横向距离，框架左顶点到父控件的纵向距离，带外边框的width()，带外边框的height()
"""
print(window.x())
print(window.y())
print(window.pos())
print(window.width())
print(window.height())
print(window.size())
print(window.frameSize())
print(window.rect())
print(window.geometry())
print(window.frameGeometry())
print("*" * 40)
window.show()
print(window.x())
print(window.y())
print(window.pos())
print(window.width())
print(window.height())
print(window.size())
print(window.frameSize())
print(window.rect())
print(window.geometry())
print(window.frameGeometry())

img=Image.open('position.png')
img.show()
sys.exit(app.exec_())