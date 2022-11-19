import sys
from PyQt6 import QtWidgets, uic
from MainWindow import Ui_MainWindow

qtcreator_file = '/Users/sydneymikulin/Documents/CodeJamProject/03_output/mainwindow.ui' # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Podcast Mode')
    window.show()
    sys.exit(app.exec())

genres = ['Personal Finance', 'Locally Focused', 'Sports', 'Business', 'Health & Fitness', 'Arts', 'Music', 'Technology', 'Fiction', 'History', 'Kids & Family', 'News', 'Comedy', 'Society & Culture', 'Religion & Spirituality', 'Government', 'TV & Film', 'Leisure', 'Education', 'Science', 'True Crime']
genres.sort()