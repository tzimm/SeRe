# -*- coding: utf-8 *-*

from PySide import QtCore, QtGui
import SeRe_RenameBox

#class _file():#
#
#    def __init__(self):
#        #super(_file, self).__init__()
#        self.name = ""
#        self.fullpath = ""
#
#    def GetName(self):
#        return self.name
#
#    def GetFullpath(self):
#        return self.fullpath


class _dialog_box(QtGui.QDialog, SeRe_RenameBox.Ui_Dialog):
    """
    return format: [enumerate_, e_front, string_, s_front]
        enumerate_: bool 1 - enumerate, 0 - don't enumerate
        e_front: bool 1 - add to front, 0 add to back
        string_: string
        s_front: bool 1- add to front, 0 add to back
    """
    def __init__(self, parent=None):
        super(_dialog_box, self).__init__()
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.Accepted)
        self.buttonBox.rejected.connect(self.Rejected)

    def getValues(self):
        enumerate_ = self.rb_addNmbrs.isChecked()
        e_front = self.rb_nr_beginning.isChecked()
        string_ = self.txt_custom.displayText()
        s_front = self.rb_txt_beginning.isChecked()
        print str(enumerate_)
        print str(e_front)
        print str(s_front)
        print string_
        return (enumerate_, e_front, string_, s_front)

    def Accepted(self):
        super(_dialog_box, self).accept()

    def Rejected(self):
        super(_dialog_box, self).reject()
