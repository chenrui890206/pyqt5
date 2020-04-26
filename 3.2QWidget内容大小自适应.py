from PyQt5.Qt import *
from PIL import Image
import sys

app = QApplication(sys.argv)
window = QWidget()

window.resize(500, 500)
window.move(100, 100)

label = QLabel(window)
label.setText("社会顺")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")

def changeCao():
    new_content = label.text() + "社会顺"
    label.setText(new_content)
    # 大小会随着内容的改变而改变
    label.adjustSize()


btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100, 300)
btn.clicked.connect(changeCao)

window.show()

sys.exit(app.exec_())