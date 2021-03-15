# the code uses https://greyli.com/flask-tutorial-chapter-9-test/ as a reference
from app.app import app, db, Todo
from flask import current_app, url_for
from tests import BaseTestCase
import unittest


class AppTestCase(BaseTestCase):
    def setUp(self):
        super(AppTestCase, self).setUp()

        item1 = Todo(text='Item 1', complete=0)
        item2 = Todo(text='Item 2', complete=1)
        item3 = Todo(text='Item 3', complete=2)

        db.session.add_all([item1, item2, item3])
        db.session.commit()

    def test_app_exits(self):
        # check whether the app exists
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        # check whether the status is testing
        self.assertTrue(current_app.config['TESTING'])

    # test the app page
    def test_main_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('My Kanban', data)
        self.assertEqual(response.status_code, 200)

    # test the database
    def test_append_data(self):
        todo = Todo(text='hello', complete=2)
        db.session.add(todo)
        db.session.commit()
        item = Todo.query.filter_by(text='hello').first()
        # test whether the data exists
        self.assertIsNotNone(item)

    # test the addtodo method
    def test_adding_todo(self):
        # test adding todo item
        response = self.client.post('/addtodo', data=dict(Input_todo='test1'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('test1', data)

        # test adding todo item, but input text is null
        response = self.client.post('/addtodo', data=dict(Input_todo=''), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Add something to do!', data)

    # test the adddoing method
    def test_adding_doing(self):
        # test adding doing item
        response = self.client.post('/adddoing', data=dict(Input_doing='test2'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('test2', data)

        # test adding todo item, but input text is null
        response = self.client.post('/adddoing', data=dict(Input_doing=''), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Add something that you are doing!', data)

    # test the adddone method
    def test_adding_done(self):
        # test adding doing item
        response = self.client.post('/adddone', data=dict(Input_done='test3'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('test3', data)

        # test adding todo item, but input text is null
        response = self.client.post('/adddone', data=dict(Input_done=''), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Add something that you have done!', data)

    # test the delete method
    def test_delete(self):
        # test Item 2 was originally on the page
        response1 = self.client.get('/')
        data = response1.get_data(as_text=True)
        self.assertIn('Item 2', data)
        self.assertIsNotNone(Todo.query.filter_by(text='Item 2').first())

        # test Item 2 disappears from the page after del_item method
        response2 = self.client.get(url_for('del_item', id=2), follow_redirects=True)
        data = response2.get_data(as_text=True)
        self.assertNotIn('Item 2', data)
        self.assertIsNone(Todo.query.filter_by(text='Item 2').first())

    # test the complete method
    def test_complete(self):
        # test the original complete status of Item 1 is 0: Todo
        complete_status = Todo.query.filter_by(text='Item 1').first().complete
        self.assertEqual(complete_status, 0)

        # apply the complete method
        self.client.get(url_for('complete', id = 1), follow_redirects=True)

        # test the current complete status of Item 1 is 1: Done
        complete_status = Todo.query.filter_by(text='Item 1').first().complete
        self.assertEqual(complete_status, 1)

        # test the original complete status of Item 3 is 2: Doint
        complete_status = Todo.query.filter_by(text='Item 3').first().complete
        self.assertEqual(complete_status, 2)

        # apply the complete method
        self.client.get(url_for('complete', id = 3), follow_redirects=True)

        # test the current complete status of Item 1 is 1: Done
        complete_status = Todo.query.filter_by(text='Item 3').first().complete
        self.assertEqual(complete_status, 1)

    # test the backtodo method
    def test_backtodo(self):
        # test the original complete status of Item 3 is 0: Done
        complete_status = Todo.query.filter_by(text='Item 2').first().complete
        self.assertEqual(complete_status, 1)

        # apply the backtodo method
        self.client.get(url_for('backtodo', id = 2), follow_redirects=True)

        # test the current complete status of Item 3 is 0: Todo
        complete_status = Todo.query.filter_by(text='Item 2').first().complete
        self.assertEqual(complete_status, 0)

    # test the toding method
    def test_todoing(self):
        # test the original complete status of Item 1 is 0: Todo
        complete_status = Todo.query.filter_by(text='Item 1').first().complete
        self.assertEqual(complete_status, 0)

        # apply the todoing method
        self.client.get(url_for('todoing', id = 1), follow_redirects=True)

        # test the current complete status of Item 1 is 2: Doint
        complete_status = Todo.query.filter_by(text='Item 1').first().complete
        self.assertEqual(complete_status, 2)
