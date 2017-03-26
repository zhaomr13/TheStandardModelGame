from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QHostAddress, QTcpServer

class Server(QObject):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)

        self.server = QTcpServer()

        self.server.listen(QHostAddress.Any, 8088)
        self.server.newConnection.connect(self.send)

    def send(self):
        socket = self.server.nextPendingConnection()
        socket.write("hello\n")
        # socket.flush()
        # socket.disconnect()

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    server = Server()
    # server.show()
    sys.exit(app.exec_())
