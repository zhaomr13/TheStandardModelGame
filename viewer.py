from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView)

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
        self.setMinimumSize(500, 500)

class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setText(text)

class Viewer():
    def __init__(self):
        self.scene = Scene()
        self.canvas = Canvas(self.scene, parent=None)
        self.next_turn = Button("Next Round")
        self.next_turn.setEnabled(False)
        self.register = Button("Register")

    def enable(self):
        self.next_turn.setEnabled(True)
        pass

    def disable(self):
        self.next_turn.setEnabled(False)
        pass

