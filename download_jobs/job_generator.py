import redis
import time
from redis_check import is_redis_available
import json
from csv import DictReader


class AttachmentsGenerator:

        def __init__(self, database):
            self.database = database

        def get_job_id(self):
            return self.database.incr('last_job_id')

        def add_job(self, job_type, url):
            return {'job_id': self.get_job_id(),
                    'url': url,
                    'job_type': job_type
                    }

        def add_job_type_counter(self, job, database):
            job_count = {'num_jobs' : 0}
            for type_ in ('attachments', 'comments', 'dockets', 'documents'):
                if job['job_type'] == type_:
                    job_count['num_jobs'] += 1
                    t = 'num_jobs_' + (type_ if type_ != 'attachments' else 'attach') + '_queue'
                    database.lpush(f'num_jobs_{t}_queue', json.dumps(job_count))


if __name__ == '__main__':
    database = redis.Redis()
    while not is_redis_available(database):
        print("Redis database is busy loading")
        time.sleep(30)
    
    generator = AttachmentsGenerator(database)

    for type_ in ('dockets', 'documents', 'comments'):
        reader = DictReader(open(f'missing_{type_}.csv'))
        for row in reader:
            job = generator.add_job(type_, row['job_url'])
            generator.add_job_type_counter(job, database)
            database.lpush('jobs_waiting_queue', json.dumps(job))
