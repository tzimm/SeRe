# -*- coding: utf-8 *-*

from PySide import QtCore, QtGui
import SeRe_RenameBox
import math
import os

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
    def __init__(self, selected_files):
        """
        selected_files: to display in widget
        """
        super(_dialog_box, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.Accepted)
        self.buttonBox.rejected.connect(self.Rejected)
        self.pB_iterate.clicked.connect(self.Iterate)
        self.pB_preview.clicked.connect(self.RenamePreview)
        self.Renamer = ListRenamer(selected_files)
        self.filelist = selected_files
        #add selected Items to source list Widget
        self.lW_source.addItems(selected_files)
        self.RenamePreview()

    def Iterate(self):
        renamed_filelist=[]
        for idx in range(0, self.lW_result.count()):
            renamed_filelist.append(self.lW_result.item(idx).text())
            ##cur_item = self.GUI.list_browser.item(idx)
            ##all_filelist.append(cur_item.text())
        self.lW_source.clear()
        self.lW_result.clear()
        self.lW_source.addItems(renamed_filelist)

        self.Renamer.SetNewFilelist(renamed_filelist)

    def RenamePreview(self):
        Values = self.GetValues()
        # get renames for the selected items
        renamed_filelist = self.Renamer.Rename(Values)
        self.lW_result.clear()
        self.lW_result.addItems(renamed_filelist)

    def SetRemoveString(self, remove_string):
        self.txt_remove.setText(remove_string)

    def GetValues(self):
        Values = {}
        Values["enumerate"] = self.rb_addNmbrs.isChecked()
        Values["prepend_numbers"] = self.rb_nr_beginning.isChecked()
        Values["prepend_string"] = self.rb_txt_beginning.isChecked()
        Values["string"] = self.txt_custom.displayText()
        Values["remove_string"] = self.txt_remove.displayText()

        try:
            Values["start_number"] = int(self.txt_startnmbr.displayText())
        except ValueError:
            print("Error: Please enter a Number into NumberBox")
            super(_dialog_box, self).reject()
        return (Values)

    def Accepted(self):
        Values = self.GetValues()

        # get renames for the selected items
        renamed_filelist = self.Renamer.Rename(Values)
        # rename selected items
        for index in range(0, len(self.filelist)):
            src = self.currentpath + "/" + self.filelist[index]
            dst = self.currentpath + "/" + renamed_filelist[index]
            os.rename(src, dst)
        super(_dialog_box, self).accept()

    def Rejected(self):
        super(_dialog_box, self).reject()


class ListRenamer:
    """
    takes a list of filenames and renames them
    """
    def __init__(self, filelist):
        self.SetNewFilelist(filelist)

    def SetNewFilelist(self, filelist):
        self.filelist = filelist

    def Rename(self, Values):
        """
        filelist: list as displayed in browse including relative path
        startnmbr: nmbr to start enumerating
        enumerate_, e_front, string_, s_front: as returned by dialog box class

        result: additional list with the same order as filelist with rename
        recommendations
        """
        #round up, log to base 10
        nmbr_of_digits = int(math.log(len(self.filelist), 10) + 0.99)
        #startnumber to enumerate
        enumerate_nmbr = Values["start_number"]

        renamed_filelist = []
        for filename in self.filelist:
            filename = self._RemoveSubstrings(filename, Values["remove_string"])

            ending = filename[filename.rfind("."):]
            #beginning including the slas
            beginning = filename[:filename.rfind("/") + 1]

            raw_filename = filename[len(beginning):-len(ending)]

            rename_string = raw_filename
            if Values["string"] != "":
                if Values["prepend_string"]:
                    rename_string = Values["string"] + rename_string
                else:
                    rename_string += Values["string"]
            # enumerate is after string, because it shall be dominant
            if Values["enumerate"]:
                nmbr = str(enumerate_nmbr)
                add_zeros = nmbr_of_digits - len(nmbr)
                for y in range(add_zeros):
                    nmbr = "0" + nmbr
                if Values["prepend_numbers"]:
                    rename_string = str(nmbr) + rename_string
                else:
                    rename_string += str(nmbr)
                enumerate_nmbr += 1
            #append renamed to list
            renamed_filelist.append(beginning + rename_string + ending)

        if len(self.filelist) != len(renamed_filelist):
            print("filelist:" + str(self.filelist))
            print("renamed_filelist:" + str(renamed_filelist))
            raise Exception(
                "Rename Class: renamed list not as long as list")
        return renamed_filelist

    def _RemoveSubstrings(self, string_, substrings):
        """
        wrapper function for RemoveFrontBackSpaces and RemoveSubstring
        @param substrings: string as "substring1; substring2; substring3"
        @param string_: string that shall have its substrings removes
        """
        substringlist = substrings.split(";")
        for substring in substringlist:
            #print "Remove: \"" + substring + "\""
            substring_ = self._RemoveFrontBackSpaces(substring)
            string_ = self._RemoveSubstring(string_, substring_)

        return string_

    def _RemoveFrontBackSpaces(self, string_):
        """
        returns string_ without spaces at front and at the back
        """
        leftidx = 0
        rightidx = -1
        for i in range(len(string_)):
            if string_[i] != " ":
                leftidx = i
                break
        for i in range(1, len(string_) + 1):
            if string_[-i] != " ":
                rightidx = 1 + len(string_) - (i)
                break
        return string_[leftidx:rightidx]

    def _RemoveSubstring(self, string_, substring):
        """
        @param string_: string with substrings
        @param substring: string that shall be removed from substrings
        """
        #substring = substring.lower()  # case insensitive
        if substring == "<AllNumbers>":
            #print "benis"
            new_string = ""
            for letter in string_:
                try:
                    int(letter)
                except ValueError:
                    new_string = new_string + letter
            return new_string
        else:
            return string_.replace(substring, "")
