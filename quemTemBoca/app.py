from flask import Flask
from quemTemBoca.db import get_restaurants, init_app

app = Flask(__name__)

init_app(app)

@app.route('/')
def hello():
        return {'restaurantes': get_restaurants()}