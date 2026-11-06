# Task Management System

A command-line task management application developed in Python. The program allows registered users to manage tasks and provides additional options for an administrator to manage users, review completed tasks, and generate summary reports.

This project was created as part of my Python programming practice and demonstrates working with functions, loops, conditional statements, dictionaries, text files, and date handling.

## Features

- **User login:** Checks entered credentials against the records in `user.txt`.
- **Register users (admin):** Adds a new user after checking that the username is available and the passwords match.
- **Add tasks:** Assigns a task to a registered user, with a title, description, assignment date, and due date.
- **View all tasks:** Displays the tasks saved in `tasks.txt`.
- **View my tasks:** Shows tasks assigned to the logged-in user. Users can mark a task as complete or edit its assigned username or due date while it is incomplete.
- **View completed tasks (admin menu):** Displays completed tasks.
- **Delete tasks (admin):** Removes a selected task.
- **Generate reports (admin):** Creates task-level and user-level summary statistics.
- **Display statistics (admin):** Shows the saved reports in the terminal, generating them first if they do not yet exist.

## Project files

| File | Purpose |
| --- | --- |
| `task_manager.py` | Main Python application and menu system. |
| `user.txt` | Usernames and passwords used by the demonstration login system. |
| `tasks.txt` | Stored task details and completion status. |
| `task_overview.txt` | Generated totals and percentages for completed, incomplete, and overdue tasks. |
| `user_overview.txt` | Generated user counts and per-user task statistics. |
| `README.md` | Project information and instructions. |

## Requirements

- Python 3
- No third-party Python packages are required.

## How to run

1. Download or clone the repository.
2. Open the `Task-Management-System` folder in a terminal or in VS Code.
3. Make sure `task_manager.py`, `user.txt`, and `tasks.txt` are in the **same folder**.
4. Make sure `user.txt` contains at least one demonstration account, using the format `username, password` (with a comma followed by a space). For example:

   ```text
   admin, demo_password
   ```

5. Start the application:

   ```bash
   python task_manager.py
   ```

6. Log in with a username and password listed in `user.txt`, then choose a menu option.

> **Note:** The example account above is only a sample. If you use it, add it to your local `user.txt` before running the application. Use fictional credentials only.

## Menu options

| Option | Action |
| --- | --- |
| `r` | Register a new user (admin) |
| `a` | Add a task |
| `va` | View all tasks |
| `vm` | View tasks assigned to the logged-in user |
| `vc` | View completed tasks (admin menu) |
| `del` | Delete a task (admin) |
| `gr` | Generate reports (admin) |
| `ds` | Display statistics (admin) |
| `e` | Exit |

The administrator sees the additional management and reporting options. Other users see the add-task, view-all, view-my-tasks, and exit options.

## Data format

Each record in `tasks.txt` follows this structure:

```text
username, task title, task description, assignment date, due date, completion status
```

For newly added tasks, the program stores the assignment date in `YYYY-MM-DD` format and expects the due date in `DD Mon YYYY` format, such as `25 Oct 2026`. Completion status is stored as `Yes` or `No`.

## Reports

Use `gr` while logged in as `admin` to create or update both reports:

- **`task_overview.txt`:** Total tasks, completed tasks, incomplete tasks, percentage incomplete, overdue incomplete tasks, and percentage overdue.
- **`user_overview.txt`:** Total registered users and tasks, plus each user's assigned-task count and percentages of all tasks, completed tasks, incomplete tasks, and overdue tasks.

Overdue tasks are calculated using the current date. Run `gr` again to refresh the saved report values after changing tasks or as time passes.

## Limitations and possible improvements

This is a learning project rather than a production-ready user management system. Passwords are currently stored in plain text, so **do not use real passwords or upload real account credentials to a public repository**. Use fictional sample data.

Potential improvements include secure password storage, stronger input validation, more consistent access restrictions, and automated tests.
