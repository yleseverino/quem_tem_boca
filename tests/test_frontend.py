
import unittest

from dotenv import load_dotenv
load_dotenv()

from quemTemBoca.app import app

class TestFrontENd(unittest.TestCase):

    def test_get_statics_files(self):
        test_client = app.test_client()
        response = test_client.get('/')

        assert b'id="app"' in response.data
