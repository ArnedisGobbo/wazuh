import unittest
from app.tests import BaseTestClass


class TaskTestCase(BaseTestClass):

    def test_get_all_tasks(self):
        res = self.client.get('/api/tasks/')
        self.assertEqual(200, res.status_code)

    def test_get_tasks_by_id(self):
        res = self.client.get('/api/tasks/1')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
