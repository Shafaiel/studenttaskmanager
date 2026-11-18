# studenttaskmanager

![Tests](https://github.com/Shafaiel/studenttaskmanager/actions/workflows/tests.yml/badge.svg)

A small Python console application that helps students manage their tasks.

Project status: In Progress (Testing)

## Features
- Add tasks (empty or whitespace-only titles are rejected, max 100 characters)
- Display all tasks with their status (`[ ]` pending, `[x]` completed)
- Mark a selected task as completed
- Delete a task using a valid task id (with confirmation)
- Tasks are saved to `tasks.json` and kept between runs

## Setup
1. Install Python 3.10 or newer.
2. Clone the repository:
   ```bash
   git clone https://github.com/Shafaiel/studenttaskmanager.git
   cd studenttaskmanager
   ```
No extra packages are needed.

## Usage
```bash
python main.py
```
Choose an option from the menu: `1` add, `2` display, `3` complete, `4` delete, `5` exit.
See the [user guide](docs/userguide.md) for details.

## Running the tests
```bash
python -m unittest discover -s tests -v
```
Tests also run automatically with GitHub Actions on every push and pull request to `main`.

## License
MIT - see [LICENSE](LICENSE).
