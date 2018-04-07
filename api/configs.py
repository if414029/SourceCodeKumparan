import os
import sqlite3

from flask import Flask, g


app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('upload')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# connect to database
@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])


# @app.errorhandler(404)
# def not_found(e):
#     return '', 404