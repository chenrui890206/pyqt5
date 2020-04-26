from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("1")


def plus_one():
    num = int(btn.text()) + 1
    # 设置文本，内容为字符串
    btn.setText(str(num))


btn.pressed.connect(plus_one)

window.show()

sys.exit(app.exec_())
