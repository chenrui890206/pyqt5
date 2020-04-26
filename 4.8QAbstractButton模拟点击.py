from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("这是按钮")
btn.move(200, 200)
btn.pressed.connect(lambda :print("点击了这个按钮"))


btn.click()

btn.animateClick(2000)


btn2 = QPushButton(window)
btn2.setText("按钮2")
def test():
    # 无效果普通点击
    # btn.click()

    # 带延迟的有效果点击
    btn.animateClick(1000)
btn2.pressed.connect(test)

window.show()

sys.exit(app.exec_())
