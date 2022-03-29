from flask import Flask, request, json, jsonify

def create_server():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        
    @app.route('/put_data', methods=['PUT'])
    def put_data():
        for i,file in enumerate(request.files):
            with open(f'downloads/file_{i}', 'w') as f:
                f.write(file) # TODO: solve writing issues
        return request.data

    return app


if __name__ == '__main__':
    server = create_server()
    server.run(host='0.0.0.0', port=8080, debug=True)