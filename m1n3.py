#! python3
import pyautogui, sys
import time

from PyQt5.QtCore import QCoreApplication, Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QStyleFactory
from PyQt5.QtWidgets import QAction, QMessageBox, QCheckBox, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QFileDialog


import keyboard

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,400,200)
        self.setWindowTitle('M1N3')
        self.locs = []
        
        self.adding_points = False
        self.should_m1n3 = False
        self.m1n1ng = False
        self.loop_index = 0

        self.m1n3_timer = QTimer()
        self.m1n3_timer.timeout.connect(self.m1n3)

        self.standby_timer = QTimer()
        self.standby_timer.timeout.connect(self.standby)
        self.standby_timer.start(1000)

        keyboard.add_hotkey('ctrl+s', self.add_point)
        keyboard.add_hotkey('ctrl+t', self.toggle_add)
        keyboard.add_hotkey('ctrl+p', self.print_points)
        keyboard.add_hotkey('ctrl+m', self.toggle_should_m1n3)
        self.show()


    def toggle_add(self):
        if not self.m1n1ng:
            if not self.adding_points:
                self.locs = []
                self.loop_index = 0
            self.adding_points = not self.adding_points
            print('Adding Points is now: ', self.adding_points)

    
    def add_point(self):
        if self.adding_points and not self.m1n1ng:
            x, y = pyautogui.position()
            self.locs.append((x,y))
            print(' -- point added: ', (x,y))

    def standby(self):
        if (self.should_m1n3 != self.m1n1ng):
            self.toggle_m1n3()

    def m1n3(self):
        old = pyautogui.position()
        pyautogui.moveTo(self.locs[self.loop_index])
        pyautogui.click()
        pyautogui.moveTo(old)
        self.loop_index = (self.loop_index + 1) % len(self.locs)

    def print_points(self):
        print(self.locs)

    def toggle_should_m1n3(self):
        self.should_m1n3 = not self.should_m1n3

    def toggle_m1n3(self):
        if not self.m1n1ng:
            self.m1n1ng = True
            self.m1n3_timer.start(5000)
        else:
            self.m1n1ng = False
            self.m1n3_timer.stop()


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()