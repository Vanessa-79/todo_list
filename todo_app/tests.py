from django.test import TestCase
from .models import ToDoItem

#create your tests here
class ToDoTests(TestCase):

    def test_add_todo_item(self):
        response = self.client.post(
            "/add/", {"title": "Test ToDo", "description": "Test Description"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDoItem.objects.count(), 1)
        self.assertEqual(ToDoItem.objects.first().title, "Test ToDo")

    def test_delete_todo_item(self):
        todo_item = ToDoItem.objects.create(
            title="Test ToDo", description="Test Description"
        )
        response = self.client.get(f"/delete/{todo_item.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDoItem.objects.count(), 0)
