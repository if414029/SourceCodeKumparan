import os
import uuid

from PIL import Image
from flask import make_response, g, abort
from .configs import app

JSON_MIME_TYPE = 'application/json'


def get_news():
    cursor = g.db.execute("SELECT id_news, title, content, image, status FROM news WHERE status = 'publish';")
    news = [{
        'id_news': row[0],
        'title': row[1],
        'content': row[2],
        'image': row[3],
        'status': row[4]
    } for row in cursor.fetchall()]

    return news


def search_news_status(status):
    cursor = g.db.execute(
        "SELECT id_news, title, content, image, status FROM news WHERE status LIKE '%s';" % (
        '%' + status + '%',))
    news = [{
        'id_news': row[0],
        'title': row[1],
        'content': row[2],
        'image': row[3],
        'status': row[4]
    } for row in cursor.fetchall()]

    return news

def search_news_topic(topic):
    query = ("SELECT id_topic FROM topic WHERE topic LIKE '%s';" % ('%' + topic + '%',))
    cursor = g.db.execute(query)
    id_topic = cursor.fetchone()[0]

    query2 = ("SELECT id_news FROM news_topic WHERE id_topic = %i;" % (id_topic,))
    cursor2 = g.db.execute(query2)
    id_news = cursor2.fetchone()[0]

    cursor3 = g.db.execute("SELECT * FROM news WHERE id_news = %i;" % (
            id_news,))
    news = [{
        'id_news': row[0],
        'title': row[1],
        'content': row[2],
        'image': row[3],
        'status': row[4]
    } for row in cursor3.fetchall()]

    return news


def validate_news(id_news):
    cursor = g.db.execute(
        "SELECT id_news, title, content, image, status FROM news WHERE id_news = %i;" % (
        id_news,))
    news = [{
        'id_news': row[0],
        'title': row[1],
        'content': row[2],
        'image': row[3],
        'status': row[4]
    } for row in cursor.fetchall()]
    if len(news) == 0:
        return False

    return True


def upload_thumb(data):
    image = Image.open(data['image'])
    filename = os.path.basename(data['image'])
    extension = os.path.splitext(filename)[1]
    new_filename = str(uuid.uuid4()) + extension
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
    image.save(upload_path)

    return upload_path


def add_news(data):
    image_path = upload_thumb(data)

    query = ('INSERT INTO news ("title", "content", "image", "status") '
             'VALUES (:title, :content, :image, :status);')
    params = {
        'title': data['title'],
        'content': data['content'],
        'image': image_path,
        'status': "publish"
    }
    g.db.execute(query, params)

    query3 = ('SELECT id_news FROM news ORDER BY id_news DESC LIMIT 1')
    cursor3 = g.db.execute(query3)
    id_news = cursor3.fetchone()[0]

    topicsplit = data['topic'].split(',')

    for topicData in topicsplit:
        query2 = ("SELECT id_topic FROM topic WHERE topic LIKE '%s';" %('%' + topicData + '%',))
        cursor2 = g.db.execute(query2, params)
        id_topic = cursor2.fetchone()[0]

        query4 = ('INSERT INTO news_topic ("id_news", "id_topic") '
                 'VALUES (:id_news, :id_topic);')

        params4 = {
            'id_news': id_news,
            'id_topic': id_topic
        }
        g.db.execute(query4, params4)

    g.db.commit()


def update_news(id_news, data):
    image_path = upload_thumb(data)

    query = (
        'UPDATE news SET title = :title, content = :content, image = :image WHERE id_news = :id_news;')
    params = {
        'title': data['title'],
        'content': data['content'],
        'image': image_path,
        'id_news': id_news
    }
    g.db.execute(query, params)

    topicsplit = data['topic'].split(',')
    for topicData in topicsplit:
        query2 = ("SELECT id_topic FROM topic WHERE topic LIKE '%s';" %('%' + topicData + '%',))
        cursor2 = g.db.execute(query2, params)
        id_topic = cursor2.fetchone()[0]

        query2 = (
            'UPDATE news_topic SET id_topic = :id_topic WHERE id_news = :id_news;')
        params2 = {
            'id_topic': id_topic,
            'id_news': id_news
        }
        g.db.execute(query2, params2)
    g.db.commit()


def delete_news(id_news):
    query = (
        'UPDATE news SET status = :status WHERE id_news = :id_news;')
    params = {
        'status': "deleted",
        'id_news': id_news
    }
    g.db.execute(query, params)
    g.db.commit()


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)