import json

class JobQueue:

    def __init__(self, database):
        self.database = database

    def add_job(self, url, job_type=None):
        job = {
            'job_id': self.get_job_id(),
            'url': url,
            'job_type': job_type
            }
        self.database.lpush('jobs_waiting_queue', json.dumps(job))
        for type_ in ('attachments', 'comments', 'documents', 'dockets'):
            if job_type == type_:
                self.database.lpush(f'num_jobs_{type_}_waiting', json.dumps(job))
                break

    def get_job_id(self):
        return self.database.incr('last_job_id')
