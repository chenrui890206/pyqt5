from PyQt5.Qt import *
from PIL import Image
import sys

class Window(QWidget):
    def mousePressEvent(self, evt):
        # 查看获取焦点的控件
        # print(self.focusWidget())

        # 使下个控件获取焦点
        # self.focusNextChild()

        # 使上个控件获取焦点
        # self.focusPreviousChild()

        # 使得上个或下个控件获取焦点
        self.focusNextPrevChild(True)

app = QApplication(sys.argv)
window = Window()

window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(150, 150)

# 获取焦点
# le2.setFocus()

# Tab键获取焦点
# le2.setFocusPolicy(Qt.TabFocus)

# 鼠标单击获取焦点
# le2.setFocusPolicy(Qt.ClickFocus)

# Tab或鼠标单击获取焦点
# le2.setFocusPolicy(Qt.StrongFocus)

# 不能通过上两种方式获得焦点(默认值),setFocus仍可使其获得焦点
# le2.setFocusPolicy(Qt.NoFocus)

# 取消焦点
# le2.clearFocus()

# 获取焦点的顺序设置
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

window.show()

sys.exit(app.exec_())