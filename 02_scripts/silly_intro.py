from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('123Loadboard')

        self.truck = QLabel()
        self.truck.setPixmap(QPixmap('./01_data/truck.svg'))
        self.drive = QPushButton('Start Drive')
        self.drive.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.truck)
        layout.addWidget(self.drive)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

def start_drive():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

start_drive()