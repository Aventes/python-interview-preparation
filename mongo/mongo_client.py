import pymongo

client = pymongo.MongoClient(
    'mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.1')

db_ = client['mydb']
users_col_ = db_['users']
print(db_.list_collection_names())

