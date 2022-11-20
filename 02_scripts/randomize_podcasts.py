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

CURR = 0

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

    def playEpisode(playlist): 
        audioLink = getEpisodeLink(playlist, CURR)
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
        root.quit()

    def unpauseEpisode():
        mixer.music.unpause()

    def nextEpisode(playlist):
        mixer.music.stop()
        mixer.music.unload()
        global CURR
        i = CURR%3 +1
        mixer.music.load('./03_output/podcasts/loadboardMessage'+str(i)+'.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            pass
    
        mixer.music.stop()
        mixer.music.unload()
    
        CURR =  CURR + 1
        playEpisode(playlist)


    playbtn = Button(root, text="Play", command = lambda: playEpisode(playlist))
    playbtn.grid(row=1, column=0)

    pausebtn = Button(root, text="Pause", command=pauseEpisode)
    pausebtn.grid(row=1, column=1)

    resumebtn = Button(root, text="Resume", command=unpauseEpisode)
    resumebtn.grid(row=1, column=2)

    nextbtn = Button(root, text="Skip", command=lambda: nextEpisode(playlist))
    nextbtn.grid(row=1, column=3)

    stopbtn = Button(root, text="End Drive", command=stopPlaying)
    stopbtn.grid(row=2, column=1)

    #And finally run the loop start the application
    mainloop()  


def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/queue.json')
    
    recommendations = []
    #recommendations = getJson('./01_data/recommendations.json')
    playlist=[]

    for key in selectedOptions:
        playlist.append(selectedOptions[key])

    for key in selectedOptions:
       for recommendedEpisode in getRecommendations(selectedOptions[key]["id"]).json()["recommendations"]:
            recommendations.append(recommendedEpisode)
    
    random.shuffle(recommendations)
    playlist=playlist+recommendations
    playlist=removeDuplicates(playlist)

    player(playlist)

if __name__ == "__main__":
    main()