from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QHBoxLayout, QVBoxLayout)
from PyQt5.QtNetwork import (QTcpSocket)

from game import Agent
from game import Step
from viewer import Viewer
from register import RegisterDialog

def is_next_step(step):
    return True

class AskServer():
    def __init__(self, socket):
        self.socket = socket
        self.time = 0
        self.my_turn = False
        self.step = Step()

    def update_data(self):
        if not self.socket.readyRead():
            return
        message = self.socket.readLine()
        new_step = Step()
        new_step.from_string(message)
        if new_step.user == this_user:
            self.my_turn = True
        else:
            self.my_turn = False
        self.step = new_step

    def is_my_turn(self):
        message = self.socket.readLine()
        print(message, "*")
        return True
        self.update_data()
        return self.my_turn

    def get_step(self):
        return Step()
        self.update_data()
        return self.step()

class SendServer():
    def __init__(self, socket):
        self.socket = socket

    def send_message(self, step):
        message = step.to_string()
        self.socket.write(message)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.socket = QTcpSocket()
        self.ask = AskServer(self.socket)
        self.send = SendServer(self.socket)

        timer = QTimer(self)
        timer.timeout.connect(self.loop)
        timer.setInterval(1)
        timer.start()


        self.viewer = Viewer()
        self.agent = Agent(self.viewer)
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.show()

        layout = QHBoxLayout()
        sublayout = QVBoxLayout()
        layout.addWidget(self.viewer.canvas)
        sublayout.addWidget(self.viewer.next_turn)
        layout.addLayout(sublayout)
        # layout.addWidget(self.viewer.address)
        self.register_dialog.register.clicked.connect(self.register)
        self.setLayout(layout)
        # controller.next_turn.clicked.connect(self.next_turn())


        self.setWindowTitle("The Standard Model Game")

    def loop(self):
        my_turn = self.ask.is_my_turn()
        step = self.ask.get_step()
        if self.agent.is_leagal_step(step):
            self.agent.process(step)
        else:
            print("Something is wrong!!!")

        if (my_turn):
            self.viewer.enable()
        else:
            self.viewer.disable()

        # print("hehehe")

    def register(self):
        self.socket.connectToHost("192.168.1.107", 8088)
        self.socket.write("Mingrui Zhao@12")
        self.register_dialog.setVisiable(False)

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

