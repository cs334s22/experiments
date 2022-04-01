from flask import Flask, request, jsonify
import json
import os

def create_server():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'put_downloads')

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        
    @app.route('/put_data', methods=['PUT'])
    def put_data():
        files = request.files.getlist('file') # All the files must have 'file'
        data = json.dumps(request.form.to_dict())
        print(data)
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'OK'

    return app


if __name__ == '__main__':
    server = create_server()
    server.run(host='0.0.0.0', port=8080, debug=True)