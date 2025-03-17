from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(user=self.user, title="Test Task", description="Testing", completed=False)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {"title": "New Task", "description": "Task desc", "completed": False})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
