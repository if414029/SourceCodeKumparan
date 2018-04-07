import json
import sqlite3

from flask import request
from .configs import app
from .utilstopic import add_topic, json_response, JSON_MIME_TYPE


@app.route('/topic', methods=['POST'])
def topic_create():
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    if not all([data.get('topic')]):
        error = json.dumps({'error': 'Missing field/s (topic)'})
        return json_response(error, 400)

    add_topic(data)

    return json_response(status=201)