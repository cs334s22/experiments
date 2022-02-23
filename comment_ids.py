import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)

db = client.mirrulations
comments = db.comments
cursor = comments.find({"$or": [{ "data.attributes.comment": {"$regex": "attach", "$options": "i"}}, {"data.attributes.comment": None}, { "data.attributes.comment": {"$regex": "document", "$options": "i"}}]}, {"data.id": 1, "data.relationships.attachments.links.self": 1})
total_count = len(list(cursor))


def get_comment_ids():
    count = 0
    with open('comment_ids.json', 'w') as file:
        file.write('[')
        for comment in cursor:
            # $options : i --> ignores case sensitivity
            # $regex --> Find where the value that "contains" the following string
            count += 1
            file.write(json.dumps(comment, default=str))
            if count < total_count:
                file.write(',')
        file.write(']')


if __name__ == '__main__':
    get_comment_ids()
