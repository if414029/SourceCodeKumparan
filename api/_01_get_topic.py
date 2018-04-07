import json

from .configs import app
from .utilstopic import get_topics, json_response


@app.route('/topics')
def topic_list():
    topics = get_topics()

    # check whether the topic_search_result is null
    if len(topics) == 0:
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    return json_response(json.dumps(topics))
