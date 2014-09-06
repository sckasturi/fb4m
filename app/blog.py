from app import app
from flask import jsonify, request, render_template, redirect
from pymongo import MongoClient
from json import loads as json

client = MongoClient()

@app.route('/api/blog', methods = ['POST'])
def blogger():
    input_ = request.form.to_dict()
    db = client.findablogforme
    input_["topics"] = input_["topics"].lower().replace(" ", "").split(",")
    #input_["topics"] = json(str(input_["topics"]).lower().replace("'","\""))
    db.blogs.insert(input_)
    del input_["_id"]
    return redirect("/")

@app.route('/blog', methods = ['GET'])
def submit_blog():
    
    return render_template("blog.html")
