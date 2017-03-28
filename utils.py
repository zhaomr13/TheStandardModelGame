from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMessageBox, QToolButton
from PyQt5.QtGui import QIcon

import icons_rc

class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setText(text)

def show_message(title, message, level=0):
    #QMessageBox.standardIcon(
    #            QStyle.SP_MessageBoxInformation), "Information",
    #            QSystemTrayIcon.Information)
    print("Running show message")
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon(":/images/icons/heart.png"))
    # icon = tray_icon.Information
    tray_icon.show()
    tray_icon.showMessage(title, message)
