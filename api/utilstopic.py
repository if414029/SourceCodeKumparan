import os
import uuid

from flask import make_response, g, abort
from .configs import app

JSON_MIME_TYPE = 'application/json'


def get_topics():
    cursor = g.db.execute('SELECT id_topic, topic FROM topic;')
    topics = [{
        'id_topic': row[0],
        'topic': row[1]
    } for row in cursor.fetchall()]

    return topics


def validate_topic(id_topic):
    cursor = g.db.execute(
        "SELECT id_topic, topic FROM topic WHERE id_topic = %i;" % (
        id_topic,))
    topics = [{
        'id_topic': row[0],
        'topic': row[1]
    } for row in cursor.fetchall()]
    if len(topics) == 0:
        return False

    return True

def add_topic(data):
    query = ('INSERT INTO topic ("topic") '
             'VALUES (:topic);')
    params = {
        'topic': data['topic']
    }
    g.db.execute(query, params)
    g.db.commit()


def update_topic(id_topic, data):
    query = (
        'UPDATE topic SET topic = :topic WHERE id_topic = :id_topic;')
    params = {
        'topic': data['topic'],
        'id_topic': id_topic
    }
    g.db.execute(query, params)
    g.db.commit()


def delete_topic(id_topic):
    delete_query = 'DELETE FROM topic WHERE topic.id_topic = :id_topic'
    g.db.execute(delete_query, {'id_topic': id_topic})
    g.db.commit()


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)