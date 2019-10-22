import sys
import re
import csv
import json
import string

#print(cred)


# get tweet data and create the csv writer object


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

