from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QLineEdit, QTextEdit, QSpinBox, QSpacerItem)

from PyQt5.QtCore import QObject, pyqtProperty, QPointF
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem

import avatar_rc


# class Pixmap(QObject):
    # def __init__(self, pix):
        # super(Pixmap, self).__init__()

        # self.pixmap_item = QGraphicsPixmapItem(QPixmap(pix))
        # self.pixmap_item.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    # def _set_pos(self, pos):
        # self.pixmap_item.setPos(pos)

    # pos = pyqtProperty(QPointF, fset=_set_pos)

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        # self.
        self.avatar = []
        super(Scene, self).__init__(parent)

        for index in range(2):
            print(QPixmap(":/images/avatar/1.jpg"))
            # self.avatar.append(QPixmap(":/images/avatar/%d.png"%index) )
            self.avatar.append(QGraphicsPixmapItem(QPixmap(":/images/avatar/%d.png"%index) ))
        for index in range(2):
            super(Scene, self).addItem(self.avatar[index])
            # self.avatar[index].setPos(0,0)
        self.current_avatar = self.avatar[0]
        # self.current_avatar.show()
        # self.setGeometry(100, 100, 1000, 1000)

    def changeAvatar(self, index):
        if index > 2: index = 2
        self.current_avatar.setVisible(False)
        self.current_avatar = self.avatar[index]
        self.current_avatar.setVisible(True)

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

class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setText(text)

class RegisterDialog(QDialog):
    def __init__(self, parent):
        super(RegisterDialog, self).__init__(parent)
        self.scene = Scene()
        # self.scene.addPixmap(QPixmap(":/images/avatar/1.png"))

        self.viewer = Canvas(self.scene)
        self.register = Button("Register")
        self.spin_box = QSpinBox()
        self.spin_box.valueChanged.connect(self.changeAvatar)
        splitter = QSplitter()
        # self.address = QLineEdit("192.168.20.20:8088")
        self.address = QLineEdit("192.168.3.17:8088")
        layout = QHBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(splitter)
        sublayout = QVBoxLayout()
        spacer = QSpacerItem(300, 150)
        sublayout.addWidget(self.spin_box)
        sublayout.addItem(spacer)
        sublayout.addWidget(self.address)
        sublayout.addWidget(self.register)
        # address.add
        layout.addLayout(sublayout)
        self.setLayout(layout)
        self.viewer.show()
        # self.viewer.update()

    def get_host(self):
        return self.address.text().split(":")[0]

    def get_port(self):
        return int(self.address.text().split(":")[1])

    def get_username(self):
        return "Mingrui Zhao"

    def get_avatar(self):
        return self.spin_box.value()

    def enable(self):
        pass

    def disable(self):
        pass

    def changeAvatar(self):
        index = self.spin_box.value()
        self.scene.changeAvatar(index)
