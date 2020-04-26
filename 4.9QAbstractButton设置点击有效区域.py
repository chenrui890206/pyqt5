from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

class Btn(QPushButton):
    # 重写hitButton根据坐标来返回点击是否有效
    def hitButton(self, point):
        # print(point)
        # if point.x() > self.width() / 2:
        #     return True
        # return False

        # 通过给定的一个点坐标, 计算与圆心的距离
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # ((x1 - x2) 平方 + (y1 - y2) 平方) 开平方
        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))
        if distance < self.width() / 2:
            return True

        # 如果距离 < 半径  True
        # 返回 False
        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))
        painter.drawEllipse(self.rect())

btn = Btn(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)

btn.pressed.connect(lambda : print("按钮被按下了"))

window.show()

sys.exit(app.exec_())
