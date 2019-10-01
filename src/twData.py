import tweepy
import json
import storage
import pymysql

json.load(open('../credentials.json'))
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
        try:
            self.myStream = tweepy.Stream(auth=auth, listener = self.myStreamListener)
            self.myStream.filter(follow=['25073877'])
            
            
        except:
            print('Error starting tweepy Stream.')
            
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
        
        #print(status.created_at)
        #print(status.user.screen_name)
        print("_______________________________________________________")
        
        #self.myStream.filter(follow=['25073877'])
        #store.genQuery("")
        #store.genQuery("CREATE TABLE IF NOT EXISTS `tweet` (`tweet` varchar(255));")
        #print()
        if("RT" not in status.text[:2]):
            print(status.text)
            store.genQuery("INSERT INTO tweet (tweet) VALUES "+"(\'" + str(status.text).replace("\'|\"", "") +"\');")
    
    # on failure
    def on_error(self, status):
        print(status)

#twitterStream = Stream(auth, listener())

