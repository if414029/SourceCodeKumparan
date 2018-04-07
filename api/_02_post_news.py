import json
import sqlite3

from flask import request
from .configs import app
from .utilsnews import add_news, json_response, JSON_MIME_TYPE


@app.route('/news', methods=['POST'])
def news_create():
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    if not all([data.get('title'), data.get('content'), data.get('topic')]):
        error = json.dumps({'error': 'Missing field/s (title, content, topic)'})
        return json_response(error, 400)

    add_news(data)

    return json_response(status=201)