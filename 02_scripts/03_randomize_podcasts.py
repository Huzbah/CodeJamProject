#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
from listennotes import podcast_api
from requests import get
from playsound import playsound
import random
import multiprocessing


def getJson(fileName): 
    f = open(fileName)
    data = json.load(f)
    return data

def getApiKey():
    f = open('./01_data/private/key.txt', 'r')
    return f.readline()

def getRecommendation(episode_id):
    api_key = getApiKey()
    client = podcast_api.Client(api_key=api_key)
    response = client.fetch_recommendations_for_episode(id=episode_id, safe_mode=0)
    
    return response

def play(playlist):
    i=0
    while i < len(playlist):
        audioLink = getEpisodeLink(playlist, i)

        x = get(audioLink).content
        file = open('./03_output/podcasts/podcast.mp3','wb')
        file.write(x)
        file.close()

        p = multiprocessing.Process(target=playsound, args=('./03_output/podcasts/podcast.mp3',))
        p.start()

        #get name of the podcast
        #stored differently sometimes, idk its the API
        try:
            epTitle = playlist[i]["title"]
            podTitle = playlist[i]["podcast"]["title"]
        except:
            try: 
                epTitle = playlist[i]["title_orginal"]
                podTitle = playlist[i]["podcast"]["title_original"]
            except:
                epTitle = ""
                podTitle = ""

        print("Currently listening to: "+ epTitle+" from "+ podTitle)
        action = input("type SKIP to skip podcast or type STOP to end the ride \n")
        if action == "SKIP":
            p.terminate()
        if action == "STOP":
            p.terminate()
            break
        
        messageNum = random.randint(1,2)
        playsound('./03_output/podcasts/loadboardMessage'+str(messageNum)+'.mp3')
        i=i+1


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

    
    #[result.append(x) for x in playlist if x not in result]
    return result

def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/example.json')
    
    recommendations = []
    #recommendations = getJson('./01_data/recommendations.json')
    playlist=[]

    for episode in selectedOptions["results"]:
        playlist.append(episode)

    for list in selectedOptions["results"]:
        for episode in getRecommendation(list["id"]).json()["recommendations"]:
           recommendations.append(episode)
  
    random.shuffle(recommendations)
    playlist=playlist+recommendations
    playlist=removeDuplicates(playlist)
    play(playlist)


    #with open('./01_data/recommendations.json', "w") as outfile:
    #    json.dump(playlist,outfile, indent=4)

if __name__ == '__main__':
    main()