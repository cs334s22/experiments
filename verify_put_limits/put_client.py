import requests
from json import dumps, loads, load
import base64

'''
This had results, but couldn't work for both json and files

def put_data(data, params, files):
    requests.put('http://127.0.0.1:8080/put_data', json=dumps(data), params=params, files=files)
    # requests.put('http://127.0.0.1:8080/put_data', json=dumps(data), params=params)
    # requests.put('http://127.0.0.1:8080/put_data', params=params, files=files)

if __name__ == '__main__':
    files = [
        ('file', open('test_files/test.txt', 'rb')), 
        ('file', open('test_files/cameraman.tif', 'rb')),
        ('file', open('test_files/test.pdf', 'rb')),
        # ('text', open('test_files/test.txt', 'rb')), # This is what a text extracted from a PDF would be
    ]

    data = {'directory': '/path/to/dir', 
            'job_id': 17, 
            'results': 'attachments',
            }
    params = {'client_id': 42} 
    put_data(data, params, files)
'''

def put_data(data, params, files):
    requests.put('http://127.0.0.1:8080/put_data', json=dumps(data), params=params)

if __name__ == '__main__':

    # The keys should be generated from a combination of the job_id and the file format
    # see download_attachments() from attachments_tests/get_comment_attachments.py for how we get the format
    files = {
        'test.txt': str(base64.b64encode(open('test_files/test.txt', 'rb').read()).decode('utf-8')),
        'cameraman.tif': str(base64.b64encode(open('test_files/cameraman.tif', 'rb').read().decode('utf-8'))), 
        'test.pdf': str(base64.b64encode(open('test_files/test.pdf', 'rb').read().decode('utf-8'))), 
    }

    data = {'directory': '/path/to/dir', 
            'job_id': 17, 
            'results': files,
            }
    params = {'client_id': 42} 
    put_data(data, params, files)






