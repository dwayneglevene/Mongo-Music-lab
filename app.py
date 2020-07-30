# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request,redirect
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'Musiclab'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://Musiclabadmin:9rS3biAl9GaWqkzp@cluster0.by8nn.mongodb.net/Musiclab?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    return "This is the music text"


# ADD SONGS

@app.route('/add')

def add():
    # define a variable for the collection you want to connect to
    item = mongo.db.items
    # use some method on that variable to add/find/delete data
    item.insert({"song":"Dem Franchize boys", "name":"D4L","Description":"We started snap"})
    item.insert({"song":"You got it bad", "name":"Usher","Description":"Love song"})

    # return a message to the user (or pass data to a template)
    return 'Got it'


# SHOW A LIST OF ALL SONG TITLES

@app.route("/songlist")

def songlist():
    collection = mongo.db.items
    events = collection.find({})
    print(events)
    return render_template("songlist.html",events=events)

