# Simple CLI Task Manager

A simple, Python-based command-line tool for managing personal tasks.
This project is an implementation of the Task Tracker project from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

---

## Features

- **Add tasks**  
- **Update task descriptions**  
- **Delete tasks**  
- **Mark tasks as in-progress or done**  
- **List tasks**, optionally filtered by status  
- **Persistent storage** in a JSON file

---

## Requirements

- Python 3.10 or higher (for `match-case` syntax)

---

## Usage

Run the script via Python:

    python task.py <command> [arguments]

---

### Available Commands

#### Add a Task

    add <description>

Example:

    python task.py add "Buy groceries"

---

#### Update a Task

    update <id> <new description>

Example:

    python task.py update 2 "Buy groceries and milk"

---

#### Delete a Task

    delete <id>

Example:

    python task.py delete 3

---

#### Mark a Task as In Progress

    mark-in-progress <id>

Example:

    python task.py mark-in-progress 4

---

#### Mark a Task as Done

    mark-done <id>

Example:

    python task.py mark-done 4

---

#### List All Tasks

    list

Example:

    python task.py list

---

#### List By Status

    list <status>

Valid statuses are:

    todo
    in-progress
    done

Example:

    python task.py list done

---

## License

MIT License. Free to use and modify!
