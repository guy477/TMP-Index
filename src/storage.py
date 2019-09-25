import json
import pymysql
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
#gcloud database credentials



#Connect to remote database
#for deployment reference https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard_python37/cloudsql/main_mysql.py

host = '127.0.0.1'



class storage:
    cred = json.load(open('../credentials.json'))
    cnx = None
    engine = None
    def __init__():
        db_user = cred['CLOUD_SQL_USERNAME']
        db_password = cred['CLOUD_SQL_PASSWORD']
        db_name = cred['CLOUD_SQL_DATABASE_NAME']
        db_connection_name = cred['CLOUD_SQL_CONNECTION_NAME']

        connect(db_user, db_password, db_name, db_connection_name)

    def connect(usr, pswd, name, conn):
        cnx = pymysql.connect(user=usr, password=pswd,
                              host=name, db=conn)
        pool(usr, pswd, name, conn)
        

    def pool(usr, pswd, name, conn):
        engine_url = 'mysql+pymysql://{}:{}@{}/{}'.format(
        usr, pswd, name, conn)
        engine = sqlalchemy.create_engine(engine_url, poolsize=3)
        
    
    
    
