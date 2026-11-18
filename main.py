"""Console interface for the Student Task Manager."""
from task_manager import TaskManager

DATA_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
"""


def handle_add(manager):
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added task {task.id}: {task.title}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager):
    task_id = int(input("Task id to complete: "))
    task = manager.complete_task(task_id)
    print(f"Task {task.id} marked as completed.")


def handle_delete(manager):
    raw = input("Task id to delete: ").strip()
    if not raw.isdigit():
        print("Error: please enter a valid numeric task id.")
        return
    task_id = int(raw)
    task = manager.find_task(task_id)
    if task is None:
        print(f"Error: No task with id {task_id}.")
        return
    confirm = input(f"Delete '{task.title}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return
    manager.delete_task(task_id)
    print(f"Deleted task {task.id}: {task.title}")


ACTIONS = {
    "1": handle_add,
    "2": handle_display,
    "3": handle_complete,
    "4": handle_delete,
}


def main():
    manager = TaskManager(DATA_FILE)
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
            continue
        action(manager)


if __name__ == "__main__":
    main()
