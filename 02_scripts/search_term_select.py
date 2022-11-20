from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        genres = {'Personal Finance':144, 'Locally Focused':151, 'Sports':77, 'Business':93, 'Health & Fitness':88, 'Arts':100, 'Music':134, 'Technology':127, 'Fiction':168, 'History':125, 'Kids & Family':132, 'News':99, 'Comedy':133, 'Society & Culture':122, 'Religion & Spirituality':69, 'Government':117, 'TV & Film':68, 'Leisure':82, 'Education':111, 'Science':107, 'True Crime':135}
        genres = dict(sorted(genres.items()))

        self.setWindowTitle('Podcast Mode')

        label1 = QLabel('Select your first genre preference:')
        self.genre1 = QComboBox()
        self.genre1.addItem('Select First Genre')
        self.genre1.addItems(genres.keys())
        self.genre1.activated.connect(self.check_index)


        label2 = QLabel('Select your second genre preference:')
        self.genre2 = QComboBox()
        self.genre2.addItem('Select Second Genre')
        self.genre2.addItems(genres.keys())
        self.genre2.activated.connect(self.check_index)

        label3 = QLabel('Select your third genre preference:')
        self.genre3 = QComboBox()
        self.genre3.addItem('Select Third Genre')
        self.genre3.addItems(genres.keys())
        self.genre3.activated.connect(self.check_index)

        self.confirm = QPushButton()
        self.confirm.setText('Confirm Selection')
        self.confirm.setEnabled(False)
        self.confirm.clicked.connect(self.make_file)
        self.confirm.clicked.connect(self.close)

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

    def check_index(self):
        cindex1 = self.genre1.currentIndex()
        cindex2 = self.genre2.currentIndex()
        cindex3 = self.genre3.currentIndex()
        indices = [cindex1, cindex2, cindex3]

        if indices[0]>0 and indices[1] >0 and indices[2]>0:
            self.confirm.setEnabled(True)
        else:
             self.confirm.setEnabled(False)

    def make_file(self):
        genre_selection = self.genre1.currentText(), self.genre2.currentText(), self.genre3.currentText()
        with open('./01_data/examplefile.txt', 'w') as f:
            f.write(str(genre_selection))

def run_search_select():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
