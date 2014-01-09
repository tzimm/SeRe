# -*- coding: utf-8 *-*


from PySide import QtCore, QtGui
import SeRe_GUI
import sys
import os
import SeRe_HelperClasses


class _scan_gui():

    def __init__(self, qtgui_mainwindow):
        self.DEBUG = 0
        self.GUI = SeRe_GUI.Ui_MainWindow()
        self.GUI.setupUi(qtgui_mainwindow)
        self.currentpath = ""  # current path without the finishing slash
        self.GUI.pb_browse.clicked.connect(self.BrowseClicked)
        self.GUI.pb_rename.clicked.connect(self.RenameClicked)
        self.GUI.le_search.textChanged.connect(self.ManSearch)
        self.GUI.le_exclude.textChanged.connect(self.ManSearch)
        self.InitializeBrowser()
        self.GUI.list_browser.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    def InitializeBrowser(self):
        self.skriptpath = self.GetSkriptpath()
        self.DisplayDirectory(self.skriptpath)

    def ManSearch(self):
        """
        manual search
        """
        search = self.GUI.le_search.displayText()
        exclude = self.GUI.le_exclude.displayText()

        self.GUI.list_browser.clear()
        fileslist = self.GetAllFiles()
        matching = []
        if exclude != "":
            for i in fileslist:
                if (i.lower().find(search.lower()) != -1) and (i.lower().find(exclude.lower()) == -1):
                    matching.append(i)
        else:
            for i in fileslist:
                if (i.lower().find(search.lower()) != -1):

                        matching.append(i)

        self.GUI.list_browser.addItems(matching)

    def DisplayDirectory(self, path):
        self.GUI.list_browser.clear()  # clear browser
        self.GUI.lbl_curpath.setText(path)  # set current path label
        self.currentpath = path
        fileslist = self.GetAllFiles()  # get files from path
        self.GUI.list_browser.addItems(fileslist)

    def GetAllFiles(self):
        if self.GUI.cb_deepsearch.isChecked():
            fileslist = self.ReturnFirstLevel(self.currentpath, "deepfiles")
        else:
            fileslist = self.ReturnFirstLevel(self.currentpath, "files")
        fileslist.sort(key=lambda x: self.SortFilename(x))
        return fileslist

    def SortFilename(self, filename):
        filename = filename.lower()
        return filename[:filename.find(".")]

    def BrowseClicked(self):
        FolderDialog = QtGui.QFileDialog()
        FolderDialog.setFileMode(QtGui.QFileDialog.Directory)
        FolderDialog.setDirectory(self.skriptpath)
        foldername = FolderDialog.getExistingDirectory(caption = "Please select a directory")
        self.DisplayDirectory(foldername)

    def ReturnFirstLevel(self, mainpath, mode="files"):
        """
        easier interface for the os.walk functionality; only used for first file hierarchy
        returns files or folders within first folder hierarchy without path
        @params mainpath: path to search
        @params mode: either "files" or "folders" to specify what to return;
                    "deepfiles" returns all subfiles in the folder hierarchy
        @return list of all files or folders within the path; ONLY NAMES NOT THE FULL PATH
        """
        if mode == "files":
            walkgenerator = os.walk(mainpath)
            #extract lists from generator
            for dirpath, dirnames, filenames in walkgenerator:
                break
            return filenames
        elif mode == "folders":
            dirs = []
            for dirname, dirnames, filenames in os.walk(mainpath):
                dirs.append(dirname)
            del dirs[0]
            return dirs
        elif mode == "deepfiles":
            walkgenerator = os.walk(mainpath)
            files = []
            pathes = []
            for dirpath, dirnames, filenames in walkgenerator:
                for i in filenames:
                    files.append(dirpath[len(mainpath):] + "/" + i)
            return files

    def GetPath(self, mainpath, searchname):
        """
        deprecated

        thought to be used with the list widget to be able to still use all
        the built-in search functions
        search for a filename using os.walk and return the full path
        """
        walkgenerator = os.walk(mainpath)
        for dirpath, dirnames, filenames in walkgenerator:
            try:
                idx = filenames.index(searchname)
                return dirpath + "/" + filenames[idx]
            except ValueError:
                continue
        return -1

    def RenameClicked(self):
        #Box = SeRe_HelperClasses._dialog_box()
        dialog = SeRe_HelperClasses._dialog_box(self)
        if dialog.exec_():
            (enumerate_, e_front, string_, s_front) = dialog.getValues()

            filelist = []
            # Get selected items
            for idx in range(0, self.GUI.list_browser.count()):
                cur_item = self.GUI.list_browser.item(idx)
                # only rename selected items
                if cur_item.isSelected():
                #self.GUI.list_browser.isItemSelected(cur_item):
                    filelist.append(cur_item.text())
            # get renames for the selected items
            renamed_filelist = self.RenameFilelist(filelist, 1, enumerate_, e_front, string_, s_front)
            if len(filelist) != len(renamed_filelist):
                raise Exception("You did wrong ;_;")
            # rename selected items
            for index in range(0, len(filelist)):
                scr = self.currentpath+ "/" + filelist[index]
                dst = self.currentpath + "/" + renamed_filelist[index]
                os.rename(src, dst)

    def RenameFilelist(self, filelist, startnmbr, enumerate_, e_front, string_, s_front):
        """
        filelist: list as displayed in browse including relative path
        startnmbr: nmbr to start enumerating
        enumerate_, e_front, string_, s_front: as returned by dialog box class

        result: additional list with the same order as filelist with rename
        recommendations
        """
        enumerate_nmbr = startnmbr
        renamed_filelist = []
        for filename in filelist:
            ending = filename[filename.rfind("."):]
            #beginning including the slas
            beginning = filename[:filename.rfind("/") + 1]

            raw_filename = filename[len(beginning):-len(ending)]

            rename_string = raw_filename
            if string_ != "":
                if s_front:
                    rename_string = string_ + rename_string
                else:
                    rename_string += string
            # enumerate is after string, because it shall be dominant
            if enumerate_:
                if e_front:
                    rename_string = str(enumerate_nmbr) + rename_string
                else:
                    renambe_string += str(enumerate_nmbr)
                enumerate_nmbr += 1
            #append renamed to list
            renamed_filelist.append(beginning + rename_string + ending)
        return renamed_filelist

    def GetSkriptpath(self):
        skriptpath = os.path.realpath(__file__)
        return skriptpath[:skriptpath.rfind("/")]


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
scan_gui = _scan_gui(window)
window.show()
sys.exit(app.exec_())

