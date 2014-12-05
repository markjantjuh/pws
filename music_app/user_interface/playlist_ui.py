# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist.ui'
#
# Created: Fri Dec 05 12:30:32 2014
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

class Ui_playlist_dialog(object):
    def setupUi(self, playlist_dialog):
        playlist_dialog.setObjectName(_fromUtf8("playlist_dialog"))
        playlist_dialog.resize(294, 84)
        self.textbox_name = QtGui.QLineEdit(playlist_dialog)
        self.textbox_name.setGeometry(QtCore.QRect(70, 20, 204, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        self.textbox_name.setFont(font)
        self.textbox_name.setObjectName(_fromUtf8("textbox_name"))
        self.label_playlist = QtGui.QLabel(playlist_dialog)
        self.label_playlist.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label_playlist.setFont(font)
        self.label_playlist.setObjectName(_fromUtf8("label_playlist"))
        self.button_create = QtGui.QPushButton(playlist_dialog)
        self.button_create.setGeometry(QtCore.QRect(110, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        self.button_create.setFont(font)
        self.button_create.setObjectName(_fromUtf8("button_create"))
        self.button_cancel = QtGui.QPushButton(playlist_dialog)
        self.button_cancel.setGeometry(QtCore.QRect(200, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        self.button_cancel.setFont(font)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))

        self.retranslateUi(playlist_dialog)
        QtCore.QMetaObject.connectSlotsByName(playlist_dialog)

    def retranslateUi(self, playlist_dialog):
        playlist_dialog.setWindowTitle(_translate("playlist_dialog", "Create playlist", None))
        self.label_playlist.setText(_translate("playlist_dialog", "Name:", None))
        self.button_create.setText(_translate("playlist_dialog", "Create", None))
        self.button_cancel.setText(_translate("playlist_dialog", "Cancel", None))

