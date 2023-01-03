import unittest
from core.crud import get_user_by_email, create_user, get_users, get_user, create_user_task, get_tasks

class TestCrud(unittest.TestCase):
    def test_create_user(self):
        self.assertEqual(create_user(), None)

    def test_get_users(self):
        self.assertEqual(get_users(), None)

    def test_get_user(self):
        self.assertEqual(get_user(), None)

    def test_get_user_by_email(self):
        self.assertEqual(get_user_by_email(), None)

    def test_create_user_task(self):
        self.assertEqual(create_user_task(), None)

    def test_get_tasks(self):
        self.assertEqual(get_tasks(), None)
