import json

from .configs import app
from .utilstopic import delete_topic, validate_topic, json_response


@app.route('/topic-delete/<int:id_topic>', methods=['DELETE'])
def topic_delete(id_topic):
    # check whether the topic with id_topic is valid
    if not validate_topic(id_topic):
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    delete_topic(id_topic)

    return json_response(status=204)