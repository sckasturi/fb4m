from app import app
from flask import jsonify, request, render_template
from pymongo import MongoClient
from random import choice
from json import loads as json
client = MongoClient()

@app.route('/api/read', methods = ['GET'])
def reader():
    query = request.args.to_dict()
    print(query)
    db = client.findablogforme
    db.read.insert(query)
    del query["_id"]
    print(query)
    blogs = []
    query = json(str(query).lower().replace("'", "\""))
    print(query)
    empty_keys = [k for k,v in query.items() if len(v) < 1] 
    for i in empty_keys:
        del query[i]
    for blog in db.blogs.find(query):
        del blog["_id"]
        blogs.append(blog)
    if len(blogs) == 0:
        return jsonify([])
    return jsonify(choice(blogs))

@app.route('/')
def find_blogs():
   return render_template("index.html") 
