import requests

def put_data(files):
    requests.put('http://127.0.0.1:8080/put_data', files=files)


def put_data_and_json(files):
    requests.put('http://127.0.0.1:8080/put_data', data={'test1': 'TEST1', 'test2': 'TEST2'}, files=files)


if __name__ == '__main__':
    files = [
        ('file', open('test_files/test.txt', 'rb')), 
        ('file', open('test_files/cameraman.tif', 'rb')),
        ('file', open('test_files/test.pdf', 'rb')),
    ] # All the files must have 'file'
    # put_data(files)
    put_data_and_json(files)
