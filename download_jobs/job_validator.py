import os
import sys
import dotenv
import csv
from search_iterator import SearchIterator
from regulations_api import RegulationsAPI
from data_storage import DataStorage


class WorkGenerator:

    def __init__(self, api, datastorage):
        self.api = api
        self.datastorage = datastorage

    def download(self, endpoint):
        beginning_timestamp = '1972-01-01 00:00:00'
        collection_size = self.datastorage.get_collection_size(endpoint)
        f = open(f'missing_{endpoint}.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['job_id', 'job_url', 'job_type'])
        counter = 0
        for result in SearchIterator(self.api, endpoint, beginning_timestamp):
            if result == {}:
                continue
            for r in result['data']:
                if not self.datastorage.exists(r):
                    print(r['id'])
                    writer.writerow([r['id'], r['links']['self'], r['type']])
                counter += 1
            percentage = (counter / collection_size) * 100
            print(f'{percentage:.2f}%')
        f.close()



def generate_work(collection=None):
    dotenv.load_dotenv()

    if collection is not None:
        api_key = os.getenv(f'{collection.upper()}_API_KEY')
    else:
        api_key = os.getenv('DOCKETS_API_KEY')

    api = RegulationsAPI(api_key)
    storage = DataStorage()
    generator = WorkGenerator(api, storage)

    if not collection:
        generator.download('dockets')
        generator.download('documents')
        generator.download('comments')
    else:
        generator.download(collection)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('dockets', 'documents', 'comments'):
        generate_work(sys.argv[1])
    else:
        generate_work()
