import sys
from datetime import datetime

tasks_list = []


class Task:
    def __init__(self, description):
        self.id = len(tasks_list) + 1
        self.description = description
        self.status = "todo"
        self.created_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.updated_at = self.created_at

    def update_description(self, description):
        self.description = description
        self.updated_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def update_status(self, status):
        self.status = status
        self.updated_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def find_task_by_id(id):
    for task in tasks_list:
        if task.id == id:
            return task
    else:
        return None


def filter_tasks_by_status(status):
    filtered_tasks = list(filter(lambda task: (task.status == status), tasks_list))
    return filtered_tasks


def add_task(description):
    task = Task(description)
    tasks_list.append(task)
    return task


def update_task(id, description):
    task = find_task_by_id(id)
    if not task:
        return
    task.update_description(description)


def delete_task(id):
    task = find_task_by_id(id)
    tasks_list.remove(task)


def mark_in_progress(id):
    task = find_task_by_id(id)
    if not task:
        return
    task.update_status("in-progress")


def mark_done(id):
    task = find_task_by_id(id)
    if not task:
        return
    task.update_status("done")


def list_tasks(status=None):
    tasks = tasks_list

    if status:
        tasks = filter_tasks_by_status(status.lower())

    for task in tasks:
        print(
            f"{'-' * 32}\n"
            f"ID         : {task.id}\n"
            f"Description: {task.description}\n"
            f"Status     : {task.status}\n"
            f"Created at : {task.created_at}\n"
            f"Updated at : {task.updated_at}"
            f"{f'\n{"-" * 32}' if tasks[-1] == task else ''}"
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
                id = arguments[1]
                description = arguments[2:]
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    update_task(id, description)
        case "delete":
            if len(arguments[1:]) > 0:
                id = arguments[1]
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    delete_task(id)
        case "mark-in-progress":
            if len(arguments[1:]) > 0:
                id = arguments[1]
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    mark_in_progress(id)
        case "mark-done":
            if len(arguments[1:]) > 0:
                id = arguments[1]
                if isinstance(id, int) and id >= 1 and find_task_by_id(id):
                    mark_done(id)
        case "list":
            status = None
            if len(arguments[1:]) > 0:
                status = arguments[1]
            list_tasks(status)
