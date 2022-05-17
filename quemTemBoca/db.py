import psycopg2
import psycopg2.extras
from pydantic import parse_obj_as
from os import environ
import logging
from flask import g

from quemTemBoca.models import Restaurante
from quemTemBoca.s3 import get_restaurant_logo, get_restaurant_background

DATABASE_URL = environ.get('DATABASE_URL')
if not DATABASE_URL:
    logging.exception("ENV variable DATABASE not founded")
    exit(1)


def get_restaurants() -> list[Restaurante]:
    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute('''
            SELECT  
                    r.id,
                    r.nome,
                    r.descricao,
                    r.pontuacao,
                    r.preco_entrega,
                    r.criado_em

            FROM restaurantes r
            ORDER BY pontuacao DESC
            ''')
    restaurantes = cur.fetchall()

    # Add images links from s3
    for restaurant in restaurantes:
        restaurant['logo_url'] = get_restaurant_logo(restaurant['id'])
        restaurant['background_url'] = get_restaurant_background(restaurant['id'])

    parse_obj_as(list[Restaurante], restaurantes)
    cur.close()

    return restaurantes

def init_app(app):
    'Add function close_db to run at the end of the request'
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(DATABASE_URL,)
    return g.db

def close_db(e=None):
    'Close the connection to the db'
    db = g.pop('db', None)
    if db is not None:
        db.close()
