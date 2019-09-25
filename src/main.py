from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

json.load(open('../credentials.json'))
cred = json.load(open('../credentials.json'))



#twitter api authentication
auth = OAuthHandler(cred["API"], cred["API Secret"])
auth.set_access_token(cred["Access"], "Access Secret")

#twitterStream = Stream(auth, listener())


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)




#a = tweepy.StreamListener(cred['Twitter API Key'])
#a.filter()
#a = tweepy.Stream(cred['Twitter API Key'], )
