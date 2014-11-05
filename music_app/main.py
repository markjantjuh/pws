__author__ = 'MarkJan'

#imports
import sys

from PyQt4 import QtGui

import menu
import player
from music_app.user_interface.main_ui import Ui_File



#application
class Main(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_File()
        self.ui.setupUi(self)

        #bind functions to UI

        #menubinds
        self.ui.actionOpen_library.triggered.connect(menu.open_library)
        self.ui.actionAdd_tags.triggered.connect(menu.add_tags)
        self.ui.actionPlay_from_disc.triggered.connect(menu.play_from_disk)
        self.ui.actionConvert_file_s.triggered.connect(menu.convert_file_s)
        self.ui.actionCreate_playlist.triggered.connect(menu.create_playlist)
        self.ui.actionEqualizer.triggered.connect(menu.equalizer)

        #playerbinds
        self.ui.Fastbackward.clicked.connect(player.fast_backward)
        self.ui.Fastforward.clicked.connect(player.fast_forward)
        self.ui.Shuffle.clicked.connect(player.shuffle)
        self.ui.Play.clicked.connect(player.play_sound)
        self.ui.Stop.clicked.connect(player.stop_sound)




#start application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

