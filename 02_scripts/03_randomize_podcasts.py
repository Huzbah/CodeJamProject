#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
import sys
from listennotes import podcast_api
from requests import get
from pygame import mixer
import random
import multiprocessing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox,  QDateEdit, QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget, QLabel)
from PyQt6.QtGui import QIcon


def getJson(fileName): 
    f = open(fileName)
    data = json.load(f)
    return data

def getApiKey():
    f = open('./01_data/private/key.txt', 'r')
    return f.readline()

def getRecommendations(episode_id):
    api_key = getApiKey()
    client = podcast_api.Client(api_key=api_key)
    response = client.fetch_recommendations_for_episode(id=episode_id, safe_mode=0)
    
    return response

def getPodcastTitle(episode):
    try:
        return episode["podcast"]["title"]

    except:
        try:
            return episode["podcast"]["title_original"]
        except:
            return ""

def getEpisodeTitle(episode):
    try:
        return episode["title"]

    except:
        try:
            return episode["title_original"]
        except:
            return ""

def getEpisodeLink(playlist, i):
    if(i>=len(playlist)):
        return "ERROR: out of episodes to play"

    audioLink = playlist[i]["audio"]
    return audioLink

def removeDuplicates(playlist):
    result = []
    seen = []
    for d in playlist:
        if d["id"] not in seen:
            seen.append(d["id"])
            result.append(d)
    return result

def podcastPlayer(playlist):
    return

    
def playEpisode(playlist, i):  #Play
    currentsong = playlist[i]
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def pauseEpisode():
    return
    
def play(playlist):
    i=0
    while i < len(playlist):
        audioLink = getEpisodeLink(playlist, i)

        x = get(audioLink).content
        file = open('./03_output/podcasts/podcast1.mp3','wb')
        file.write(x)
        file.close()

        #p = multiprocessing.Process(target=playsound, args=('./03_output/podcasts/podcast.mp3',))
        #p.start()

        #get name of the podcast
        #stored differently sometimes, idk its the API
        

        print("Currently listening to: "+ epTitle+" from "+ podTitle)
        action = input("type SKIP to skip podcast or type STOP to end the ride \n")
        if action == "SKIP":
            p.terminate()
        if action == "STOP":
            p.terminate()
            break
        
        messageNum = random.randint(0,1)
        playsound('./03_output/podcasts/loadboardMessage'+str(messageNum)+'.mp3')
        i=i+1


def stop():
    return 0

def popUp(p, episode):
    # create a window to take in queue suggestions
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Podcast Player")
            
            label = QLabel('Currently Playing:')
            
           # title = QLabel('Currently listening to: '+ epTitle+' from '+ podTitle)

            pause = QPushButton()
            pause.setText('Pause')
            # confirm.setEnabled(False)
            pause.clicked.connect(stop)
    
            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(title)
            
            container = QWidget()
            container.setLayout(layout)
            layout.addWidget(pause)

            self.setCentralWidget(container)
            
        def text_changed(self, s):
            return s

        def current_text_changed(self, s):
            return s

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()


    app.exec()

def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/example.json')
    
    #recommendations = []
    recommendations = getJson('./01_data/recommendations.json')
    playlist=[]

    for episode in selectedOptions["results"]:
        playlist.append(episode)

    #for chosenEpisode in selectedOptions["results"]:
    #    for recommendedEpisode in getRecommendations(chosenEpisode["id"]).json()["recommendations"]:
    #       recommendations.append(recommendedEpisode)
    
    random.shuffle(recommendations)
    playlist=playlist+recommendations
    playlist=removeDuplicates(playlist)
    play(playlist)


    #with open('./01_data/recommendations.json', "w") as outfile:
    #    json.dump(playlist,outfile, indent=4)

if __name__ == '__main__':
    main()