from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import QCoreApplication
import sys
import os
import platform
import ctypes
import csv
import ast
import cv2

from GUICode import Ui_IO
from video_processing import process


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_IO()
        self.ui.setupUi(self)
        self.ui.videoPath.setText(str(os.path.dirname(os.path.abspath(__file__))))
        # SHOW YOURSELF
        self.show()

        # SETTINGS / CONNECTIONS
        self.ui.btnChooseVideo.clicked.connect(self.chooseVideo)

        self.ui.btnChooseVideo_2.clicked.connect(self.chooseSaveFile)

        self.ui.BtnStartprocess.clicked.connect(self.detect)

        self.ui.btnSaveLogs.clicked.connect(self.save_logs)

        self.ui.btnPlayVideo.clicked.connect(self.play)

    # Set video path
    def chooseVideo(self):
        starting_directory = ''
        if platform.system() == "Windows":
            starting_directory = 'USERPROFILE'
        else:
            starting_directory = 'HOME'

        fname = QFileDialog.getOpenFileName(self, 'Choose Video', str(os.path.dirname(os.path.abspath(__file__))),
                                            "Video Files (*.mp4 *.mkv *.avi)")
        # SET lineEdit TO CHOSEN PATH
        self.ui.videoPath.setText(fname[0])

    # Set logs path
    def chooseSaveFile(self):
        starting_directory = ''
        if platform.system() == "Windows":
            starting_directory = 'USERPROFILE'
        else:
            starting_directory = 'HOME'

        # fname = QFileDialog.getOpenFileName(self, 'Choose Log File', os.environ[starting_directory])
        fname = QFileDialog.getExistingDirectory(self, 'Choose Log File',
                                                 str(os.path.dirname(os.path.abspath(__file__))))
        # SET lineEdit TO CHOSEN PATH
        self.ui.lineEdit_2.setText(fname)

    # Analyze video
    def detect(self):
        # Get paths
        fname = self.ui.videoPath.text()
        log_dir = self.ui.lineEdit_2.text()
        log_window = self.ui.plainTextEdit
        # Check if paths are correct
        if os.path.isdir(log_dir) and os.path.isfile(fname):
            process(self.ui.progressBar, fname, log_dir, log_window)
        elif os.path.isdir(log_dir):
            ctypes.windll.user32.MessageBoxW(0, "Niepoprawna ścieżka do nagrania", "Error", 1)
        elif os.path.isfile(fname):
            ctypes.windll.user32.MessageBoxW(0, "Wybierz istniejący folder na logi", "Error", 1)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Wybierz istniejący folder na logi oraz poprawną ścieżkę do nagrania",
                                             "Error", 1)

    # Save logs
    def save_logs(self):
        # Get logs path and logs as a plain text
        logger = self.ui.plainTextEdit.toPlainText()
        INPUT_DIR = self.ui.videoPath.text()
        LOG_DIR = self.ui.lineEdit_2.text() + "/" + INPUT_DIR.split('/')[-1].split('.')[0] + '.csv'
        # Convert logs into a list and save
        logger = ast.literal_eval(logger)
        with open(LOG_DIR, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',',
                                quotechar='`', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['id', 'class', 'x_pos', 'y_pos', 'first appearance [s]'])
            for car in logger:
                writer.writerow(car)

    # Play processed video
    def play(self):
        # Get output path based on original video path
        input_file = self.ui.videoPath.text()
        output_file = input_file.split('.')[0] + '_output.' + input_file.split('.')[1]
        cap = cv2.VideoCapture(output_file)
        output_file = output_file.split("/")[-1]
        # Play until video ends
        while (cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, None, None, fx=0.5, fy=0.5)
            cv2.imshow(output_file, frame)
            key = cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

            if key in [27, 1048603]:  # ESC key to abort, close window
                cv2.destroyAllWindows()
                break

        cap.release()
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())