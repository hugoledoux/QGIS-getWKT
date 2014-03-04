# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_getwkt.ui'
#
# Created: Tue Mar  4 12:16:42 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_GetWKT(object):
    def setupUi(self, GetWKT):
        GetWKT.setObjectName(_fromUtf8("GetWKT"))
        GetWKT.resize(521, 358)
        self.widget = QtGui.QWidget(GetWKT)
        self.widget.setGeometry(QtCore.QRect(15, 12, 491, 331))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wktTextEdit = QtGui.QTextEdit(self.widget)
        self.wktTextEdit.setReadOnly(True)
        self.wktTextEdit.setObjectName(_fromUtf8("wktTextEdit"))
        self.verticalLayout.addWidget(self.wktTextEdit)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(GetWKT)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), GetWKT.accept)
        QtCore.QMetaObject.connectSlotsByName(GetWKT)

    def retranslateUi(self, GetWKT):
        GetWKT.setWindowTitle(_translate("GetWKT", "GetWKT", None))
        self.pushButton.setText(_translate("GetWKT", "OK", None))

