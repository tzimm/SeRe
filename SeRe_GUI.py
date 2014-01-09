# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeRe.ui'
#
# Created: Thu Jan  9 15:56:20 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 664)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_search = QtGui.QLineEdit(self.groupBox)
        self.le_search.setObjectName("le_search")
        self.verticalLayout.addWidget(self.le_search)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_exclude = QtGui.QLineEdit(self.groupBox_2)
        self.le_exclude.setObjectName("le_exclude")
        self.verticalLayout_2.addWidget(self.le_exclude)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.lbl_curpath = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_curpath.sizePolicy().hasHeightForWidth())
        self.lbl_curpath.setSizePolicy(sizePolicy)
        self.lbl_curpath.setObjectName("lbl_curpath")
        self.verticalLayout_3.addWidget(self.lbl_curpath)
        self.list_browser = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_browser.sizePolicy().hasHeightForWidth())
        self.list_browser.setSizePolicy(sizePolicy)
        self.list_browser.setObjectName("list_browser")
        self.verticalLayout_3.addWidget(self.list_browser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_browse = QtGui.QPushButton(self.centralwidget)
        self.pb_browse.setObjectName("pb_browse")
        self.horizontalLayout.addWidget(self.pb_browse)
        self.cb_deepsearch = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_deepsearch.sizePolicy().hasHeightForWidth())
        self.cb_deepsearch.setSizePolicy(sizePolicy)
        self.cb_deepsearch.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.cb_deepsearch.setObjectName("cb_deepsearch")
        self.horizontalLayout.addWidget(self.cb_deepsearch)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pb_rename = QtGui.QPushButton(self.centralwidget)
        self.pb_rename.setObjectName("pb_rename")
        self.verticalLayout_3.addWidget(self.pb_rename)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SeRe", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "search for:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "exclude in search:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_curpath.setText(QtGui.QApplication.translate("MainWindow", "curpath", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_browse.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_deepsearch.setText(QtGui.QApplication.translate("MainWindow", "Deep Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_rename.setText(QtGui.QApplication.translate("MainWindow", "rename selection", None, QtGui.QApplication.UnicodeUTF8))

