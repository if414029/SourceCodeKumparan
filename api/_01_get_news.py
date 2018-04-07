import json

from .configs import app
from .utilsnews import get_news, search_news_status, search_news_topic, json_response


@app.route('/newsList')
def news_list():
    news = get_news()

    # check whether the news_search_result is null
    if len(news) == 0:
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    return json_response(json.dumps(news))


@app.route('/newsList/<string:status>')
def news_search_status(status):
    news_search_result = search_news_status(status)

    # check whether the news_search_result is null
    if len(news_search_result) == 0:
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    return json_response(json.dumps(news_search_result))

@app.route('/newsList/<string:topic>')
def news_search_topic(status):
    news_search_result = search_news_topic(status)

    # check whether the news_search_result is null
    if len(news_search_result) == 0:
        error = json.dumps({'error': 'Data not found on storage)'})
        return json_response(error, 404)

    return json_response(json.dumps(news_search_result))