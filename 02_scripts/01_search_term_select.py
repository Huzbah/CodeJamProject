from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

genres = ['Personal Finance', 'Locally Focused', 'Sports', 'Business', 'Health & Fitness', 'Arts', 'Music', 'Technology', 'Fiction', 'History', 'Kids & Family', 'News', 'Comedy', 'Society & Culture', 'Religion & Spirituality', 'Government', 'TV & Film', 'Leisure', 'Education', 'Science', 'True Crime']
genres.sort()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Podcast Mode')

        label1 = QLabel('Select your first genre preference:')
        self.genre1 = QComboBox()
        self.genre1.addItem('Select First Genre')
        self.genre1.addItems(genres)
        self.genre1.activated.connect(self.check_index)


        label2 = QLabel('Select your second genre preference:')
        self.genre2 = QComboBox()
        self.genre2.addItem('Select Second Genre')
        self.genre2.addItems(genres)
        self.genre2.activated.connect(self.check_index)

        label3 = QLabel('Select your third genre preference:')
        self.genre3 = QComboBox()
        self.genre3.addItem('Select Third Genre')
        self.genre3.addItems(genres)
        self.genre3.activated.connect(self.check_index)

        self.confirm = QPushButton()
        self.confirm.setText('Confirm Selection')
        self.confirm.setEnabled(False)
        self.confirm.clicked.connect(self.close)
        self.confirm

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.genre1)
        layout.addWidget(label2)
        layout.addWidget(self.genre2)
        layout.addWidget(label3)
        layout.addWidget(self.genre3)
        layout.addWidget(self.confirm)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def check_index(self, index):
        cindex1 = self.genre1.currentIndex()
        cindex2 = self.genre2.currentIndex()
        cindex3 = self.genre3.currentIndex()
        indices = cindex1, cindex2, cindex3

        if indices[0]>0 and indices[1] >0 and indices[2]>0:
            self.confirm.setEnabled(True)
        else:
             self.confirm.setEnabled(False)

        return indices

    # def allow_confirm(self, index):

        


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())