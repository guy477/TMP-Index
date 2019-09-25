import storage
import twData

def main():
    db = storage.storage()
    if db.connect():
        tw = twData.twData()
        tw.startStream()
        #Donald Trump = 25073877
        #Jim Cramer   = 14216123
        #tw.filterFollow()
        
    

if __name__ == '__main__':
    main()
    

#a = tweepy.StreamListener(cred['Twitter API Key'])
#a.filter()
#a = tweepy.Stream(cred['Twitter API Key'], )
