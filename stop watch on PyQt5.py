#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget,      QApplication,
                             QLCDNumber,   QPushButton,
                             QGridLayout,  QTableWidget,
                             QVBoxLayout,  QMenu,
                             QMenuBar,     QGroupBox,
                             QTableWidgetItem)
from PyQt5.QtCore import QTime, QTimer


class stopwatch(QWidget):
    def __init__(self):
        super(stopwatch, self).__init__()
        self.createMenu()
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        self.int_button = QPushButton("Int", self)
        self.setGeometry(200, 200, 450, 220)
        self.setWindowTitle("StopWatch")
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.setRowCount(100)
        
        
        self.LCD = QLCDNumber(self)
        self.gridGroupBox = QGroupBox()
        self.grid = QGridLayout()
        
        self.grid.addWidget(self.LCD, 0, 0, 1, 3)
        self.grid.addWidget(self.table, 0, 3, 0, 3)
        self.grid.setRowMinimumHeight(0, 200)
        self.grid.addWidget(self.start_button, 1, 0)
        self.grid.addWidget(self.int_button, 1, 1)
        self.grid.addWidget(self.reset_button, 1, 2)
        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        
        
        self.gridGroupBox.setLayout(self.grid)
        mainLayout.addWidget(self.gridGroupBox)
        
        
        self.setLayout(mainLayout)
        
        self.LCD.setDigitCount(12)
        self.time = 0
        self.ms = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.rezults = 0
        self.LCD.display("00:00:00:00")
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.display)
        self.start_button.clicked.connect(self.start)
        self.reset_button.clicked.connect(self.reset)
        self.int_button.clicked.connect(self.int_)
        
    def createMenu(self):
        self.menuBar = QMenuBar()

        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)    
    def start(self):
        self.timer.start()
        self.start_button.setText("Pause")
        self.start_button.clicked.disconnect()
        self.start_button.clicked.connect(self.stop)
        
    
    def stop(self):
        self.timer.stop()
        self.start_button.setText("Start")
        self.start_button.clicked.disconnect()
        self.start_button.clicked.connect(self.start)
        

    def int_(self):
        item = ("%02d:%02d:%02d:%02d" % (self.hour, self.min, self.sec, self.ms))
        self.table.setItem(0, self.rezults, QTableWidgetItem(item))
        self.rezults += 1
        

    def reset(self):
        self.timer.stop()
        self.time = 0
        self.ms = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.rezults = 0
        self.table.clearContents()
        self.stop()
        self.display()
        
        
    def display(self):
              
        self.LCD.display("%02d:%02d:%02d:%02d" % (self.hour, self.min, self.sec, self.ms))
        if self.ms != 99:
            self.ms += 1
        else:
            self.ms = 0
            if self.sec != 59:
                self.sec += 1
            else:
                self.sec = 0
                if self.min != 59:
                    self.min +=1
                else:
                    self.min = 0
                    if self.hour != 23:
                        self.hour += 1
                    else:
                        self.hour = 0
          
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    stop_watch = stopwatch()
    stop_watch.show()

    sys.exit(app.exec_())
