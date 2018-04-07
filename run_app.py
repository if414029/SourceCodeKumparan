import os

# from api._01_get_topic import app
# from api._02_post_topic import app
# from api._03_put_topic import app
# from api._04_delete_topic import app
from api._01_get_news import app
# from api._02_post_news import app
# from api._03_put_news import app
# from api._04_delete_news import app


if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] = 'kumparan.db'
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)