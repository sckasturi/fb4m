from app import app
from flask import jsonify, request
from pymongo import MongoClient
from random import choice

client = MongoClient()

@app.route('/read', methods = ['GET'])
def reader():
    input_ = request.get_json()
    db = client.findablogforme
    db.read.insert(input_)
    del input_["_id"]
    blogs = []
    for blog in db.blogs.find(input_):
        del blog["_id"]
        blogs.append(blog)
    return jsonify(choice(blogs))
