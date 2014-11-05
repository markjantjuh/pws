# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat Nov 01 17:43:38 2014
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
        self.actionOpen_file = QtGui.QAction(File)
        self.actionOpen_file.setObjectName(_fromUtf8("actionOpen_file"))
        self.actionOpen_directory = QtGui.QAction(File)
        self.actionOpen_directory.setObjectName(_fromUtf8("actionOpen_directory"))
        self.actionPlay_from_disc = QtGui.QAction(File)
        self.actionPlay_from_disc.setObjectName(_fromUtf8("actionPlay_from_disc"))
        self.actionEqualizer = QtGui.QAction(File)
        self.actionEqualizer.setObjectName(_fromUtf8("actionEqualizer"))
        self.actionIncrease_volume = QtGui.QAction(File)
        self.actionIncrease_volume.setObjectName(_fromUtf8("actionIncrease_volume"))
        self.actionDecrease_volume = QtGui.QAction(File)
        self.actionDecrease_volume.setObjectName(_fromUtf8("actionDecrease_volume"))
        self.actionMute = QtGui.QAction(File)
        self.actionMute.setObjectName(_fromUtf8("actionMute"))
        self.actionAdd_tags = QtGui.QAction(File)
        self.actionAdd_tags.setObjectName(_fromUtf8("actionAdd_tags"))
        self.actionConvert_file_s = QtGui.QAction(File)
        self.actionConvert_file_s.setObjectName(_fromUtf8("actionConvert_file_s"))
        self.actionCreate_playlist = QtGui.QAction(File)
        self.actionCreate_playlist.setObjectName(_fromUtf8("actionCreate_playlist"))
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionOpen_directory)
        self.menuFile.addAction(self.actionPlay_from_disc)
        self.menuFile.addAction(self.actionAdd_tags)
        self.menuFile.addAction(self.actionConvert_file_s)
        self.menuFile.addAction(self.actionCreate_playlist)
        self.menuSound.addAction(self.actionEqualizer)
        self.menuSound.addAction(self.actionIncrease_volume)
        self.menuSound.addAction(self.actionDecrease_volume)
        self.menuSound.addAction(self.actionMute)
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
        self.actionOpen_file.setText(_translate("File", "Open file(s)", None))
        self.actionOpen_directory.setText(_translate("File", "Open directory", None))
        self.actionPlay_from_disc.setText(_translate("File", "Play from disc", None))
        self.actionEqualizer.setText(_translate("File", "Equalizer", None))
        self.actionIncrease_volume.setText(_translate("File", "Increase volume", None))
        self.actionDecrease_volume.setText(_translate("File", "Decrease volume", None))
        self.actionMute.setText(_translate("File", "Mute", None))
        self.actionAdd_tags.setText(_translate("File", "Edit metadata", None))
        self.actionConvert_file_s.setText(_translate("File", "Convert file(s)", None))
        self.actionCreate_playlist.setText(_translate("File", "Create playlist", None))

