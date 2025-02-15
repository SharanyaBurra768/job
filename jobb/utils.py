from pymongo import MongoClient


client = MongoClient('mongodb+srv://wangchongye125:test123456@cluster0.of7cz.mongodb.net/job?retryWrites=true&w=majority&appName=Cluster0')
db = client['job']
users_collection = db['users']