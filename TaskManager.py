from task import Task  # uses your existing Task class

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, description=""):
        t = Task(title, due_date, description)
        self.tasks.append(t)
        return t

    def find_task(self, title):
        for t in self.tasks:
            if t.title == title:
                return t
        return None

    def mark_complete(self, title):
        t = self.find_task(title)
        if t:
            t.mark_complete()
            return True
        return False

    def edit_task(self, title, new_title=None, new_due_date=None, new_description=None):
        t = self.find_task(title)
        if t:
            t.edit_task(new_title, new_due_date, new_description)
            return True
        return False

    def remove_task(self, title):
        t = self.find_task(title)
        if t:
            self.tasks.remove(t)
            return True
        return False

    def list_tasks(self, only_completed=None):
        if only_completed is None:
            return list(self.tasks)
        return [t for t in self.tasks if t.completed is bool(only_completed)]

    def list_overdue(self, today):
        return [t for t in self.tasks if not t.completed and t.is_overdue(today)]

    def __str__(self):
        if not self.tasks:
            return "No tasks yet."
        lines = []
        for t in self.tasks:
            lines.append(str(t))
        return "\n".join(lines)
