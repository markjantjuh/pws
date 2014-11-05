# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Nov 05 17:13:40 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_File(QtGui.QMainWindow):
    def setupUi(self, File):
        File.setObjectName(_fromUtf8("File"))
        File.resize(1000, 800)
        self.centralwidget = QtGui.QWidget(File)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Play = QtGui.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(475, 700, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        self.Play.setFont(font)
        self.Play.setObjectName(_fromUtf8("Play"))
        self.Fastforward = QtGui.QPushButton(self.centralwidget)
        self.Fastforward.setGeometry(QtCore.QRect(595, 700, 75, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        self.Fastforward.setFont(font)
        self.Fastforward.setObjectName(_fromUtf8("Fastforward"))
        self.Fastbackward = QtGui.QPushButton(self.centralwidget)
        self.Fastbackward.setGeometry(QtCore.QRect(330, 700, 75, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        self.Fastbackward.setFont(font)
        self.Fastbackward.setObjectName(_fromUtf8("Fastbackward"))
        self.Shuffle = QtGui.QPushButton(self.centralwidget)
        self.Shuffle.setGeometry(QtCore.QRect(415, 700, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        self.Shuffle.setFont(font)
        self.Shuffle.setObjectName(_fromUtf8("Shuffle"))
        self.Stop = QtGui.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(535, 700, 50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        self.Stop.setFont(font)
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.Progressbar = QtGui.QSlider(self.centralwidget)
        self.Progressbar.setGeometry(QtCore.QRect(10, 670, 980, 19))
        self.Progressbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Progressbar.setOrientation(QtCore.Qt.Horizontal)
        self.Progressbar.setObjectName(_fromUtf8("Progressbar"))
        File.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(File)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSound = QtGui.QMenu(self.menubar)
        self.menuSound.setObjectName(_fromUtf8("menuSound"))
        File.setMenuBar(self.menubar)
        self.open_library = QtGui.QAction(File)
        self.open_library.setObjectName(_fromUtf8("open_library"))
        self.open_directory = QtGui.QAction(File)
        self.open_directory.setObjectName(_fromUtf8("open_directory"))
        self.play_from_disc = QtGui.QAction(File)
        self.play_from_disc.setObjectName(_fromUtf8("play_from_disc"))
        self.equalizer = QtGui.QAction(File)
        self.equalizer.setObjectName(_fromUtf8("equalizer"))
        self.upvolume = QtGui.QAction(File)
        self.upvolume.setObjectName(_fromUtf8("upvolume"))
        self.downvolume = QtGui.QAction(File)
        self.downvolume.setObjectName(_fromUtf8("downvolume"))
        self.mute = QtGui.QAction(File)
        self.mute.setObjectName(_fromUtf8("mute"))
        self.add_tags = QtGui.QAction(File)
        self.add_tags.setObjectName(_fromUtf8("add_tags"))
        self.convert_files = QtGui.QAction(File)
        self.convert_files.setObjectName(_fromUtf8("convert_files"))
        self.create_playlist = QtGui.QAction(File)
        self.create_playlist.setObjectName(_fromUtf8("create_playlist"))
        self.menuFile.addAction(self.open_library)
        self.menuFile.addAction(self.open_directory)
        self.menuFile.addAction(self.play_from_disc)
        self.menuFile.addAction(self.add_tags)
        self.menuFile.addAction(self.convert_files)
        self.menuFile.addAction(self.create_playlist)
        self.menuSound.addAction(self.equalizer)
        self.menuSound.addAction(self.upvolume)
        self.menuSound.addAction(self.downvolume)
        self.menuSound.addAction(self.mute)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSound.menuAction())

        self.retranslateUi(File)
        QtCore.QMetaObject.connectSlotsByName(File)

    def retranslateUi(self, File):
        File.setWindowTitle(_translate("File", "MainWindow", None))
        self.Play.setText(_translate("File", "Play", None))
        self.Fastforward.setText(_translate("File", ">>", None))
        self.Fastbackward.setText(_translate("File", "<<", None))
        self.Shuffle.setText(_translate("File", "Shuffle", None))
        self.Stop.setText(_translate("File", "Stop", None))
        self.menuFile.setTitle(_translate("File", "Files", None))
        self.menuSound.setTitle(_translate("File", "Sound", None))
        self.open_library.setText(_translate("File", "Open file(s)", None))
        self.open_directory.setText(_translate("File", "Open directory", None))
        self.play_from_disc.setText(_translate("File", "Play from disc", None))
        self.equalizer.setText(_translate("File", "Equalizer", None))
        self.upvolume.setText(_translate("File", "Increase volume", None))
        self.downvolume.setText(_translate("File", "Decrease volume", None))
        self.mute.setText(_translate("File", "Mute", None))
        self.add_tags.setText(_translate("File", "Tags", None))
        self.convert_files.setText(_translate("File", "Convert file(s)", None))
        self.create_playlist.setText(_translate("File", "Create playlist", None))

