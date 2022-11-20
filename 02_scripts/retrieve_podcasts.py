from listennotes import podcast_api
import json 
import sys
import requests
from io import BytesIO
from PIL import Image
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox,  QDateEdit, QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget, QLabel)
from PyQt6.QtGui import QIcon

api_key = ""

def get_podcast(term):
    global api_key
    client = podcast_api.Client(api_key=api_key)      
    response = client.search(q=term, offset=5, unique_podcasts=1, language= 'English')
    #print(response.json)
    return response.json()
#display best podcasts and select from list to prepare queue
#merge json for recommendation during drive time

def get_title_dict(response):
    pick=5 # allows to choose from 5 pods
    i=0
    pod_dict={}   #for each podcast store the title and image to add to combobox
    
    for pod in response:
        i=i+1
        pod_dict[pod.get('podcast').get('title_original')]= pod
            #response = requests.get(pod.get('image'))
            #img = Image.open(BytesIO(response.content))
            #img.save("../03_output/"+pod.get('title')+".png", "PNG")
        if i==pick:
            break
    return pod_dict

def select_queue():
    global api_key
    api_key = open("./01_data/private/key.txt", "r").readline() # load api

    with open("./01_data/examplefile.txt", "rt") as f: #load genre ids selected
        for line in f:
            terms= line.split(',')
            
    #declare variable to collect queue
    queue_list=[]

    #get podcasts with call to api
    response1=get_podcast(terms[0]).get('results')
    response2=get_podcast(terms[1]).get('results')
    response3=get_podcast(terms[2]).get('results')

    pod_dict1=get_title_dict(response1)
    pod_dict2=get_title_dict(response2)
    pod_dict3=get_title_dict(response3)

    #display option in gui
    # create a window to take in queue suggestions
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Create Queue")
            
            label = QLabel('Select podcasts for your queue:')
            
            layout = QVBoxLayout()
        
            combobox1= QComboBox() # intitialize a combo box
            combobox2= QComboBox()
            combobox3= QComboBox()
            
            label1 = QLabel('Select the first podcast:')
            for pod in pod_dict1:
                
                icon=QIcon("./03_output/icon.png")
                combobox1.addItem(pod, icon)
            
            # Connect signals
        
            combobox1.currentTextChanged.connect(self.text_changed)
            combobox1.activated.connect(self.check_index)
             
            label2 = QLabel('Select the second podcast:')
            for pod in pod_dict2:
                
                icon=QIcon("./03_output/icon.png")
                combobox2.addItem(pod, icon)
            
            # Connect signals
        
            combobox2.currentTextChanged.connect(self.text_changed)
            combobox2.activated.connect(self.check_index)
            
            label3 = QLabel('Select the third podcast:')
            for pod in pod_dict3:
                
                icon=QIcon("./03_output/icon.png")
                combobox3.addItem(pod, icon)
            
            # Connect signals
            combobox3.activated.connect(self.check_index)
            combobox3.currentTextChanged.connect(self.text_changed)
            
            confirm = QPushButton()
            confirm.setText('Confirm Selection')
            self.confirm.setEnabled(False)
            # confirm.setEnabled(False)
            confirm.clicked.connect(self.close)
    
            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(label1)
            layout.addWidget(combobox1)
            layout.addWidget(label2)
            layout.addWidget(combobox2)
            layout.addWidget(label3)
            layout.addWidget(combobox3)
            
            container = QWidget()
            container.setLayout(layout)
            layout.addWidget(confirm)

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

            
        def text_changed(self, s):
            queue_list.append(s)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

    queue_dict={}

    queue_dict[queue_list[0]]=pod_dict1.get(queue_list[0])
    queue_dict[queue_list[1]]=pod_dict2.get(queue_list[1])
    queue_dict[queue_list[2]]=pod_dict3.get(queue_list[2])

    json_object = json.dumps(queue_dict)

    # Writing to file
    with open("./01_data/queue.json", "w") as outfile:
        outfile.write(json_object)