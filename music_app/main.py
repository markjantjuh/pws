__author__ = 'MarkJan'

#imports
import sys
from PyQt4 import QtGui
from user_interface import Ui_MainWindow

#application
class Main(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #bind functions to UI

#start application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

