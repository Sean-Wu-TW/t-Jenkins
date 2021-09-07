import unittest
import myFlask
from myFlask import factory
from myFlask.routes import init_app

app = factory.create_app() 
init_app(app)
class TestHello(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/test')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

if __name__ == '__main__':
    unittest.main()