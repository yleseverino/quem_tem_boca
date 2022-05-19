import psycopg2
import psycopg2.extras
from pydantic import parse_obj_as
from os import environ
import logging
from flask import g

from quemTemBoca.models import Restaurante, Prato, User
from quemTemBoca.s3 import get_restaurant_logo, get_restaurant_background, get_dishe_img

DATABASE_URL = environ.get('DATABASE_URL')
if not DATABASE_URL:
    logging.exception("ENV variable DATABASE not founded")
    exit(1)

def consulta_db(query_string) -> list[Restaurante]:
    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    cur.execute('''
            SELECT  
                    r.id,
                    r.nome,
                    r.descricao,
                    r.pontuacao,
                    r.preco_entrega,
                    r.telefone,
                    r.criado_em

            FROM restaurantes r
            JOIN pratos p ON r.id = p.restaurante_fk
            WHERE UPPER(r.nome) LIKE %s OR UPPER(r.descricao) LIKE %s OR UPPER(p.nome) LIKE %s OR UPPER(p.descricao) LIKE %s
            ORDER BY pontuacao DESC
            ''',('%' + query_string.upper() + '%','%' + query_string.upper() + '%','%' + query_string.upper() + '%','%' + query_string.upper() + '%'))
    restaurantes = cur.fetchall()

    # Add images links from s3
    for restaurant in restaurantes:
        restaurant['logo_url'] = get_restaurant_logo(restaurant['id'])
        restaurant['background_url'] = get_restaurant_background(restaurant['id'])

    parse_obj_as(list[Restaurante], restaurantes)
    cur.close()

    return restaurantes


def autenticate_user(data) -> User:
    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    cur.execute('''
            SELECT  
                    u.id,
                    u.nome,
                    u.email,
                    u.hash_password

            FROM users u
            where email = %s
            ''', (data['email'],))
    user_dict = cur.fetchone()
    cur.close()

    if not user_dict:
        return None

    user = User(**user_dict)

    if user.check_password_hash_user(data['password']):
        return user
    else:
        return None

def get_restaurants() -> list[Restaurante]:

    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    cur.execute('''
            SELECT  
                    r.id,
                    r.nome,
                    r.descricao,
                    r.pontuacao,
                    r.preco_entrega,
                    r.telefone,
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

def get_restaurant(restaurant_id) -> Restaurante:
    'Get restaurant info with its dishes'
    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    cur.execute('''
            SELECT  
                    r.id,
                    r.nome,
                    r.descricao,
                    r.pontuacao,
                    r.preco_entrega,
                    r.criado_em,
                    r.telefone

            FROM restaurantes r
            WHERE r.id = %s
            ORDER BY pontuacao DESC
            ''',(restaurant_id,))
    restaurante = cur.fetchone()
    cur.close()

    restaurante['logo_url'] = get_restaurant_logo(restaurante['id'])
    restaurante['background_url'] = get_restaurant_background(restaurante['id'])

    return Restaurante(**restaurante, pratos = get_dishes(restaurant_id))

def get_dishes(restaurant_id) -> list[Prato]:
    'Get dishes that are sell by a restaurant'
    cur = get_db().cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute('''
            SELECT  
                    r.id,
                    r.nome,
                    r.descricao,
                    r.preco

            FROM pratos r
            where restaurante_fk = %s
            ORDER BY nome
            ''', (restaurant_id, ))
    pratos = cur.fetchall()
    cur.close()

    for prato in pratos:
        prato['img_url'] = get_dishe_img(prato['id'])

    parse_obj_as(list[Prato], pratos)

    return pratos

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
