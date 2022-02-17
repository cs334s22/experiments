import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

uri = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
client = MongoClient(uri)

db = client.mirrulations
comments = db.comments
total_count = 276451  # TODO: Need to fix --> It shouldn't be hard-coded :(


def get_comment_ids():
    count = 0
    with open('comment_ids.json', 'w') as file:
        file.write('[')
        for comment in comments.find({"data.attributes.comment": {"$regex": "see attachment", "$options": "i"}},{"data.id": 1}):
            count += 1
            file.write(json.dumps(comment, default=str))
            if count < total_count:
                file.write(',')
        file.write(']')


if __name__ == '__main__':
    get_comment_ids()
