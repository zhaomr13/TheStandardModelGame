from PyQt5.QtCore import QObject, QTimer, QByteArray
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtNetwork import QHostAddress, QTcpServer

from user import User
from step import Step
from utils import show_message

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(text, parent)

class Server(QWidget):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)

        self.users = []
        self.step_index = 0
        self.active_user = -1
        self.active_socket = None
        import random
        self.nodes_list = range(8)
        random.shuffle(self.nodes_list)
        print self.nodes_list
        self.setWindowTitle("The Standard Model Game Server")

        self.sockets = []

        mainLayout = QVBoxLayout()
        self.register_started = False
        self.b_register_user = Button("Start Register")
        self.b_register_user.clicked.connect(self.register_user_change_status)

        self.game_started = False
        self.b_start = Button("Start")
        self.b_start.clicked.connect(self.start_game)
        mainLayout.addWidget(self.b_register_user)
        mainLayout.addWidget(self.b_start)
        self.setLayout(mainLayout)

        self.server = QTcpServer()

        self.server.listen(QHostAddress.Any, 8088)
        self.server.newConnection.connect(self.registing)

        self.timer = QTimer(self)
        # self.register_timer.timeout.connect(self.registing)
        self.timer.setInterval(1)
        self.timer.start()
        # self.timer.timeout.connect(self.checkout)

    def start_game(self):
        if (len(self.users) == 0):
            show_message("No User Registed", "", 2)
            return

        self.game_started = True
        for user_index, user in enumerate(self.users):
            self.step_index += 1
            step = Step()
            step.user = user_index
            step.index = self.step_index
            step.action = "setup user"
            step.command = [user.username, user.avatar, self.nodes_list[user_index]]
            self.broad_cast(step)

        step = Step()
        step.action = "start game"
        self.process(step)

        self.get_initial_funding()

        step = Step()
        step.action = "next turn"
        self.process(step)

    def get_initial_funding(self):
        pass

    def register_user_change_status(self):
        if self.register_started:
            self.register_started = False
            # self.register_timer.stop()
            self.b_register_user.setText("Start Register")
        else:
            self.register_started = True
            # self.register_timer.start()
            self.b_register_user.setText("Stop Register")

    def register_user(self, socket):
        if socket in self.sockets:
            return
        self.sockets.append(socket)
        socket.waitForReadyRead()
        message = socket.readLine().data().decode().split("@")
        index = len(self.sockets)
        user = User(message[0], int(message[1]), index, None)
        socket.readyRead.connect(lambda: self.checkout(socket))
        self.users.append(user)
        print("Register User")

    def registing(self):
        if self.register_started:
            socket = self.server.nextPendingConnection()
            # address = socket.peerAddress()
            self.register_user(socket)


    def checkout(self, socket):
        #for socket in self.sockets:
        #    socket.write(steps[-1].to_string())
        print("checkout")
        print(self.active_user)
        print(self.active_socket)
        print(socket)

        if self.active_socket is socket:
            print("is")
            message = socket.readLine().data().decode()
            step = Step()
            step.from_string(message)
            self.process(step)

        """
        if self.game_started:
            for socket in self.sockets:
                if socket.readyRead():
                    message = str(socket.readLine().data())
            for socket in self.sockets:
                self.send_step(socket, step)
        """
        # socket = self.server.nextPendingConnection()
        # socket.write("hello\n")
        # socket.flush()
        # socket.disconnect()
    def change_to_next_user(self):
        self.active_user += 1
        if self.active_user == len(self.sockets):
            self.active_user = 0
        self.active_socket = self.sockets[self.active_user]

    def broad_cast(self, step):
        print("broading cast")
        for user_index, socket in enumerate(self.sockets):
            if step.action == "setup user":
                step.work_user = user_index
            qmessage = QByteArray()
            qmessage.append(step.to_string())
            socket.write(qmessage)

    def process(self, step):
        if step.action == "start game":
            print("Start game")
            self.step_index += 1
            step.index = self.step_index
            self.broad_cast(step)

        if step.action == "next turn":
            self.change_to_next_user()
            self.step_index += 1
            # step = Step()
            step.from_string("%d@get funding@%d@%d@%d\n"%(self.active_user, self.step_index, self.active_user, 1000))
            self.broad_cast(step)

        if step.action == "buy node":
            self.step_index += 1
            step.index = self.step_index
            self.broad_cast(step)

        # if step.action == "get funding":
        # step.

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    server = Server()
    server.show()
    sys.exit(app.exec_())
