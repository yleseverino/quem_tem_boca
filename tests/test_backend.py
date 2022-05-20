
import unittest

from dotenv import load_dotenv
load_dotenv()

from quemTemBoca.app import app

class TestBackEndApi(unittest.TestCase):

    def test_home_api_get_restaurantes(self):
        test_client = app.test_client()
        response = test_client.get('/api')

        assert b'restaurantes' in response.data
    
    def test_get_dishes_from_a_restaurante(self):
        test_client = app.test_client()
        response = test_client.get('/api?restaurant_id=1')

        assert b'pratos' in response.data
    
    def test_consulta_prato_ou_restaurante_na_pesquisa(self):
        test_client = app.test_client()
        response = test_client.get('/api/consulta/misto')

        assert b'brasileira' in response.data
    
    def test_consulta_prato_ou_restaurante_na_pesquisa_em_branco(self):
        test_client = app.test_client()
        response = test_client.get('/api/consulta/')
        
        assert b'brasileira' in response.data
    
    def test_login_jwt_success(self):
        test_client = app.test_client()
        response = test_client.post('/api/login', json= {
                "email":"fred@graodireto.com.br",
                "password":"123Fred"
            })
        
        assert b'"authenticated": true' in response.data
    
    def test_login_jwt_fail(self):
        test_client = app.test_client()
        response = test_client.post('/api/login', json= {
                "email":"HACKER",
                "password":"HACKER"
            })
        
        assert b'"authenticated": false' in response.data

