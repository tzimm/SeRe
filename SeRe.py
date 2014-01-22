# -*- coding: utf-8 *-*
from PySide import QtCore, QtGui
import SeRe_GUI
import sys
import os
import SeRe_HelperClasses

class _scan_gui():

    def __init__(self, qtgui_mainwindow):
        self.GUI = SeRe_GUI.Ui_MainWindow()
        self.GUI.setupUi(qtgui_mainwindow)
        self.GUI.pb_browse.clicked.connect(self.BrowseClicked)
        self.GUI.pb_rename.clicked.connect(self.RenameClicked)
        self.GUI.le_search.textChanged.connect(self.RefreshDisplay)
        self.GUI.le_exclude.textChanged.connect(self.RefreshDisplay)
        self.GUI.cb_deepsearch.stateChanged.connect(self.RefreshDisplay)
        self.GUI.list_browser.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.InitializeBrowser()

    def InitializeBrowser(self):
        """
        could as well directly be located in __init__
        not GUI specific methods are called here
        """
        self.skriptpath = self.GetSkriptpath()
        self.currentpath = self.skriptpath  # default path is skriptpath
        self.DisplayDirectory(self.skriptpath)

    def RefreshDisplay(self):
        """
        1. search for files in self.skriptpath
        2. filter files for the ones that fit to the searchstrings
        3. display those files in file browser
        """
        search = self.GUI.le_search.displayText()
        exclude = self.GUI.le_exclude.displayText()

        self.GUI.list_browser.clear()
        fileslist = self.GetAllFiles()
        matching = []
        if exclude != "":
            for i in fileslist:
                if (i.lower().find(search.lower()) != -1) and (
                    i.lower().find(exclude.lower()) == -1):
                    matching.append(i)
        else:
            for i in fileslist:
                if (i.lower().find(search.lower()) != -1):

                        matching.append(i)

        self.GUI.list_browser.addItems(matching)

    def DisplayDirectory(self, path):
        """
        display items from directory @path in the file browser
        """
        self.GUI.list_browser.clear()  # clear browser
        self.GUI.lbl_curpath.setText(path)  # set current path label
        self.currentpath = path
        #fileslist = self.GetAllFiles()  # get files from path
        #self.GUI.list_browser.addItems(fileslist)
        self.RefreshDisplay()  # overwrite the found items with the search

    def GetAllFiles(self):
        """
        uses os.walk to scan file hierarchy trees
        and returns a list of the found files
        """
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
            for dirpath, dirnames, filenames in walkgenerator:
                for i in filenames:
                    files.append(dirpath[len(mainpath):] + "/" + i)
            return files

    def RenameClicked(self):
        # Get selected items
        selected_filelist = []
        all_filelist = []

        for idx in range(0, self.GUI.list_browser.count()):
            cur_item = self.GUI.list_browser.item(idx)
            all_filelist.append(cur_item.text())
            # only rename selected items
            if cur_item.isSelected():
                selected_filelist.append(cur_item.text())
        #if nothing in particular is selected we assume that everything is meant
        if len(selected_filelist) == 0:
            dialog = SeRe_HelperClasses._dialog_box(all_filelist)
        else:
            dialog = SeRe_HelperClasses._dialog_box(selected_filelist)
        dialog.SetRemoveString(
            "<allNumbers>; " + self.GUI.le_search.displayText())
        dialog.exec_()

    def GetSkriptpath(self):
        skriptpath = os.path.realpath(__file__)
        return skriptpath[:skriptpath.rfind("/")]


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
scan_gui = _scan_gui(window)
window.show()
sys.exit(app.exec_())

