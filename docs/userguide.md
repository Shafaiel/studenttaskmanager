# User Guide - Student Task Manager

## Starting the program
Open a terminal in the project folder and run:
```bash
python main.py
```

## Menu
| Option | What it does |
|--------|--------------|
| 1 | Add a task - type a title. Empty titles are not allowed. |
| 2 | Display tasks - shows every task with its id and status. |
| 3 | Complete task - shows pending tasks; type the id of the task you finished. |
| 4 | Delete task - type the task id, then `y` to confirm. |
| 5 | Exit the program. |

## Example
```
Choose an option: 1
Task title: Read chapter 3
Added task 1: Read chapter 3
Choose an option: 3
Pending tasks:
  1. [ ] Read chapter 3
Select task id to complete: 1
Task 1 marked as completed.
```

## Error messages
- `Task title cannot be empty.` - enter some text for the title.
- `No task with id N.` - check the id with option 2.
- `please enter a valid numeric task id.` - ids are whole numbers.

## Where tasks are stored
Tasks are saved in `tasks.json` in the project folder. Delete this file to start fresh.
