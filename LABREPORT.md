# Lab Report - Student Task Manager

- **Repository:** https://github.com/Shafaiel/studenttaskmanager
- **Release:** https://github.com/Shafaiel/studenttaskmanager/releases/tag/v1.0.0
- **Screenshots:** see the [labevidence](labevidence/) folder

## 1. Git vs GitHub, and add / commit / push

**Git** is a version control tool that runs on my own computer. It saves snapshots (commits) of my project so I can see the history and go back if something breaks.
**GitHub** is a website that hosts Git repositories online. It lets me back up my code, share it, and use extra tools like Issues, Pull Requests, Actions and Releases.

- `git add` chooses which changes go into the next commit (puts them in the staging area).
- `git commit` saves those staged changes as a snapshot with a message, on my computer.
- `git push` uploads my new commits to GitHub.

## 2. Branches, Pull Requests and merge conflicts

**Branches** let me build a feature separately without touching `main`. If the feature breaks or is not finished, `main` still works. I used three: `feature/addtask`, `feature/completetask` and `feature/deletetask`.

**Pull Requests** are used to ask for a branch to be merged into `main`. They show the changed files so the code can be reviewed and commented on, and the automated tests run on them before merging. Writing `Closes #1` in a PR also closes the linked Issue when it merges.

A **merge conflict** happens when two branches change the **same line** of the same file from the same starting commit. Git cannot decide which version is correct, so it stops and marks both versions with `<<<<<<<`, `=======` and `>>>>>>>`. I had this in `README.md`, where one branch wrote "In Progress" and the other "Testing". I fixed it by editing the line by hand, removing the markers, then running `git add` and `git commit`.

## 3. fetch vs pull, merge vs rebase

- `git fetch` only **downloads** new commits from GitHub. It does not change my files, so I can look at them first.
- `git pull` is `fetch` **plus merge**. It downloads the commits and adds them to my current branch straight away.

- **Merge** joins two branches with a new merge commit. The history shows exactly what happened, including the branches.
- **Rebase** moves my commits so they sit on top of the latest `main`. The history becomes one straight line, but the commits are rewritten, so you should not rebase commits that others already use.

## 4. How Issues and Actions help a team

**Issues** work like a shared to-do list. Each task or bug gets a description, a label (for example enhancement, bug, documentation) and a person working on it, so the team knows what is planned, who is doing it and what is finished.

**GitHub Actions** runs the tests automatically on every push and Pull Request. Nobody can forget to test, and broken code is caught before it reaches `main`. In this project the first run failed on a wrong assertion, and the next run passed after I fixed it.

## 5. A difficulty and how I solved it

When I tried to push the GitHub Actions workflow file (`.github/workflows/tests.yml`), GitHub rejected it. My login token only had the `repo` permission, and GitHub needs an extra `workflow` permission to change workflow files. I solved it by running `gh auth refresh -h github.com -s workflow`, entering the one-time code in the browser and approving it. After that the push worked and the tests ran on GitHub.

A smaller problem: the first version of the app crashed with `ValueError: list.remove(x): x not in list` when I tried to delete a task id that did not exist. I fixed it in the `feature/deletetask` branch by checking that the id is a number and that the task exists before deleting it.

## Part H checklist

| Requirement | Done |
|---|---|
| At least 12 meaningful commits | Yes, 20+ commits on `main` |
| 3 feature branches | `feature/addtask`, `feature/completetask`, `feature/deletetask` |
| At least 4 Issues | 5 Issues (#1 to #5), all labelled |
| 5 merged Pull Requests | #6, #7, #8, #9 and the PR that added this report |
| 1 resolved conflict | `README.md` project status line |
| 3 automated tests | 5 tests in `tests/test_task_manager.py` |
| 1 workflow | `.github/workflows/tests.yml` |
| 1 release | `v1.0.0` |
