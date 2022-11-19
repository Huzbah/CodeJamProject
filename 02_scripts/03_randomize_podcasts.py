#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
from listennotes import podcast_api

def getJson(fileName): 
    f = open(fileName)
    data = json.load(f)
    return data

#clean common words
def findTopMatches(allOptions, selectedOptions):
    preferedGenreCombos = [2]
    print(len(selectedOptions["results"]))
    for i in selectedOptions["results"]:
        print(i["podcast"]["genre_ids"])
    #print(selectedOptions["results"][9])
    #for i in selectedOptions["results"][0]:
    #    preferedGenreCombos.append(i['podcast']['genre_ids'])
    #    print(preferedGenreCombos)

def getApiKey():
    return '7591584d4b5d4dfd950f972ef7734277'

def getRecommendation(episode_id):
    api_key = getApiKey()

    client = podcast_api.Client(api_key=api_key)

    response = client.fetchRecommendationsForEpisode(id: episode_id)
    
    return response

def main():
    # currently opening a test file
    selectedOptions = getJson('./01_data/example.json')
    getRecommendation(selectedOptions["results"][0][""])


if __name__ == '__main__':
    main()