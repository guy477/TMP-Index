import storage
import twData
import json
from threading import Thread
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/get_data")
def get_data():
    
    print(twData.vals)
    if(twData.vals[0].__len__() > 25):
        return jsonify({'payload':json.dumps({'data':sum(twData.vals[0][-25:])/25.0})})
    if(twData.vals[0].__len__() ==0 ):
        return jsonify({'payload':json.dumps({'data':0.0})})
    return jsonify({'payload':json.dumps({'data':sum(twData.vals[0])/len(twData.vals[0])})})

@app.route("/")
def restult():
    return render_template('main.html')

def data():
    tw = twData.twData()
    tw.startStream()

if __name__ == "__main__":
    thread = Thread(target=data)
    thread.start()
    app.run(debug=True)


"""
def main():
    db = storage.storage()
    if db.connect():
        tw = twData.twData()
        tw.startStream()
        #Donald Trump = 25073877
        #Jim Cramer   = 14216123
        #AMD          = 14861876
        #tw.filterFollow()
        
    

if __name__ == '__main__':
    main()
    

#a = tweepy.StreamListener(cred['Twitter API Key'])
#a.filter()
#a = tweepy.Stream(cred['Twitter API Key'], )
"""