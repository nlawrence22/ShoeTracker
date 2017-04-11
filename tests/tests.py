import unittest
from shoetracker import shoetracker


class ShoesTestCase(unittest.TestCase):

    def setUp(self):
        shoetracker.app.config['TESTING']=True
        self.app = shoetracker.app.test_client()

    def tearDown(self):
        pass

    def test_helloWorld(self):
        response = self.app.get('/')
        assert b'Hello, World!' in response.data


if __name__ == '__main__':
    unittest.main()
