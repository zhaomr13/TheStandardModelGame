from PyQt5.QtGui import QPixmap
class Detector():
    def __init__(self):
        self.name = ""
        self.cost = ""
        self.pixmap = None


def register_detectors():
    detector_list = []
    d_Atlas = Detector()
    d_Atlas.name = "ATLAS detector"
    d_Atlas.cost = 1000
    d_Atlas.pixmap = QPixmap(":/images/buttons/demo.jpg")
    detector_list.append(d_Atlas)

    return detector_list
