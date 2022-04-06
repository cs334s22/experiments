from flask import Flask, request, json
import base64
import os

'''
This had results, but couldn't work for both json and files

files = request.files.getlist('file')
if files is not None:
    files = request.files.getlist('file') # All the files must have 'file'
    for file in files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
data = json.loads(request.get_json()) 
# This is how we can read the text file
# if request.form.getlist('text') is not None:
#     file = request.files.getlist('text')
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
'''

def create_server():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'put_downloads')

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        
    @app.route('/put_data', methods=['PUT'])
    def put_data():
        data = json.loads(request.get_json())
        for key in data['results'].keys():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], key), 'wb') as f:
                f.write(base64.b64decode(data['results'][key].encode('utf-8')))

        return 'OK'

    return app


if __name__ == '__main__':
    server = create_server()
    server.run(host='0.0.0.0', port=8080, debug=True)