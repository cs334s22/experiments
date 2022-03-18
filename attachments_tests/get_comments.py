import json
from pymongo import MongoClient

uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)

db = client.mirrulations
comments = db.comments
total_count = len(list(comments.find({}, {"data.id": 1, "data.relationships.attachments.links.related" : 1})))


def get_comments():
    # The limit 10 is just so we don't check everything in the database (for now)
    for count, comment in enumerate(comments.find({}, 
                            {"data.id": 1, "data.relationships.attachments.links.related" : 1}).limit(10)):
        with open(f'comment{count}.json', 'w') as file:
            # file.write('[')
            # Ideally we will just be sending this json, for now we save to disk
            file.write(json.dumps(comment, default=str))
            # if count < total_count:
            #     file.write(', \n')
            # file.write(']')


if __name__ == '__main__':
    get_comments()
    # with open('comments10.json') as file:
    #     json_file = json.load(file)
    #     print(type(json_file))