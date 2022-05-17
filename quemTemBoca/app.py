from flask import Flask, request
from quemTemBoca.db import get_restaurants, init_app, get_restaurant

app = Flask(__name__)

init_app(app)

@app.route('/api')
def api():

    restaurant_id = request.args.get('restaurant_id')

    if restaurant_id:
        return get_restaurant(restaurant_id).dict()
    return {'restaurantes': get_restaurants()}