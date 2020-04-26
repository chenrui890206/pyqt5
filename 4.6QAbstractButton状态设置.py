from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText("按钮")

# 定义图标
icon = QIcon("position.png")

# 设置图标
btn.setIcon(icon)

# 设置图标大小
size = QSize(50, 50)
btn.setIconSize(size)

btn.pressed.connect(lambda :print("按钮被点击了"))

push_button = QPushButton(window)
push_button.setText("这是QPushButton")
push_button.move(100, 100)

radio_button = QRadioButton(window)
radio_button.setText("这是一个radio")
radio_button.move(100, 150)

checkbox = QCheckBox(window)
checkbox.setText("这是checkbox")
checkbox.move(100, 200)

push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")

# 设置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

# 设为可选中
push_button.setCheckable(True)

# 获取是否可选中
print(push_button.isCheckable())
print(radio_button.isCheckable())
print(checkbox.isCheckable())

# 设为选中
radio_button.setChecked(True)
push_button.setChecked(True)
checkbox.setChecked(True)

# 获取是否选中
print(push_button.isChecked())
print(radio_button.isChecked())
print(checkbox.isChecked())

def cao():
    # 切换选中与不选中
    push_button.toggle()
    radio_button.toggle()
    checkbox.toggle()

    # push_button.setChecked(not push_button.isChecked())


btn.pressed.connect(cao)

# 设为是否可用，即使不可用也可以通过代码控制能否选中
push_button.setEnabled(False)
radio_button.setEnabled(False)
checkbox.setEnabled(False)

window.show()

sys.exit(app.exec_())
