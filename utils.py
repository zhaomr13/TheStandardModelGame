from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMessageBox
from PyQt5.QtGui import QIcon

import icons_rc
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
