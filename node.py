from PyQt5.QtCore import QPointF, QSizeF, QRectF, QObject, pyqtSignal
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QPixmap

import icons_rc

class NodePixmap(QGraphicsItem):
    def __init__(self, no_user_pix_name, highlight_pix_name, normal_pixs_name):
        super(NodePixmap, self).__init__()

        self.index = -1
        self.x = 0
        self.y = 0
        self.owner = None
        self.visible_flag = False
        self.highlight_flag = False
        self.no_user_pix = QPixmap(no_user_pix_name).scaled(100, 100)
        self.highlist_pix = QPixmap(highlight_pix_name).scaled(100, 100)
        self.normal_pixs = []
        for pix_name in normal_pixs_name:
            self.normal_pixs.append(QPixmap(pix_name).scaled(100, 100))
        self.clicked_signal = None

    def paint(self, painter, option, widget):
        if not self.can_show: return
        if self.highlight_flag:
            painter.drawPixmap(QPointF(self.x, self.y), self.highlight_pix)
        elif self.owner is None:
            painter.drawPixmap(QPointF(self.x, self.y), self.no_user_pix)
        else:
            painter.drawPixmap(QPointF(self.x, self.y), self.normal_pixs[self.owner.index])

    def boundingRect(self):
        return QRectF(QPointF(self.x, self.y), QSizeF(100, 100))

    def mousePressEvent(self, event):
        print("emit", self.clicked_signal)
        self.clicked_signal.emit(self.index)
        print("node", "pressed")

    def mouseMoveEvent(self, event):
        print("moving")

    def mouseHoveEvent(self, event):
        # def enterEvent(self, event):
        print("enter")

class Node(QObject):
    clicked = pyqtSignal(int)
    def __init__(self, parent=None):
        super(Node, self).__init__(parent)
        self.cost = 0
        self.name = ""
        self.index = -1
        self.pos = None
        self.pixmap = None
        self.viewer = None
        self.monitor = None
        self.owner = None
        self.neighboors = []
        self.can_buy_flag = False

    def show_information(self):
        message = "Name: %s\nCost: %d$\n"%(self.name, self.cost)
        if self.owner is not None:
            message += "Owner: %s\n"%(self.owner.username)
            message += self.owner.get_information()
        self.monitor.set_text(message)

    def can_buy(self):
        return self.can_buy_flag

    def set_can_buy(self):
        self.can_buy_flag = True
        self.set_highlight(True)

    def set_normal(self):
        self.can_buy_flag = False
        self.set_highlight(False)

    def is_neighboor(self, node):
        return node in self.neighboors

    def register_pixmap(self, no_user_pix_name, highlight_pix_name, normal_pixs_name):
        self.pixmap = NodePixmap(no_user_pix_name, highlight_pix_name, normal_pixs_name)
        print(self.pixmap)
        self.pixmap.owner = self.owner
        self.pixmap.x = self.pos[0]
        self.pixmap.y = self.pos[1]
        self.pixmap.index = self.index
        self.pixmap.clicked_signal = self.clicked
        self.viewer.scene.addItem(self.pixmap)
        # self.pixmap.clicked.connect(self.clicked)

    def set_visible(self, status):
        self.pixmap.can_show = status
        self.pixmap.update()

    def set_highlight(self, status):
        self.pixmap.highlight = status
        self.pixmap.update()

    def change_owner(self, owner):
        self.owner = owner
        self.pixmap.owner = owner
        self.pixmap.update()


def register_nodes(viewer, monitor):
    no_user = ":images/nodes/nouser.png"
    highlight = ":images/icons/heart.png"
    normal_pixs = [":images/nodes/u0.png", ":images/nodes/u1.png", ":images/nodes/u2.png", ":images/nodes/u3.png"]
    nodes_list = []

    node0 = Node()
    node0.index = 0
    node0.name = "Node0"
    node0.pos = (100, 100)
    node0.viewer = viewer
    node0.monitor = monitor
    node0.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node0)

    node1 = Node()
    node1.index = 1
    node1.name = "Node0"
    node1.pos = (300, 100)
    node1.viewer = viewer
    node1.monitor = monitor
    node1.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node1)

    node2 = Node()
    node2.index = 2
    node2.name = "node2"
    node2.pos = (500, 100)
    node2.viewer = viewer
    node2.monitor = monitor
    node2.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node2)

    node3 = Node()
    node3.index = 3
    node3.name = "node3"
    node3.pos = (100, 300)
    node3.viewer = viewer
    node3.monitor = monitor
    node3.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node3)

    node4 = Node()
    node4.index = 4
    node4.name = "CERN"
    node4.pos = (300, 300)
    node4.cost = 10000
    node4.viewer = viewer
    node4.monitor = monitor
    node4.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node4)

    node5 = Node()
    node5.index = 5
    node5.name = "node5"
    node5.pos = (500, 300)
    node5.viewer = viewer
    node5.monitor = monitor
    node5.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node5)

    node6 = Node()
    node6.index = 6
    node6.name = "node6"
    node6.pos = (100, 500)
    node6.viewer = viewer
    node6.monitor = monitor
    node6.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node6)

    node7 = Node()
    node7.index = 7
    node7.name = "node7"
    node7.pos = (300, 500)
    node7.viewer = viewer
    node7.monitor = monitor
    node7.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node7)

    node8 = Node()
    node8.index = 8
    node8.name = "node8"
    node8.pos = (500, 500)
    node8.viewer = viewer
    node8.monitor = monitor
    node8.register_pixmap(no_user, highlight, normal_pixs)
    nodes_list.append(node8)

    node0.neighboors = [node1, node3]
    node1.neighboors = [node0, node2, node4]
    node2.neighboors = [node1, node5]
    node3.neighboors = [node0, node4, node6]
    node4.neighboors = [node1, node3, node5, node7]
    node5.neighboors = [node2, node4, node8]
    node6.neighboors = [node3, node7]
    node7.neighboors = [node4, node6, node8]
    node8.neighboors = [node5, node7]

    return nodes_list
