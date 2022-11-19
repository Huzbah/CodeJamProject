#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
from listennotes import podcast_api
from requests import get
from playsound import playsound

def getJson(fileName): 
    f = open(fileName)
    data = json.load(f)
    return data

def getApiKey():
    return '7591584d4b5d4dfd950f972ef7734277'

def getRecommendation(episode_id):

    api_key = getApiKey()
    client = podcast_api.Client(api_key=api_key)
    response = client.fetch_recommendations_for_episode(id=episode_id, safe_mode=0)
    
    return response
def play(audioLink):
    x = get(audioLink).content
    file = open('./03_output/podcast/podcast.mp3','wb')
    file.write(x)
    file.close()

    playsound('podcast.mp3')

def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/example.json')
    recommendations = []
    for list in selectedOptions["results"]:
        for episode in getRecommendation(list["id"]).json()["recommendations"]:
            recommendations.append(episode)
    #audioLink = recommendations["recommendations"][0]["audio"]
    #play(audioLink)

    with open('./01_data/recommendations.json', "w") as outfile:
        json.dump(recommendations,outfile)
    #play(playNext)

if __name__ == '__main__':
    main()