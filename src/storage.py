import json
import pymysql
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
#gcloud database credentials



#Connect to remote database
#for deployment reference https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard_python37/cloudsql/main_mysql.py

host = '127.0.0.1'
cred = json.load(open('../credentials.json'))


class storage:
    db_user = ""
    db_password = ""
    db_name = ""
    db_connection_name = ""
    cnx = None
    cur = None
    #engine = None

    def __init__(self):
        self.db_user = cred['CLOUD_SQL_USERNAME']
        self.db_password = cred['CLOUD_SQL_PASSWORD']
        self.db_name = cred['CLOUD_SQL_DATABASE_NAME']
        db_connection_name = cred['CLOUD_SQL_CONNECTION_NAME']

        #connect(db_user, db_password, db_name, db_connection_name)

    def connect(self):
        try:
            self.cnx = pymysql.connect(host, user=self.db_user,
                              password=self.db_password, db=self.db_connection_name)
        except Exception:
            print("Error connecting to db. Check local proxy")
        else:
            with self.cnx:
                self.cur = self.cnx.cursor()
            return True
        return False
                
    

    def getVersion(self):
        self.cur.execute("SELECT VERSION()")
        ver = self.cur.fetchone()

        print(ver[0])

    
    def genQuery(self, query, verbose=False):
        try:
            self.cur.execute(query)
        except Exception:
            print("Error with query: " + query)
        else:
            self.cnx.commit()
            result = self.cur.fetchall()
            print(result)
    

    def select(self, person):
        try:
            self.cur.execute("SELECT * FROM {}".format(person))
        except Exception:
            print('error with query: '+person)
        output = self.cur.fetchall()
        if output is not None:
            for row in output:
                print(row)
        else:
            print('No '+person+' in db')

    def insert(self, person, tweet):
        try:
            self.cur.execute("INSERT INTO {} ({})".format(person, tweet))
        except:
            print('error with query involving '+ person+" and "+ tweet)
        
    
    def closeDB(self):
        try:
            self.cnx.close()
        except:
            print('couldnt close db')
    
    
    
