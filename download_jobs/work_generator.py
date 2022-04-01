import os
import time
import dotenv
import csv
from search_iterator import SearchIterator
from results_processor import ResultsProcessor
from regulations_api import RegulationsAPI
from data_storage import DataStorage


class WorkGenerator:

    def __init__(self, api, datastorage):
        # self.job_queue = job_queue
        self.api = api
        # self.processor = ResultsProcessor(job_queue, datastorage)
        self.datastorage = datastorage

    def download(self, endpoint):
        # Gets the timestamp of the last known job in queue
        # last_timestamp = self.job_queue.get_last_timestamp_string(endpoint)
        last_timestamp = '1972-01-01 00:00:00'
        f = open('missing_jobs.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['job_id', 'job_url', 'job_type'])
        # Finds a job, from the timestamp of the last known job
        # Returns a URL for the specific element
        for result in SearchIterator(self.api, endpoint, last_timestamp):
            if result == {}:
                continue
            for r in result['data']:
                if not self.datastorage.exists(r):
                    # print(r['id'])
                    writer.writerow([r['id'], r['links']['self'], r['type']])
            # If jobs are not in redis
            # add the URL to the jobs_queue (redis server)
            # self.processor.process_results(result)
            # timestamp = result['data'][-1]['attributes']['lastModifiedDate']
            # self.job_queue.set_last_timestamp_string(endpoint, timestamp)
        f.close()

if __name__ == '__main__':
    # I wrapped the code in a function to avoid pylint errors
    # about shadowing api and job_queue
    def generate_work():
        # Gets an API key
        dotenv.load_dotenv()
        api = RegulationsAPI(os.getenv('API_KEY'))

        storage = DataStorage()

        generator = WorkGenerator(api, storage)

        # Download dockets, documents, and comments
        # from all jobs in the job queue
        generator.download('dockets')
        # generator.download('documents')
        # generator.download('comments')

    while True:
        generate_work()
        # Sleeps for 6 hours
        time.sleep(60 * 60 * 6)
