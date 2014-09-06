from app import app
from flask import jsonify, request
from pymongo import MongoClient

client = MongoClient()

@app.route('/read', methods = ['POST'])
def reader():
    input_ = request.get_json()
    db = client.findablogforme
    db.blogs.insert(input_)
    del input_["_id"]
    return jsonify(input_)
