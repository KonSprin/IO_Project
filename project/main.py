from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import QCoreApplication
import sys
import os
import platform

from GUICode import Ui_IO

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_IO()
        self.ui.setupUi(self)

        # SHOW YOURSELF
        self.show()

        # SETTINGS / CONNECTIONS
        self.ui.btnChooseVideo.clicked.connect(self.chooseVideo)      

        self.ui.btnChooseVideo_2.clicked.connect(self.chooseSaveFile)  
        
        self.ui.BtnStartprocess.clicked.connect(self.detect)

            

    def chooseVideo(self):
        starting_directory = ''
        if platform.system() == "Windows":
            starting_directory = 'USERPROFILE'
        else:
            starting_directory = 'HOME'

        fname = QFileDialog.getOpenFileName(self, 'Choose Video', os.path.join(os.environ[starting_directory], 'Videos'), "Video Files (*.mp4 *.mkv *.avi)")

        # SET lineEdit TO CHOSEN PATH
        self.ui.videoPath.setText(fname[0])

    def chooseSaveFile(self):
        starting_directory = ''
        if platform.system() == "Windows":
            starting_directory = 'USERPROFILE'
        else:
            starting_directory = 'HOME'

        fname = QFileDialog.getOpenFileName(self, 'Choose Log File', os.environ[starting_directory])

        # SET lineEdit TO CHOSEN PATH
        self.ui.videoPath.setText(fname[0])

    def detect(self):
        fname = self.ui.videoPath.text()
        print("Started processing {}!".format(fname))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())