from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoModelTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="learn django",
            body="important",
        )

    def test_todo_content(self):
        self.assertEqual(self.todo.title, "learn django")
        self.assertEqual(self.todo.body, "important")
        self.assertEqual(str(self.todo), "learn django")
