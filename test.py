from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QLineEdit, QTextEdit, QSpinBox, QSpacerItem, QApplication)

from PyQt5.QtCore import QObject, pyqtProperty, QPointF
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem

import test_rc

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        # self.
        self.avatar = []
        super(Scene, self).__init__(parent)

class Canvas(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(Canvas, self).__init__(scene, parent)
        self.setMinimumSize(1000, 1000)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    scene = Scene()
    pixmap = QPixmap(":images/avatar/0.png")
    # pixmap = pixmap.scaledToWidth(scene.width());
    scene.addPixmap(pixmap)

    viewer = Canvas(scene)
    viewer.show()
    sys.exit(app.exec_())
