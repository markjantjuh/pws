__author__ = 'MarkJan'

#imports
import sys
from PyQt4 import QtGui

from music_app.user_interface.main_ui import Ui_File
from user_interface.playlist_ui import Ui_playlist_dialog
from user_interface.add_tags_ui import Ui_add_tags_dialog

import playlist

#application
class Main(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_File()
        self.ui.setupUi(self)

        #bind functions to UI
        #menubinds
        self.ui.open_library.triggered.connect(self.open_library)
        self.ui.add_tags.triggered.connect(self.add_tags)
        self.ui.play_from_disc.triggered.connect(self.play_from_disk)
        self.ui.convert_files.triggered.connect(self.convert_files)
        self.ui.create_playlist.triggered.connect(self.create_playlist)
        self.ui.equalizer.triggered.connect(self.equalizer)

        #playerbinds
        self.ui.Fastbackward.clicked.connect(self.fast_backward)
        self.ui.Fastforward.clicked.connect(self.fast_forward)
        self.ui.Shuffle.clicked.connect(self.shuffle)
        self.ui.Play.clicked.connect(self.play_sound)
        self.ui.Stop.clicked.connect(self.stop_sound)

    def create_playlist(self):
        self.new_window = PlaylistUi()
        self.new_window.show()

        #get input and call create_playlist

    def add_tags(self):
        self.new_window = AddTagsUi()
        self.new_window.show()

    def open_library(self):
        pass

    def play_from_disk(self):
        pass

    def convert_files(self):
        pass

    def equalizer(self):
        pass

    def fast_forward(self):
        pass

    def fast_backward(self):
        pass

    def shuffle(self):
        pass

    def play_sound(self):
        pass

    def stop_sound(self):
        pass

class PlaylistUi(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_playlist_dialog()
        self.ui.setupUi(self)

        self.ui.button_create.clicked.connect(self.createPlaylist)

    def createPlaylist(self):
        self.name = str(self.ui.textbox_name.text())
        playlist.createPlaylist(self.name)

        self.close()

class AddTagsUi(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_add_tags_dialog()
        self.ui.setupUi(self)

#start application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

