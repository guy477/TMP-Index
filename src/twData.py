import tweepy
import json
import re
import requests
import sent, time
import storage
from datetime import datetime as dt
from datetime import timedelta
import pymysql
import sched
from threading import Thread

#json.load(open('../credentials.json'))
cred = json.load(open('../credentials.json'))



#twitter api authentication
auth = tweepy.OAuthHandler(cred["API"], cred["API Secret"])
auth.set_access_token(cred["Access"], cred["Access Secret"])



store = storage
thread = Thread(target=store.storage)
thread.start()


s = sent.Sentiment()

#store.genQuery("INSERT INTO test (hi)")

class twData:
    myStreamListener = None
    myStream = None
    def __init__(self):
        self.myStreamListener = MyStreamListener()
    
    def startStream(self):
        crash_counter = 0
        
        s = sched.scheduler(time.time, time.sleep(10))
        
        while(1):
            try:
                self.myStream = tweepy.Stream(auth=auth, listener = self.myStreamListener)
                #self.myStream.filter(follow=['25073877']) ### TRUMP
                self.myStream.filter(follow=['25073877'])  ### AMD
                print('hi')
            except:
                crash_counter+=1
                print(crash_counter)
                continue

    def timeHelper(self):
        pass
    """
    def filterTrack(self, track):
        self.myStream.filter(track = track)

    def filterFollow(self, follow):
        self.myStream.filter(follow = follow, is_async = True)
    """

vals = [[], []]

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):


    def on_status(self, status):
        #gets tweets directed at trump as well as trumps tweets.
        if('RT @' not in status.text and not status.retweeted ):
            tweet = status.text.lower()
            tweet = re.sub(r"[,.]", "", tweet)
            
            sen = s.sentiment(tweet)
            response = sen.getGlobalScoreTag()
            
            print(response)
            
            if('@realdonaldtrump' in tweet):
                a = s.scoreToVal(response)
                if(a != -2):
                    vals[0].append(a)
                
            
            if((vals[0].__len__() % 50 == 0) and len(vals[0])!=0):
                #store.send_message(status, str(sum(vals[0][len(vals[0])-50:])/50.))
                vals[0] = vals[0][-25:]
            
            #store.genQuery("INSERT INTO tweet (tweet) VALUES "+"(\'" + tweet +"\');")
        
        else:
            pass
    
    # on failure
    def on_error(self, status):
        print(status)
    
        
    

#twitterStream = Stream(auth, listener())
