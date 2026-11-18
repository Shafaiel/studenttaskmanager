"""Core logic for the Student Task Manager."""
from dataclasses import dataclass


@dataclass
class Task:
    """A single student task."""
    id: int
    title: str
    completed: bool = False

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"{self.id:>3}. [{mark}] {self.title}"


class TaskManager:
    """Keeps a list of tasks in memory."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Create a new task and return it."""
        task = Task(id=self.next_id, title=title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """Return all tasks."""
        return list(self.tasks)

    def find_task(self, task_id):
        """Return the task with the given id, or None."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark a task as completed."""
        task = self.find_task(task_id)
        task.completed = True
        return task

    def delete_task(self, task_id):
        """Remove a task from the list."""
        task = self.find_task(task_id)
        self.tasks.remove(task)
        return task
