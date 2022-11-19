#a method to shuffle podcasts after the selected few is played 
#uses the orginal list of fetched podcasts as well as new keywords from 
#the selected podcasts
#attempts to make the queue the length of the drive
import json
from collections import Counter

def getJson(fileName): 
    f = open(fileName)
    data = json.load(f)
    return data

#clean common words
def findTopMatches(allOptions, selectedOptions):
    for i in range(1):
        textData = allOptions["results"][i]['title_original']+allOptions["results"][i]['description_original']
    splitText = textData.split()
    counter = Counter(splitText)
    most_occur = counter.most_common(4)
    print(most_occur)

def main():
    # currently opening a test file
    allOptions = getJson('./01_data/example.json')
    selectedOptions = getJson('./01_data/example.json')
    findTopMatches(allOptions, selectedOptions)


if __name__ == '__main__':
    main()