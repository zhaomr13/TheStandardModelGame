from PyQt5.QtCore import (qAbs, QLineF, QSizeF, QPointF, QRectF, qrand, qsrand, Qt,
        QTime, QTimer)
from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QTextBrowser, QGraphicsPixmapItem, QGraphicsObject, QGraphicsItem)
from PyQt5.QtGui import QPixmap, QBrush

import images_rc

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

class BackgroundPixmap(QGraphicsItem):
    def __init__(self, pixs):
        super(BackgroundPixmap, self).__init__()

        self.p = []
        for pix in pixs:
            self.p.append(QPixmap(pix).scaled(1000, 1000))
            print(self.p)
        self.current = 0

    def paint(self, painter, option, widget):
        print("drawing")
        painter.drawPixmap(QPointF(0, 0), self.p[self.current])

    def boundingRect(self):
        return QRectF(QPointF(0, 0), QSizeF(1000, 1000))


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
        self.setMinimumSize(1000, 1000)

class CanvasViewer():
    def __init__(self):
        self.scene = Scene()
        self.canvas = Canvas(self.scene, parent=None)
        self.cover = BackgroundPixmap([":/images/cover.png", ":/images/map.png"])
        # self.item = QGraphicsPixmapItem(self.cover)
        self.scene.addItem(self.cover)
        # self.item.show()
        # self.cover.setVisible(False)
        # self.maze = QGraphicsPixmapItem(QPixmap(":/images/map.png").scaled(1000, 1000))
        # self.maze.setVisible(False)
        # self.background = self.cover
        # self.scene.addItem(self.maze)
        self.set_background("cover")

    def set_text(self, text):
        self.monitor.setText(text)

    def set_background(self, picture):
        if picture == "map":
            self.cover.current = 0
            self.cover.update()
            # self.background.setVisible(False)
            # self.maze.setVisible(True)
            # self.background = self.maze
        if picture == "cover":
            self.cover.current = 1
            self.cover.update()
            # self.background.setVisible(False)
            # self.cover.setVisible(True)
            # self.background = self.cover
        # self.item.show()
        self.canvas.show()
