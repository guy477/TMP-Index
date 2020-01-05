import sys
import re
import csv
import json
import string
import meaningcloud

#print(cred)

cred = json.load(open('../credentials.json'))
class Sentiment:
    
    def __init__(self):
        super().__init__()
        
    def sentiment(self, inp):
        return meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(cred['sent-api2'], lang='en', txt=inp, txtf='plain').sendReq())

    def scoreToVal(self, scoreTag):
        val = 0
        if scoreTag == "P+":            
            val = 1
        elif scoreTag == "P":
            val = .5
        elif scoreTag == "NEU":
            val = 0
        elif scoreTag == "N":
            val = -.5
        elif scoreTag == "N+":
            val = -1
        else:
            val = -2

        return val
    

# get trump historica tweet data from 2018 and create the csv writer object
"""
cred = json.load(open('../data/condensed_2018.json'))
tweets = open('../data/tweets.csv', 'w', encoding='utf-8', newline="")
csvwrite = csv.writer(tweets)


for i in cred:
    tweet = i['text'].lower()
    # ’ and “ are special characters.
    tweet = re.sub(r"["+string.punctuation+"“’]*", "", tweet)
    #|
    tweet = re.sub(r"http(\w)*", "", tweet)
    if "\"" in tweet:
        print(tweet)
    csvwrite.writerow([tweet])
tweets.close()

"""



#ToDo:
#   Train a sentiment analysis model on trumps tweets

