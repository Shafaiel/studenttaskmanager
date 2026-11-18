import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.manager = TaskManager(os.path.join(self.tmp.name, "tasks.json"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Read chapter 3")
        self.assertEqual(task.title, "Read chapter 3")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Finish lab report")
        self.manager.complete_task(task.id)
        self.assertFalse(self.manager.find_task(task.id).completed)  # deliberate mistake

    def test_delete_task(self):
        task = self.manager.add_task("Buy notebook")
        self.manager.delete_task(task.id)
        self.assertEqual(self.manager.list_tasks(), [])

    def test_delete_invalid_id_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)


if __name__ == "__main__":
    unittest.main()
