import json
import unittest
from json import JSONDecodeError

from shoetracker import shoetracker


class ShoesTestCase(unittest.TestCase):

    def setUp(self):
        shoetracker.app.config['TESTING'] = True
        self.app = shoetracker.app.test_client()

    def tearDown(self):
        pass

    def test_helloWorld(self):
        response = self.app.get('/')
        assert b'Hello, World!' in response.data

    def test_add_shoe_returns_200(self):
        response = self.app.post('/shoes', data=json.dumps(dict(
            name="New Balance")), content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_shoe_returns_valid_json(self):
        response = self.app.post('/shoes', data=json.dumps(dict(
            name="New Balance")), content_type='application/json')

        try:
            data = json.loads(response.get_data(as_text=True))
        except JSONDecodeError as error:
            self.fail("Could not decode JSON from response\n")

        self.assertIsNotNone(data)

    def test_add_shoe_returns_id(self):
        response = self.app.post('/shoes', data=json.dumps(dict(
            name="New Balance")), content_type='application/json')

        data = json.loads(response.get_data(as_text=True))

        self.assertIn('id', data)


if __name__ == '__main__':
    unittest.main()
