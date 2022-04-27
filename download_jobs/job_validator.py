import os
import sys
import dotenv
import redis
import time
from redis_check import is_redis_available
from search_iterator import SearchIterator
from regulations_api import RegulationsAPI
from data_storage import DataStorage
from job_queue import JobQueue


class WorkGenerator:

    def __init__(self, api, datastorage, job_queue):
        self.api = api
        self.datastorage = datastorage
        self.job_queue = job_queue

    def download(self, endpoint):
        beginning_timestamp = '1972-01-01 00:00:00'
        collection_size = self.datastorage.get_collection_size(endpoint)
        counter = 0
        for result in SearchIterator(self.api, endpoint, beginning_timestamp):
            if result == {}:
                continue
            for r in result['data']:
                if not self.datastorage.exists(r):
                    print(r['id'])
                    self.job_queue.add_job(r['links']['self'], r['type'])
                counter += 1
            percentage = (counter / collection_size) * 100
            print(f'{percentage:.2f}%')


def generate_work(collection=None):
    dotenv.load_dotenv()

    database = redis.Redis()
    # Sleep for 30 seconds to give time to load
    while not is_redis_available(database):
        print("Redis database is busy loading")
        time.sleep(30)

    api_key = os.getenv((collection.upper() if collection else 'DOCKETS') + '_API_KEY')
    api = RegulationsAPI(api_key)
    storage = DataStorage()
    job_queue = JobQueue(database)
    generator = WorkGenerator(api, storage, job_queue)

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
