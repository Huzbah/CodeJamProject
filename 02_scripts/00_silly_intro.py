from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFrame
from PyQt6.QtGui import QPalette, QColor, QPixmap, QFont
import sys
import 01_search_term_select.py

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('123Loadboard')

        self.truck = QLabel()
        self.truck.setPixmap(QPixmap('../01_data/truck.svg'))
        self.drive = QPushButton('Start Drive')
        self.drive.clicked.connect(self.close)

        # self.drive.setGeometry(200, 200, 200, 200)
        # self.drive.setFont(QFont('Helvetica', 20))

        # self.drive.setStyleSheet('background-color : rgb(4,180,36);'
                    # "border-top-left-radius :35px;"
                    # "border-top-right-radius : 20px; "
                    # "border-bottom-left-radius : 50px; "
                    # "border-bottom-right-radius : 10px"
                    # "padding-top : 10px;"
                    # "padding-left:10px;"
                    # "padding-right:10;"
                    # "padding-bottom :10px;")

        layout = QVBoxLayout()
        layout.addWidget(self.truck)
        layout.addWidget(self.drive)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
