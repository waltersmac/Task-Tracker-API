import unittest
from core.models import User, Tasks

class TestModels(unittest.TestCase):
    def test_task(self):
        self.assertEqual(Tasks(), None)

    def test_user(self):
        self.assertEqual(User(), None)