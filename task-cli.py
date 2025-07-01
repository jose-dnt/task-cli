import sys
from datetime import datetime

tasks = []


class Task:
    def __init__(self, description):
        self.id = len(tasks) + 1
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
    for task in tasks:
        if task.id == id:
            return task
    else:
        return None


def add_task(description):
    task = Task(description)
    tasks.append(task)
    return task


def update_task(id, description):
    task = find_task_by_id(id)
    if not task:
        return
    task.update_description(description)


def delete_task(id):
    task = find_task_by_id(id)
    tasks.remove(task)


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
    for task in tasks:
        if status and task.status != status.lower():
            continue
        print(
            f"{'-' * 32}\n"
            f"ID         : {task.id}\n"
            f"Description: {task.description}\n"
            f"Status     : {task.status}\n"
            f"Created at : {task.created_at}\n"
            f"Updated at : {task.updated_at}\n"
            f"{'-' * 32}\n"
        )
