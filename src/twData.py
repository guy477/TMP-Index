import tweepy
import json
import re
import requests
import storage
from datetime import datetime as dt
from datetime import timedelta
import pymysql

#json.load(open('../credentials.json'))
cred = json.load(open('../credentials.json'))



#twitter api authentication
auth = tweepy.OAuthHandler(cred["API"], cred["API Secret"])
auth.set_access_token(cred["Access"], cred["Access Secret"])

store = storage.storage()
store.connect()

#store.genQuery("INSERT INTO test (hi)")

class twData():
    myStreamListener = None
    myStream = None
    def __init__(self):
        self.myStreamListener = MyStreamListener()
    
    def startStream(self):
        crash_counter = 0
        while(1):
            try:
                self.myStream = tweepy.Stream(auth=auth, listener = self.myStreamListener)
                self.myStream.filter(follow=['25073877'])
                
                
            except:
                crash_counter+=1
                print(crash_counter)
                continue
            
    """
    def filterTrack(self, track):
        self.myStream.filter(track = track)

    def filterFollow(self, follow):
        self.myStream.filter(follow = follow, is_async = True)
    """

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    """
    raw_data['user']['screen_name']
	created_at = parser.parse(raw_data['created_at'])
	tweet = raw_data['text']
	retweet_count = raw_data['retweet_count']
    """

    def on_status(self, status):
        
        if('RT @' not in status.text and not status.retweeted ):
            tweet = status.text.lower()
            tweet = re.sub(r"[,.]", "", tweet)
            print(tweet)
            send_message(status, 'teehee')
            print("++++++++++++++++++++")
            store.genQuery("INSERT INTO tweet (tweet) VALUES "+"(\'" + tweet +"\');")
        else:
            pass
    
    # on failure
    def on_error(self, status):
        print(status)
        
    def send_message(self, status, action):
        n = dt.now()
        n = n - timedelta(microseconds=n.microsecond)
        n = n.time()
        print("sending message")
        return requests.post("https://api.mailgun.net/v3/sandboxe081d808d2ae4d7994bef28c0cb47653.mailgun.org/messages",
                             auth=("api", cred['mailgun']),
                             data={"from": "TRADE NOTIFICATION<postmaster@sandboxe081d808d2ae4d7994bef28c0cb47653.mailgun.org>",
                                   "to": "tmp.trade.notifier@gmail.com",
                                   "subject": "Trump - {}".format(status.text),
                                   "text": "Time: {}".format(status.created_at)})

#twitterStream = Stream(auth, listener())
