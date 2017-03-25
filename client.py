from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QHBoxLayout)

from game import Agent
from game import Step
from viewer import Viewer

def is_next_step(step):
    return True

class AskServer():
    def __init__(self):
        pass

    def my_turn(self):
        return True

    def get_step(self):
        return Step()

class SendServer():
    def __init__(self):
        pass


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ask = AskServer()
        self.send = SendServer()

        timer = QTimer(self)
        timer.timeout.connect(self.loop)
        timer.setInterval(1)
        timer.start()

        viewer = Viewer()
        self.agent = Agent(viewer)

        layout = QHBoxLayout()
        layout.addWidget(viewer.canvas)
        layout.addWidget(viewer.next_turn)
        self.setLayout(layout)
        # controller.next_turn.clicked.connect(self.next_turn())


        self.setWindowTitle("The Standard Model Game")

    def loop(self):
        my_turn = self.ask.my_turn()
        step = self.ask.get_step()
        if self.agent.is_leagal_step(step):
            self.agent.process(step)
        else:
            print("Something is wrong!!!")

        if (my_turn):
            self.viewer.enable()
        else:
            self.viewer.disable()

        print("hehehe")

    def init(self):
        # self.setGeometry(100, 100, 1000, 1000)
        pass


# main
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.init()
    window.show()
    sys.exit(app.exec_())

