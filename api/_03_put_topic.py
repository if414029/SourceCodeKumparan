import json

from flask import request
from .configs import app
from .utilstopic import update_topic, validate_topic, json_response, JSON_MIME_TYPE


@app.route('/topic-edit/<int:id_topic>', methods=['PUT'])
def topic_update(id_topic):
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    if not all([data.get('topic')]):
        error = json.dumps({'error': 'Missing field/s (topic)'})
        return json_response(error, 400)

    # check whether the topic with id_topic is valid
    if not validate_topic(id_topic):
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    update_topic(id_topic, data)

    return json_response(status=204)