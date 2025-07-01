from datetime import datetime

tasks = []


class Task:
    def __init__(self, description):
        self.id = len(tasks) + 1
        self.description = description
        self.status = "todo"
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def update_description(self, description):
        self.description = description
        self.updated_at = str(datetime.now())

    def update_status(self, status):
        self.status = status
        self.updated_at = str(datetime.now())
