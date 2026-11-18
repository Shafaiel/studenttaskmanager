"""Core logic for the Student Task Manager."""
import json
import os
from dataclasses import asdict, dataclass

MAX_TITLE_LENGTH = 100


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
    """Keeps a list of tasks and optionally saves them to a JSON file."""

    def __init__(self, storage_path=None):
        self.storage_path = storage_path
        self.tasks = []
        self.next_id = 1
        self.load()

    def load(self):
        """Load tasks from the JSON file if it exists."""
        if not self.storage_path or not os.path.exists(self.storage_path):
            return
        with open(self.storage_path, encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task(**item) for item in data.get("tasks", [])]
        self.next_id = data.get("next_id", len(self.tasks) + 1)

    def save(self):
        """Write all tasks to the JSON file."""
        if not self.storage_path:
            return
        data = {"next_id": self.next_id, "tasks": [asdict(t) for t in self.tasks]}
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_task(self, title):
        """Create a new task and return it.

        Raises ValueError if the title is empty, only whitespace,
        or longer than MAX_TITLE_LENGTH characters.
        """
        title = (title or "").strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Task title must be at most {MAX_TITLE_LENGTH} characters.")
        task = Task(id=self.next_id, title=title)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
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
        """Mark the selected task as completed.

        Raises ValueError if no task has this id or it is already completed.
        """
        task = self.find_task(task_id)
        if task is None:
            raise ValueError(f"No task with id {task_id}.")
        if task.completed:
            raise ValueError(f"Task {task_id} is already completed.")
        task.completed = True
        self.save()
        return task

    def delete_task(self, task_id):
        """Remove the task with the given id.

        Raises ValueError if the id is not a valid, existing task id.
        """
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            raise ValueError("Task id must be a whole number.")
        task = self.find_task(task_id)
        if task is None:
            raise ValueError(f"No task with id {task_id}.")
        self.tasks.remove(task)
        self.save()
        return task
