from PyQt5.QtGui import QPixmap
class Node():
    def __init__(self):
        self.name = ""
        self.pos = None
        self.pixmap = None
        self.viewer = None
        self.owner = -1

    def change_owner(self, index):
        pass


def register_nodes(viewer):
    detector_list = []
    d_Atlas = Detector()
    d_Atlas.name = "ATLAS detector"
    d_Atlas.cost = 1000
    d_Atlas.pixmap = QPixmap(":/images/buttons/demo.jpg")
    detector_list.append(d_Atlas)

    return detector_list
