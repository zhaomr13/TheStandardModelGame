from PyQt5.QtCore import (qAbs, QLineF, QSizeF, QPointF, QRectF, qrand, qsrand, Qt,
        QTime, QTimer)
from PyQt5.QtWidgets import (QWidget, QToolButton, QGraphicsScene, QGraphicsView, QTextBrowser, QGraphicsPixmapItem, QGraphicsObject, QGraphicsItem)
from PyQt5.QtGui import QPixmap, QBrush
from utils import Button

class Controller():
    def __init__(self):
        self.b_buy_node = Button("Buy Place")
        self.b_build_detector = Button("Build Detector")
        self.b_next_turn = Button("Next Round")
        self.b_buy_node.setEnabled(False)
        self.b_build_detector.setEnabled(False)
        self.b_next_turn.setEnabled(False)

    def set_buying_node(self):
        self.b_buy_node.setEnabled(False)
        self.b_build_detector.setEnabled(False)
        self.b_next_turn.setEnabled(False)

    # def keyReleaseEvent(self, event):
    # if event.key() == Qt.Key_Escape:
