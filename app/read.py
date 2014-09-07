from app import app
from flask import jsonify, request, render_template, redirect
from pymongo import MongoClient
from random import choice
from json import loads as json
from app.blog import get_blogs

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
        blogs.append(blog)
    if len(blogs) == 0:
        return redirect('/blog/none')
    return redirect('/blog/' + str(choice(blogs)["_id"]))

@app.route('/')
def find_blogs():
   db = client.findablogforme
   blogs = db.blogs.find()[:10]
   #for i in db.blogs.find():
   #    if len(blogs) == 10:
   #        break
   #    blogs.append(i)
   return render_template("index.html", blogs = get_blogs()) 
