from os import environ
from flask import Flask, request
from datetime import datetime, timedelta
import jwt

from quemTemBoca.db import get_restaurants, init_app, get_restaurant, autenticate_user, consulta_db


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('TOKEN_SECRET', 'utf-8')

init_app(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api')
def api():
    restaurant_id = request.args.get('restaurant_id')
    if restaurant_id:
        return get_restaurant(restaurant_id).dict()
    return {'restaurantes': get_restaurants()}

@app.route('/api/login', methods=('POST',))
def login_api():
    data = request.get_json()
    user = autenticate_user(data)

    if not user:
        return { 'message': 'Invalid credentials', 'authenticated': False }, 401
    
    token = jwt.encode({
        'nome': user.nome,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        app.config['SECRET_KEY'])

    return { 'authenticated': True,'JWT': token }

@app.route('/api/consulta/<query_string>')
@app.route('/api/consulta/')
def consulta(query_string = None):

    if not query_string:
        return api()

    return {'restaurantes': consulta_db(query_string)}