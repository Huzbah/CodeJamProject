#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
import sys
from listennotes import podcast_api
from requests import get
from pygame import mixer
import pygame
import random
from tkinter import *
import os 
from itertools import cycle



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
    try:
        audioLink = playlist[i]["audio"]
    except:
        audioLink = playlist[i]["listennotes_url"]
    return audioLink

def removeDuplicates(playlist):
    result = []
    seen = []
    for d in playlist:
        if d["id"] not in seen:
            seen.append(d["id"])
            result.append(d)
    return result
    mixer.music.unpause()

def player(playlist):
    root = Tk()
    root.title('Music player')
    
    mixer.init()

    def playEpisode(playlist, i): 
        print("playing")
        audioLink = getEpisodeLink(playlist, i)

        x = get(audioLink).content
        file = open('./03_output/podcasts/podcast.mp3','wb')
        file.write(x)
        file.close()
        mixer.music.load('./03_output/podcasts/podcast.mp3')
        mixer.music.play()

    def pauseEpisode():
        mixer.music.pause()

    def stopPlaying():
        mixer.music.stop()
        exit

    def unpauseEpisode():
        mixer.music.unpause()
    
    #def nextEpisode(playlist, i):
    #    mixer.music.unload()
    #    mixer.music.load('./03_output/podcasts/loadboardMessage1.mp3')
    #    mixer.music.play()

        #i=i+1
        #playEpisode(playlist, i)

    
    playbtn = Button(root, text="Play", command=playEpisode(playlist, 0))
    playbtn.grid(row=1, column=0)

    pausebtn = Button(root, text="Pause", command=pauseEpisode)
    pausebtn.grid(row=1, column=1)

    resumebtn = Button(root, text="Resume", command=unpauseEpisode)
    resumebtn.grid(row=1, column=2)

    #nextbtn = Button(root, text="Skip", command=nextEpisode(playlist, i))
    #nextbtn.grid(row=1, column=3)

    stopbtn = Button(root, text="End Drive", command=stopPlaying)
    stopbtn.grid(row=2, column=1)

    #And finally run the loop start the application
    mainloop()  



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


def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/queue.json')
    
    #recommendations = []
    recommendations = getJson('./01_data/recommendations.json')
    playlist=[]

    for key in selectedOptions:
        playlist.append(selectedOptions[key])

    #for chosenEpisode in selectedOptions["results"]:
    #    for recommendedEpisode in getRecommendations(chosenEpisode["id"]).json()["recommendations"]:
    #       recommendations.append(recommendedEpisode)
    
    random.shuffle(recommendations)
    playlist=playlist+recommendations
    playlist=removeDuplicates(playlist)

    player(playlist)

    #play(playlist)


    with open('./01_data/recommendations.json', "w") as outfile:
        json.dump(playlist,outfile, indent=4)

if __name__ == '__main__':
    main()