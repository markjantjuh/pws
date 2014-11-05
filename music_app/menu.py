__author__ = 'MarkJan'

from PyQt4 import QtGui
from user_interface.playlist_ui import Ui_playlist_dialog

class Playlist_ui(QtGui.QMainWindow):
    def __init__(self):
        #initialize the UI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_playlist_dialog()
        self.ui.setupUi(self)

        self.ui.button_create.clicked.connect(plaalist)

'''def open_file():
    lineEdit.setText(QFileDialog.getOpenFileName())
    open_library.triggered.connect(selectFile) '''

def plaalist():
    #give input pls
    #return plaalistnaampje
    print "DE FUNCTIE WERKT HOOR"

def add_tags():
    pass

def play_from_disk():
    pass

def convert_files():
    pass

def create_playlist():
    ex = Playlist_ui()
    ex.show()

def equalizer():
    pass

def open_library():
    pass


