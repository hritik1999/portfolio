from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run()