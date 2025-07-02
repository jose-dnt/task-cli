# Simple CLI-based task manager
# Supports adding, updating, listing, deleting, and marking tasks

import sys
import json
from datetime import datetime

# Tries to read the existing tasks from a JSON file, if no such file exists, it creates a new one with an empty list.
try:
    with open("tasks.json", mode="r") as f:
        tasks_list = json.load(f)
except Exception:
    tasks_list = []


class Task:
    def __init__(self, description):
        self.id = get_id()
        self.description = description
        self.status = "todo"
        self.created_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


# ----------------------------- Helper functions -----------------------------


# Generates the lowest possible unique ID for a task higher or equal to 1
def get_id():
    id = 1
    id_is_available = False
    while not id_is_available:
        for task in tasks_list:
            if task["id"] == id:
                break
        else:
            id_is_available = True
            break
        id += 1
    return id


# Returns the ID if it's a valid integer >= 1 and exists in tasks; otherwise returns None.
def validate_id(id):
    try:
        return id if isinstance(id, int) and id >= 1 and find_task_by_id(id) else None
    except Exception:
        return None


def find_task_by_id(id):
    for task in tasks_list:
        if task["id"] == id:
            return task
    else:
        return None


# Returns a filtered list with only the tasks which have that specific status
def filter_tasks_by_status(status):
    filtered_tasks = list(filter(lambda task: (task["status"] == status), tasks_list))
    return filtered_tasks


# Sorts tasks by their id in ascending order
def sort_tasks_by_id(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task["id"])
    return sorted_tasks


# ----------------------------- Task Actions ---------------------------------


def add_task(description):
    task = Task(description).to_dict()
    tasks_list.append(task)
    return task


def update_task(id, description):
    task = find_task_by_id(id)
    if not task:
        return
    task["description"] = description
    task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return task


def delete_task(id):
    task = find_task_by_id(id)
    tasks_list.remove(task)
    return task

def mark_in_progress(id):
    task = find_task_by_id(id)
    if not task:
        return
    task["status"] = "in-progress"
    task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return task


def mark_done(id):
    task = find_task_by_id(id)
    if not task:
        return
    task["status"] = "done"
    task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return task


def list_tasks(status=None):
    tasks = tasks_list

    # If status argument is passed, the code loops through a filtered list instead
    if status:
        tasks = filter_tasks_by_status(status.lower())

    # Before iterating through the tasks, sort the list
    sorted_tasks = sort_tasks_by_id(tasks)

    for task in sorted_tasks:
        print(
            f"{'-' * 32}\n"
            f"ID         : {task['id']}\n"
            f"Description: {task['description']}\n"
            f"Status     : {task['status']}\n"
            f"Created at : {task['created_at']}\n"
            f"Updated at : {task['updated_at']}"
            f"{f'\n{"-" * 32}' if sorted_tasks[-1] == task else ''}"  # If task is the last on its respective list, it prints the end line
        )


# ----------------------------- Main Logic -----------------------------------


def main():
    arguments = sys.argv[1:]

    # If at least one argument is passed
    if len(arguments) > 0:
        # Matches the first argument (task action) to its respective command
        match arguments[0]:
            case "add":
                if len(arguments[1:]) > 0:
                    description = " ".join(arguments[1:])
                    added_task = add_task(description)
                    print(f"Task {added_task['id']} added: {added_task['description']}")
            case "update":
                if len(arguments[1:]) > 1:
                    id = validate_id(int(arguments[1]))
                    description = " ".join(arguments[2:])
                    if id:
                        updated_task = update_task(id, description)
                        print(f"Task {updated_task['id']} updated: {updated_task['description']}")
            case "delete":
                if len(arguments[1:]) > 0:
                    id = validate_id(int(arguments[1]))
                    if id:
                        deleted_task = delete_task(id)
                        print(f"Task {deleted_task['id']} deleted: {deleted_task['description']}")

            case "mark-in-progress":
                if len(arguments[1:]) > 0:
                    id = validate_id(int(arguments[1]))
                    if id:
                        marked_task = mark_in_progress(id)
                        print(
                            f"Task {marked_task['id']} marked as in-progress: {marked_task['description']}"
                        )
            case "mark-done":
                if len(arguments[1:]) > 0:
                    id = validate_id(int(arguments[1]))
                    if id:
                        marked_task = mark_done(id)
                        print(f"Task {marked_task['id']} marked as done: {marked_task['description']}")
            case "list":
                status = None
                if len(arguments[1:]) > 0:
                    status = arguments[1]
                list_tasks(status)

        # Save the current task list to the JSON file
        with open("tasks.json", mode="w") as f:
            json.dump(tasks_list, f, indent=4)


# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
