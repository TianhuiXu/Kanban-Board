# the code uses https://greyli.com/flask-tutorial-chapter-9-test/ as a reference
from app.app import app, db
import unittest
from flask import current_app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()

        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def test_app_exits(self):
        # check whether the app exists
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        # check whether the status is testing
        self.assertTrue(current_app.config['TESTING'])
