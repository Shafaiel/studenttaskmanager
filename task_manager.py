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
