from PyQt5.QtCore import QTimer, QByteArray
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
        self.status = "register"
        self.socket = socket
        # self.socket.readyRead.connect(self.update_data)
        self.time = 0
        self.my_turn = False
        self.step = Step()
        self.this_user = 0

    def update_data(self):
        # if not self.socket.readyRead():
        # return
        message = str(self.socket.readLine())
        print("update data", message)
        new_step = Step()
        new_step.from_string(message)
        if new_step.user == self.this_user:
            self.my_turn = True
        else:
            self.my_turn = False
        self.step = new_step

    def is_my_turn(self):
        # return True
        # if not self.socket.readyRead():
        # return
        # message = self.socket.readLine()
        # print(message, "*")
        # return True
        # self.update_data()
        return self.my_turn

    def get_step(self):
        return self.step

class SendServer():
    def __init__(self, socket):
        self.socket = socket

    def send_message(self, step):
        print("send")
        message = step.to_string()
        print(message)
        self.socket.write(message)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.socket = QTcpSocket()
        self.socket.readyRead.connect(self.update_status)
        self.ask = AskServer(self.socket)
        self.send = SendServer(self.socket)

        timer = QTimer(self)
        # timer.timeout.connect(self.loop)
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
        self.viewer.next_turn.clicked.connect(self.next_turn)
        layout.addLayout(sublayout)
        # layout.addWidget(self.viewer.address)
        self.register_dialog.register.clicked.connect(self.register)
        self.setLayout(layout)
        # controller.next_turn.clicked.connect(self.next_turn())


        self.setWindowTitle("The Standard Model Game")

    def next_turn(self):
        step = Step()
        step.action = "next turn"
        self.send.send_message(step)

    def update_status(self):
        print("update status")
        self.ask.update_data()
        my_turn = self.ask.is_my_turn()
        step = self.ask.get_step()
        if self.agent.is_leagal_step(step):
            self.agent.process(step)
            print("process step")
        else:
            print("Something is wrong!!!")

        if (my_turn):
            self.viewer.enable()
        else:
            self.viewer.disable()



    def register(self):
        host = self.register_dialog.get_host()
        port = self.register_dialog.get_port()
        username = self.register_dialog.get_username()
        avatar = self.register_dialog.get_avatar()

        self.socket.connectToHost(host, port)
        self.socket.write("%s@%d\n"%(username, avatar) )
        self.register_dialog.setVisible(False)

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

