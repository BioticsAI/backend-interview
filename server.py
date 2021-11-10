from flask import Flask, jsonify, request
import model

import json

app = Flask(__name__)

if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)