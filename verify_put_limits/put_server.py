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


        # Check that files are being sent, thus it is an attachment job
        if request.files.getlist('file') is not None:
            files = request.files.getlist('file') # All the files must have 'file'
            data = json.dumps(request.form.to_dict())
            for file in files:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # else: this is where the notmal stuff would happen

        # Check for the text file
        if request.form.getlist('text') is not None:
            file = request.files.getlist('text')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return 'OK'

    return app


if __name__ == '__main__':
    server = create_server()
    server.run(host='0.0.0.0', port=8080, debug=True)