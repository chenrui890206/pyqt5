from PyQt5.Qt import *


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 22px;")

    def startMyTimer(self, ms):
        # 1.开启定时器startTimer(毫秒，Qt.TimerType)，返回定时器id，在关闭定时器时用到此id
        # Qt.PreciseTimer：精确定时器（尽可能保持毫秒准确）
        # Qt.CoarseTimer：粗定时器（5%的误差，默认）
        # Qt.VeryCoarseTimer：很粗的定时器（只能到秒级）
        self.timer_id = self.startTimer(ms, Qt.CoarseTimer)

    # 2.定时器执行的方法
    def timerEvent(self, *args, **kwargs):
        print("xx")
        # 获取当前的标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            # 3.杀掉定时器任务（timer_id）
            self.killTimer(self.timer_id)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject定时器()

    def QObject定时器(self):
        label = MyLabel(self)
        label.setText("10")
        label.startMyTimer(1000)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
