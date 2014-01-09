# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeRe_RenameBox.ui'
#
# Created: Thu Jan  9 15:56:17 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(227, 226)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_addNmbrs = QtGui.QCheckBox(Dialog)
        self.rb_addNmbrs.setChecked(True)
        self.rb_addNmbrs.setObjectName("rb_addNmbrs")
        self.verticalLayout.addWidget(self.rb_addNmbrs)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.rb_nr_beginning = QtGui.QRadioButton(self.groupBox)
        self.rb_nr_beginning.setGeometry(QtCore.QRect(0, 20, 105, 21))
        self.rb_nr_beginning.setChecked(True)
        self.rb_nr_beginning.setObjectName("rb_nr_beginning")
        self.rb_nr_ending = QtGui.QRadioButton(self.groupBox)
        self.rb_nr_ending.setGeometry(QtCore.QRect(120, 20, 105, 21))
        self.rb_nr_ending.setObjectName("rb_nr_ending")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.txt_custom = QtGui.QLineEdit(self.groupBox_2)
        self.txt_custom.setGeometry(QtCore.QRect(10, 20, 129, 25))
        self.txt_custom.setObjectName("txt_custom")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.rb_txt_beginning = QtGui.QRadioButton(self.groupBox_3)
        self.rb_txt_beginning.setGeometry(QtCore.QRect(0, 20, 105, 21))
        self.rb_txt_beginning.setChecked(True)
        self.rb_txt_beginning.setObjectName("rb_txt_beginning")
        self.rb_txt_ending = QtGui.QRadioButton(self.groupBox_3)
        self.rb_txt_ending.setGeometry(QtCore.QRect(120, 20, 105, 21))
        self.rb_txt_ending.setObjectName("rb_txt_ending")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_addNmbrs.setText(QtGui.QApplication.translate("Dialog", "Add Nmbrs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "add to:", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_nr_beginning.setText(QtGui.QApplication.translate("Dialog", "beginning", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_nr_ending.setText(QtGui.QApplication.translate("Dialog", "ending", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "add custom txt:", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_custom.setText(QtGui.QApplication.translate("Dialog", "_", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "add to:", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_txt_beginning.setText(QtGui.QApplication.translate("Dialog", "beginning", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_txt_ending.setText(QtGui.QApplication.translate("Dialog", "ending", None, QtGui.QApplication.UnicodeUTF8))

