__author__ = 'MarkJan'

#imports
import sys
from PyQt4 import QtGui

from music_app.user_interface.main_ui import Ui_File
from user_interface.playlist_ui import Ui_playlist_dialog
from user_interface.add_tags_ui import Ui_add_tags_dialog

import playlist, music_library

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
        self.new_window = AddTagsUi("x")
        self.new_window.show()

    def open_library(self):
        open_library.triggered.QtGui.QFileDialog.getOpenFileName()
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

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
        self.ui.button_cancel.clicked.connect(self.close)

    def createPlaylist(self):
        self.name = str(self.ui.textbox_name.text())
        playlist.createPlaylist(self.name)

        self.close()

class AddTagsUi(QtGui.QMainWindow):
    def __init__(self, filename):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_add_tags_dialog()
        self.ui.setupUi(self)

        self.filename = filename

        self.ui.button_save.clicked.connect(self.editTags)
        self.ui.button_cancel.clicked.connect(self.close)

    def editTags(self):
        self.tag_title = str(self.ui.line_title.text())
        self.tag_genre = str(self.ui.line_genre.text())
        self.tag_artist = str(self.ui.line_artist.text())
        self.tag_album = str(self.ui.line_album.text())
        self.tag_year = str(self.ui.line_year.text())
        self.tag_bpm = str(self.ui.line_bpm.text())
        self.tag_key = str(self.ui.line_key.text())
        self.tag_info = str(self.ui.line_info.text())

        music_library.editTags(self.filename, 'Song Title', self.tag_title)
        music_library.editTags(self.filename, 'Genre', self.tag_genre)
        music_library.editTags(self.filename, 'Artist', self.tag_artist)
        music_library.editTags(self.filename, 'Album', self.tag_album)
        music_library.editTags(self.filename, 'Year', self.tag_year)
        music_library.editTags(self.filename, 'BPM', self.tag_bpm)
        music_library.editTags(self.filename, 'Key', self.tag_key)
        music_library.editTags(self.filename, 'Info', self.tag_info)

#start application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

#banaan

