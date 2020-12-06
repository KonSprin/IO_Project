from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import QCoreApplication
import sys
import os
import platform
import ctypes
import csv
import ast

from GUICode import Ui_IO
from video_processing import process

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

        self.ui.btnSaveLogs.clicked.connect(self.save_logs)
            

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

        # fname = QFileDialog.getOpenFileName(self, 'Choose Log File', os.environ[starting_directory])
        fname = QFileDialog.getExistingDirectory(self, 'Choose Log File', os.environ[starting_directory])
        # SET lineEdit TO CHOSEN PATH
        self.ui.lineEdit_2.setText(fname)

    def detect(self):
        fname = self.ui.videoPath.text()
        log_dir = self.ui.lineEdit_2.text()
        log_window = self.ui.plainTextEdit
        if os.path.isdir(log_dir) and os.path.isfile(fname):
            process(self.ui.progressBar, fname, log_dir, log_window)
        elif os.path.isdir(log_dir):
            ctypes.windll.user32.MessageBoxW(0, "Niepoprawna ścieżka do nagrania", "Error", 1)
        elif os.path.isfile(fname):
            ctypes.windll.user32.MessageBoxW(0, "Wybierz istniejący folder na logi", "Error", 1)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Wybierz istniejący folder na logi oraz poprawną ścieżkę do nagrania", "Error", 1)

    def save_logs(self):
        logger = self.ui.plainTextEdit.toPlainText()
        INPUT_DIR = self.ui.videoPath.text()
        LOG_DIR = self.ui.lineEdit_2.text() + "/" +INPUT_DIR.split('/')[-1].split('.')[0] + '.csv'
        logger = ast.literal_eval(logger)
        with open(LOG_DIR, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',',
                                quotechar='`', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['id', 'class', 'x_pos', 'y_pos', 'first appearance [s]'])
            for car in logger:
                writer.writerow(car)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())