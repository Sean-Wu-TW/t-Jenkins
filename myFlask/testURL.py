import pymongo
from sqls.config import *

def findUsers():
    import mysql.connector
    cxn = mysql.connector.connect( 
        host=databaseConfig.get('hostname'), 
        user=databaseConfig.get('username'), 
        passwd=databaseConfig.get('password'), 
        db=databaseConfig.get('database') )
    cursor = cxn.cursor()
    sql = "SELECT * FROM User"
    cursor.execute(sql)
    res = list(cursor.fetchall())
    print(res)
    return res

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb+srv://Sean:wHHf6APYXRCzSozP@cluster0.ulkno.mongodb.net/test?retryWrites=true&w=majority")
    mydb = myclient["test"]
    mycol = mydb["user"]
    x = mycol.find_one()
    x['_id'] = str(x['_id'])
    print(x)
    findUsers()


