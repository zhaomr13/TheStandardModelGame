from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QTextBrowser, QGraphicsPixmapItem, QTextBrowser)
from PyQt5.QtGui import QPixmap, QBrush

import images_rc
import utils

"""

class Pixmap(QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QGraphicsPixmapItem(pix)
        self.pixmap_item.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)
"""

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        # self.
        super(Scene, self).__init__(parent)
        # self.setGeometry(100, 100, 1000, 1000)

    def add_detector(self, thedetector):
        super(Scene, self).addItem(thedetector.pixmap)

    # def paintEvent(self, event):
    # pass

    # def timerEvent(self, event):
        # self.show()
        # self.update()

class Canvas(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(Canvas, self).__init__(scene, parent)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)
        # self.setGeometry(300, 300)

class MessageBox(QTextBrowser):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 300)

class StatusMonitor(QWidget):
    def __init__(self):
        self.scene = Scene()
        self.canvas = Canvas(self.scene, parent=None)
        self.cover = QGraphicsPixmapItem(QPixmap(":/images/cover.png").scaled(300, 300))
        self.cover.setVisible(False)
        self.maze = QGraphicsPixmapItem(QPixmap(":/images/map.png").scaled(300, 300))
        self.maze.setVisible(False)
        self.background = self.cover
        self.scene.addItem(self.cover)
        self.scene.addItem(self.maze)
        self.set_background("cover")
        self.messagebox = MessageBox()

    def set_text(self, text):
        self.monitor.setText(text)

    def set_background(self, picture):
        if picture == "map":
            self.background.setVisible(False)
            self.maze.setVisible(True)
        if picture == "cover":
            self.background.setVisible(False)
            self.cover.setVisible(True)
        self.canvas.show()

    def show_message(self, message):
        print("Utils.show message")
        utils.show_message(message, message)

    def set_buying_node(self):
        pass
