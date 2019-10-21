import sys
import re
import csv
import json

cred = json.load(open('../data/condensed_2018.json'))
#print(cred)

tweets = open('../data/tweets.csv', 'w', encoding='utf-8')

# create the csv writer object

csvwrite = csv.writer(tweets)


for i in cred:
    tweet = i['text'].lower()
    tweet = re.sub(r"[,.]", "", tweet)
    #print(tweet)
    csvwrite.writerow([tweet])
tweets.close()
    
