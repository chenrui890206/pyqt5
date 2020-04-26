from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject信号与槽()

    def QObject信号与槽(self):
        # 连接窗口标题变化的信号  与  槽
        def cao(title):
            print("窗口标题变化了", title)

            # 2.阻断信号方式1：事件.disconnect()
            # self.windowTitleChanged.disconnect()

            # 3.阻断信号方式2：对象.blockSignals(True)
            self.blockSignals(True)
            self.setWindowTitle("撩课-" + title)
            self.blockSignals(False)

            # 4.返回连接到信号的接收器数量
            print(self.receivers(self.windowTitleChanged))


        # 1.事件.connect(槽函数)：当触发事件时，触发相应的槽函数
        self.windowTitleChanged.connect(cao)

        self.setWindowTitle("Hello Sz")
        self.setWindowTitle("Hello Sz2")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    # window = QWidget()
    window.show()
    sys.exit(app.exec_())
