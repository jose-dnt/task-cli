import sys
import json
from datetime import datetime

try:
    with open("tasks.json", mode="r") as f:
        tasks_list = json.load(f)
except Exception:
    tasks_list = []


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


class Task:
    def __init__(self, description):
        self.id = get_id()
        self.description = description
        self.status = "todo"
        self.created_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.updated_at = self.created_at


def find_task_by_id(id):
    for task in tasks_list:
        if task["id"] == id:
            return task
    else:
        return None


def filter_tasks_by_status(status):
    filtered_tasks = list(filter(lambda task: (task["status"] == status), tasks_list))
    return filtered_tasks

def sort_tasks_by_id(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task["id"])
    return sorted_tasks

def add_task(description):
    task = Task(description)
    tasks_list.append(task.__dict__)
    return task


def update_task(id, description):
    task = find_task_by_id(id)
    if not task:
        return
    task.update_description(description)


def delete_task(id):
    task = find_task_by_id(id)
    tasks_list.remove(task)
    print(tasks_list)


def mark_in_progress(id):
    task = find_task_by_id(id)
    if not task:
        return
    task["status"] = "in-progress"
    task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def mark_done(id):
    task = find_task_by_id(id)
    if not task:
        return
    task["status"] = "done"
    task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def list_tasks(status=None):

    tasks = tasks_list

    if status:
        tasks = filter_tasks_by_status(status.lower())

    sorted_tasks = sort_tasks_by_id(tasks)

    for task in sorted_tasks:
        print(
            f"{'-' * 32}\n"
            f"ID         : {task['id']}\n"
            f"Description: {task['description']}\n"
            f"Status     : {task['status']}\n"
            f"Created at : {task['created_at']}\n"
            f"Updated at : {task['updated_at']}"
            f"{f'\n{"-" * 32}' if sorted_tasks[-1] == task else ''}"
        )


arguments = sys.argv[1:]

if len(arguments) > 0:
    match arguments[0]:
        case "add":
            if len(arguments[1:]) > 0:
                description = " ".join(arguments[1:])
                task = add_task(description)
                print(f"Task added successfully (ID: {task.id})")
        case "update":
            if len(arguments[1:]) > 1:
                id = int(arguments[1])
                description = arguments[2:]
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    update_task(id, description)
        case "delete":
            if len(arguments[1:]) > 0:
                id = int(arguments[1])
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    print("deleted")
                    delete_task(id)
        case "mark-in-progress":
            if len(arguments[1:]) > 0:
                id = int(arguments[1])
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    mark_in_progress(id)
        case "mark-done":
            if len(arguments[1:]) > 0:
                id = int(arguments[1])
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    mark_done(id)
        case "list":
            status = None
            if len(arguments[1:]) > 0:
                status = arguments[1]
            list_tasks(status)

with open("tasks.json", mode="w") as f:
    json.dump(tasks_list, f)
