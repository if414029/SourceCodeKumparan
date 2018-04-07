import json

from .configs import app
from .utilsnews import delete_news, validate_news, json_response


@app.route('/news-delete/<int:id_news>', methods=['DELETE'])
def news_delete(id_news):
    # check whether the news with id_news is valid
    if not validate_news(id_news):
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    delete_news(id_news)

    return json_response(status=204)