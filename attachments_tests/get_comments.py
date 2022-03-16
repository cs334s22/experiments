import json
# import pymongo
from pymongo import MongoClient
# from bson.json_util import dumps, loads

uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)

db = client.mirrulations
comments = db.comments
documents = db.documents
collections = db.list_collections()
# cursor = comments.find().limit(100)
cursor = documents.find().limit(100)
total_count = len(list(cursor))


def get_comments():
    count = 0
    with open('comments100.json', 'w') as file:
        file.write('[')
        # for comment in comments.find().limit(100):
        for document in documents.find().limit(100):
            count += 1
            file.write(json.dumps(document['data']['relationships']['attachments']['links']['self'], default=str))
            # file.write(json.dumps(comments['data']['relationships']['attachments']['links']['self'], default=str))
            if count < total_count:
                file.write(', \n')
            # print(document)
        # for collect in collections:
        #     print(collect)
        file.write(']')


if __name__ == '__main__':
    get_comments()