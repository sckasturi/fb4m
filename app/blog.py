from app import app
from flask import jsonify, request, render_template, redirect
from pymongo import MongoClient
from json import loads as json
from bson.objectid import ObjectId
from random import choice, sample

client = MongoClient()

def get_blogs():
    db = client.findablogforme
    blogs = []
    blog_count = 10
    blog_list = db.blogs.find()
    for i in blog_list:
        blogs.append(i)
    return sample(blogs, 5)

@app.route('/api/blog', methods = ['POST'])
def blogger():
    input_ = request.form.to_dict()
    db = client.findablogforme
    input_["topics"] = input_["topics"].lower().replace(" ", "").split(",")
    #input_["topics"] = json(str(input_["topics"]).lower().replace("'","\""))
    db.blogs.insert(input_)
    del input_["_id"]
    return redirect("/")

@app.route('/submit', methods = ['GET'])
def submit_blog():
    return render_template("submit.html", blogs = get_blogs())

@app.route('/blog/<uid>')
def show_blog(uid):
    db = client.findablogforme
    blogs = []
    blog = db.blogs.find_one({'_id': ObjectId(uid)})
    return render_template("blog.html", blog = blog, blogs = get_blogs())

def random_tag(i):
    return (["primary", "success", "warning", "danger", "default"]*100)[i]

@app.context_processor
def inject_functions():
    return dict(random_color=random_tag, enumerate=enumerate)
