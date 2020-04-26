from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QCommandLinkButton使用")
window.resize(500, 500)

btn = QCommandLinkButton("标题", "描述", window)
btn.setText("标题2")
btn.setDescription("社会顺哥")
btn.setIcon(QIcon("position.png"))

print(btn.description())

window.show()

sys.exit(app.exec_())
