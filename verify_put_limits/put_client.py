import requests
import json

def put_data_basic(data):
    requests.put('http://127.0.0.1:8080/put_data', json=json.dumps(data))

def put_multiple(files):
    requests.put('http://127.0.0.1:8080/put_data', files=files) 

if __name__ == '__main__':
    # put_data({"test": "test"})
    # put_data_basic({"A": "a", "B": "b", "C": "c"})
    files = [open('test_files/test.txt', 'rb'), open('test_files/cameraman.tif', 'rb')] # write the bytes
    put_multiple(files)