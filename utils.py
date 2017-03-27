from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QMessageBox
def show_message(title, message):
    #QMessageBox.standardIcon(
    #            QStyle.SP_MessageBoxInformation), "Information",
    #            QSystemTrayIcon.Information)
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(.Information)
    # icon = tray_icon.Information
    tray_icon.showMessage(title, message)
    tray_icon.show()
