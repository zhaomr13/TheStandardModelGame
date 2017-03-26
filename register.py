from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QLineEdit, QTextEdit, QSpinBox, QSpacerItem)

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

class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setText(text)

class RegisterDialog(QDialog):
    def __init__(self, parent):
        super(RegisterDialog, self).__init__(parent)
        self.scene = Scene()
        self.viewer = Canvas(self.scene)
        self.register = Button("Register")
        spinBox = QSpinBox()
        splitter = QSplitter()
        address = QLineEdit("192.168.20.20:8088")
        layout = QHBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(splitter)
        sublayout = QVBoxLayout()
        spacer = QSpacerItem(300, 150)
        sublayout.addWidget(spinBox)
        sublayout.addItem(spacer)
        sublayout.addWidget(address)
        sublayout.addWidget(self.register)
        # address.add
        layout.addLayout(sublayout)
        self.setLayout(layout)

    def enable(self):
        pass

    def disable(self):
        pass

