import pymongo

myclient = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@cluster0-dc74l.mongodb.net/test?retryWrites=true&w=majority")

mydb = myclient["TwitterData_ADB"]
mycol = mydb["Tweets_locations"]


#print(myclient.list_database_names())


def insertaColeccion(datos):
    global mycol
    mycol.insert_one(datos)
