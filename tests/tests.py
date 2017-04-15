import json
import os
import unittest
from json import JSONDecodeError

from shoetracker import shoetracker


class ShoesTestCase(unittest.TestCase):

    def setUp(self):
        shoetracker.app.config['TESTING'] = True
        from shoetracker.shoetracker import db
        db.session.close()
        db.drop_all()
        db.create_all()
        self.app = shoetracker.app.test_client()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        db_loc = shoetracker.app.config['SQLALCHEMY_DATABASE_URI']
        if 'sqlite' in db_loc:
            try:
                os.remove(str(db_loc[10:]))  # slice off sqlite:///
            except OSError:
                print("Unable to remove testDB!")

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

    def test_add_shoe_no_data_returns_400(self):
        # We use data=json.dumps(None) instead of data=None because
        # otherwise we can't distinguish between flask rejecting
        # a malformed request or our code rejecting the malformed
        # request. Though it likely doesn't matter who rejects
        # the request, it's nice to explicitly know it's us.
        response = self.app.post('/shoes', data=json.dumps(None),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_add_shoe_without_name_returns_400(self):
        response = self.app.post('/shoes', data=json.dumps({'id': 1}),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_add_shoe_invalid_content_type_returns_415(self):
        response = self.app.post('/shoes', data=json.dumps(dict(
            name="New Balance")))

        self.assertEqual(response.status_code, 415)

if __name__ == '__main__':
    unittest.main()
