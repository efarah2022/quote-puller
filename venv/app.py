from os import supports_effective_ids
from flask import Flask, render_template
from markupsafe import escape
import sqlite3
import json

class ConnSingleton(object):
    conn = None
c = sqlite3.connect("quotes_database.db", check_same_thread = False)
c.text_factory = str

# def listToString(s): 
#     quoteAuthorPair = s[0]
#     x = '{ "quote":' + quoteAuthorPair[0] + '"author":' + quoteAuthorPair[1] + ' }'
#     return x

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("quotes.html")

@app.route('/get-quote')
def get_quote():
    cursor = c.execute("SELECT * FROM quotes order by RANDOM() limit 1")
    return json.dumps(cursor.fetchall()[0])
    # return listToString(cursor.fetchall())