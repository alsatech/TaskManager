from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        Task.objects.create(title="Test Task", description="Test Description")

    def test_task_content(self):
        task = Task.objects.get(id=1)
        expected_title = f'{task.title}'
        expected_description = f'{task.description}'
        self.assertEqual(expected_title, 'Test Task')
        self.assertEqual(expected_description, 'Test Description')
