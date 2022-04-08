import pymongo


class DataStorage:
    def __init__(self):
        database = pymongo.MongoClient('localhost', 27017)['mirrulations']
        self.dockets = database['dockets']
        self.documents = database['documents']
        self.comments = database['comments']

    def exists(self, search_element):
        result_id = search_element['id']

        return self.dockets.count_documents({'data.id': result_id}) > 0 or \
            self.documents.count_documents({'data.id': result_id}) > 0 or \
            self.comments.count_documents({'data.id': result_id}) > 0

    def get_collection_size(self, collection):
        return self.__getattribute__(collection).count_documents({})
