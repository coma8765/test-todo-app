import unittest
from app import create_app, db
from app.models import Task


class TaskAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.client.post(
            "/tasks/", json={"title": "Test Task", "description": "Test Description"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_get_tasks(self):
        with self.app.app_context():
            task1 = Task(title='Test Task 1', description='Test Description 1')
            task2 = Task(title='Test Task 2', description='Test Description 2')
            db.session.add(task1)
            db.session.add(task2)
            db.session.commit()

        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

    def test_get_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Test Description')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Test Task')
        self.assertEqual(data['description'], 'Test Description')

    def test_update_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Test Description')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.put(f'/tasks/{task_id}', json={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Updated Task')
        self.assertEqual(data['description'], 'Test Description')

    def test_delete_task(self):
        with self.app.app_context():
            task = Task(title='Test Task', description='Test Description')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
