import unittest
from app.tests import BaseTestClass


class TaskTestCase(BaseTestClass):

    def test_get_all_users(self):
        res = self.client.get('/api/users/')
        self.assertEqual(200, res.status_code)

    def test_get_users_by_id(self):
        res = self.client.get('/api/users/1')
        self.assertEqual(200, res.status_code)

    def test_get_user_task(self):
        res = self.client.get('/api/users/1/tasks')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
