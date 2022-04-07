import requests
from json import dumps
import base64

def put_data(data, params):
    requests.put('http://127.0.0.1:8080/put_data', json=dumps(data), params=params)


if __name__ == '__main__':

    # The keys should be generated from a combination of the job_id and the file format
    # see download_attachments() from attachments_tests/get_comment_attachments.py for how we get the format
    files = {
        'test.txt': base64.b64encode(open('test_files/test.txt', 'rb').read()).decode('ascii'),
        'cameraman.tif': base64.b64encode(open('test_files/cameraman.tif', 'rb').read()).decode('ascii'),
        'test.pdf': base64.b64encode(open('test_files/test.pdf', 'rb').read()).decode('ascii'),
        'waldo.png': base64.b64encode(open('test_files/waldo.png', 'rb').read()).decode('ascii'),
    }

    data = {'directory': '/path/to/dir', 
            'job_id': 17, 
            'results': files,
            }
    params = {'client_id': 42} 
    put_data(data, params)
