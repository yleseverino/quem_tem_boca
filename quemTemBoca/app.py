from flask import Flask
from models import Restaurante

app = Flask(__name__)

@app.route('/<city_name>')
@app.route('/')
def hello(city_name = None):
        a = Restaurante(nome = 'Nome restaurante', descricao = 'teste descricao', pontuacao = 5)
        return a.dict()
        return 'Olá mundo'