from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject定时器()

    def QObject定时器(self):
        label = QLabel(self)
        label.setText("10")
        label.move(100, 100)
        label.setStyleSheet("font-size: 22px;")

        def operate():
            print("jinlaile")
            current_sec = int(label.text())
            current_sec -= 1
            label.setText(str(current_sec))
            if current_sec == 0:
                print("停止")
                # 4.杀掉定时器任务
                label.timer.blockSignals(True)

        # 1.初始化一个定时器
        label.timer = QTimer(self)
        # # 2.计时结束调用operate()方法
        label.timer.timeout.connect(operate)
        # # 3.设置计时间隔并启动
        label.timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
