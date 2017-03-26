from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtNetwork import QHostAddress, QTcpServer

from user import User

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(text, parent)

class Server(QWidget):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)

        self.users = []
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
        self.timer.timeout.connect(self.checkout)

    def start_game(self):
        self.game_started = True

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
        message = str(socket.readLine()).split("@")
        index = len(self.sockets)
        user = User(message[0], message[1], index)
        self.users.append(user)

    def registing(self):
        if self.register_started:
            socket = self.server.nextPendingConnection()
            # address = socket.peerAddress()
            self.register_user(socket)


    def checkout(self):
        for socket in self.sockets:
            socket.write("hello\n")

        if self.game_started:
            for socket in self.sockets:
                if socket.readyRead():
                    message = str(socket.readLine())
            for socket in self.sockets:
                self.send_step(socket, step)
        # socket = self.server.nextPendingConnection()
        # socket.write("hello\n")
        # socket.flush()
        # socket.disconnect()

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    server = Server()
    server.show()
    sys.exit(app.exec_())
