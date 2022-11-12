#!/usr/bin/python3
from flask import Flask, abort, redirect, url_for, request, render_template
from urllib.parse import quote
import json
import requests
import string
import uuid
import os
from subprocess import Popen

db = {}

app = Flask(__name__)

@app.route("/new", methods=['POST'])
def new_message():
    global db
    #print(db)
    model = {}
    model['message'] = request.form['message']
    model['guid'] = str(uuid.uuid4())
    #print(f"new message created: {model['guid']}")
    db[model['guid']] = {}
    db[model['guid']]['message'] = model['message']
    db[model['guid']]['isread'] = False
    return render_template('new.html', model=model)

@app.route("/view/<id>", methods=['GET'])
def view(id):
    global db
    model = {}

    if request.cookies.get('flag'):
        #print(request.cookies['flag'])
        model['flag'] = request.cookies.get('flag')
    else:
        model['flag'] = ""

    if db[id]['isread']:
        model['message'] = "Message is gone!"
    else:
        model['message'] = db[id]['message']
        db[id]['isread'] = True
    return render_template('view.html', model=model)

@app.route("/admin-bot/<path:id>", methods=['POST'])
def admin_bot(id):
    url = f"http://127.0.0.1:5000/view/{id}"
    print(f"admin-bot running, url={url}")
    p = Popen(["node", "index.js", url])
    print("admin-bot finished")
    return render_template('admin-bot.html')
