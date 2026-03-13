# Console To‑Do List (Python)

I’m building a small beginner-friendly console to‑do list app in Python to practice programming basics (loops, lists/dicts, and input handling).

## What it can do right now

- `add` a task (auto-increments the `id`)
- `list` all tasks
- `incomplete` shows only tasks that are not done yet
- `delete` removes all completed tasks (where `Status == True`)
- `quit` exits the app

## How tasks are stored (in memory)

I store everything in a `tasks` list. Each task is a dictionary with the same keys:

- `id` (number)
- `task` (text)
- `Status` (boolean: `True` = done, `False` = not done)

Example shape (just to understand the structure):

- `tasks = [{"id": 1, "task": "Buy milk", "Status": False}, ...]`

## How to run

1) Make sure Python is installed.
2) Run:

```bash
python todo_list.py
```

## How to use

When the app asks for a command, I type one of these:

- `add` → enter task text → answer `Done? (y/n)`
- `list` → prints all tasks
- `incomplete` → prints only pending tasks
- `delete` → deletes all completed tasks
- `quit` → exits

## What I’m adding next

- Save/load tasks to a JSON file so they persist across runs
- A `complete` command (mark a task done by `id`)
- Better input validation and nicer output

