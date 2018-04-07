import json

from flask import request
from .configs import app
from .utilsnews import update_news, validate_news, json_response, JSON_MIME_TYPE


@app.route('/news-edit/<int:id_news>', methods=['PUT'])
def news_update(id_news):
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    if not all([data.get('title'), data.get('content'), data.get('topic')]):
        error = json.dumps({'error': 'Missing field/s (title, content, topic)'})
        return json_response(error, 400)

    # check whether the news with id_news is valid
    if not validate_news(id_news):
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    update_news(id_news, data)

    return json_response(status=204)