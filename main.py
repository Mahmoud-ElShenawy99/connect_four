from Controller.MainWindowController import MainWindowController
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindowController()
    ui.show()
    sys.exit(app.exec_())

