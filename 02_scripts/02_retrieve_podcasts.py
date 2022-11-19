from listennotes import podcast_api
import json 
import sys
import requests
from io import BytesIO
from PIL import Image
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox,  QDateEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,)
from PyQt5.QtGui import QIcon

api_key = open("../01_data/private/key.txt", "r").readline() # load api

with open("../01_data/examplefile.txt", "rt") as f: #load genre ids selected
    for line in f:
        genre_ids= line.split(',')
        
#display best podcasts and select from list to prepare queue
#merge json for recommendation during drive time

json_list=[]
#for term in genre_ids:
response=get_podcast(genre_ids[0])
    #display in gui

json_list=response.get('podcasts')

pod_dict={}
pick=1 # allows to choose for 5 pods

i=0
#for each podcast store the title and image to add to combobox
for pod in json_list:
    i=i+1
    pod_dict[pod.get('title')]=pod.get('image')
    if i==pick:
        break
    
    
import urllib.request

# create a window to take in queue suggestions
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create Queue")
        layout = QVBoxLayout()
    
        combobox= QComboBox() # intitialize a combo box
        
        for pod in pod_dict:
            urllib.request.urlretrieve(pod_dict[pod], "../03_output/"+pod)
            #img = Image.open("../03_output/"+pod)
            #img.save("../03_output/"+pod+".png", "PNG")
            
            response = requests.get(pod_dict[pod])
            img = Image.open(BytesIO(response.content))
            img.save("../03_output/"+pod+".png", "PNG")
            
            icon=QIcon("../03_output/"+pod+".png")
            combobox.addItem( pod)
            
  
        layout = QVBoxLayout()
        layout.addWidget(combobox)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def current_text_changed(self, s):
        print("Current text: ", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
