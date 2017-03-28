#!/bin/python

from PyQt5.QtCore import QTimer, QByteArray
from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QHBoxLayout, QVBoxLayout)
from PyQt5.QtNetwork import (QTcpSocket)

from agent import Agent
from step import Step
from viewer import CanvasViewer
from register import RegisterDialog
from utils import show_message
from utils import Button
from PyQt5.QtWidgets import QTextBrowser as StatusMonitor

class ServerIO():
    def __init__(self, socket):
        self.status = "register"
        self.socket = socket
        self.time = 0
        self.my_turn = False
        self.step = Step()
        self.this_user = 0

    def update_data(self):
        message = self.socket.readLine().data().decode()
        print("update data", message)
        new_step = Step()
        new_step.from_string(message)
        if new_step.user == self.this_user:
            self.my_turn = True
        else:
            self.my_turn = False
        self.step = new_step


    def is_my_turn(self):
        return self.my_turn

    def get_step(self):
        return self.step

    def send_message(self, step):
        print("send")
        message = step.to_string()
        qmessage = QByteArray()
        qmessage.append(message)
        print(message)
        self.socket.write(qmessage)

class Client(QWidget):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)

        self.socket = QTcpSocket()
        self.socket.readyRead.connect(self.update_status)
        self.socket.connected.connect(self.set_is_connected)
        self.remote = ServerIO(self.socket)

        self.viewer = CanvasViewer()
        self.monitor = StatusMonitor()
        self.b_next_turn = Button("Next Round")
        # self.b_register = Button("Register")
        self.set_layout()

        self.register_dialog = RegisterDialog(self)
        self.register_dialog.show()
        self.register_dialog.b_register.clicked.connect(self.register)

        self.agent = Agent(self.viewer, self.monitor)

        self.setWindowTitle("The Standard Model Game")

    def set_layout(self):
        self.b_next_turn.setEnabled(False)
        layout = QHBoxLayout()
        sublayout = QVBoxLayout()
        layout.addWidget(self.viewer.canvas)
        sublayout.addWidget(self.b_next_turn)
        self.b_next_turn.clicked.connect(self.next_turn)
        layout.addLayout(sublayout)
        self.setLayout(layout)

    def next_turn(self):
        step = Step()
        step.action = "next turn"
        self.remote.send_message(step)

    def update_status(self):
        print("update status")
        self.remote.update_data()
        my_turn = self.remote.is_my_turn()
        step = self.remote.get_step()
        if self.agent.is_leagal_step(step):
            self.agent.process(step)
            print("process step")
        else:
            print("Something is wrong!!!")

        self.disable_buttons()

    def disable_buttons(self):
        self.b_next_turn.setEnabled(True)


    def register(self):
        host = self.register_dialog.get_host()
        port = self.register_dialog.get_port()
        self.socket.connectToHost(host, port)

    def init(self):
        # self.setGeometry(100, 100, 1000, 1000)
        pass

    def set_is_connected(self):
        username = self.register_dialog.get_username()
        avatar = self.register_dialog.get_avatar()
        qmessage = QByteArray()
        qmessage.append("%s@%d\n"%(username, avatar) )
        self.socket.write(qmessage)
        self.register_dialog.setVisible(False)


# main
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    show_message("hello", "hello")
    client = Client()
    # window.init()
    client.show()
    sys.exit(app.exec_())

