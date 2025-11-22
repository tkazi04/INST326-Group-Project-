import json
from datetime import datetime
from typing import List, Optional
from Task import Task

class TaskManager:
    """
    Manages a collection of Task objects with full CRUD operations,
    search, filtering, sorting, bulk actions, and JSON persistence.

    This class works with the upgraded Task class, which uses UUIDs,
    date validation, and dictionary conversion for saving/loading.
    """

    def __init__(self):
        """Initialize an empty TaskManager with an internal task list."""
        self.tasks: List[Task] = []

    # ---- Core CRUD ----
    def add_task(self, title: str, due_date) -> Task:
        """
        Create a new Task and add it to the manager.

        Args:
            title (str): The task title.
            due_date (str or datetime): Due date in MM-DD-YYYY format or datetime.

        Returns:
            Task: The newly created Task object.
        """
        t = Task(title, due_date)
        self.tasks.append(t)
        return t

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a Task by its unique ID.

        Args:
            task_id (str): UUID of the task.

        Returns:
            Task or None: The matching Task, or None if not found.
        """
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def edit_task(self, task_id: str, title: Optional[str] = None, due_date=None, completed: Optional[bool] = None) -> bool:
        """
        Edit one or more fields of an existing task.

        Args:
            task_id (str): ID of the task to modify.
            title (str, optional): New title.
            due_date (str or datetime, optional): New due date.
            completed (bool, optional): New completion status.

        Returns:
            bool: True if the task was edited, False if task not found.
        """
        task = self.get_task(task_id)
        if not task:
            return False

        if title is not None:
            task.update_title(title)
        if due_date is not None:
            task.update_due_date(due_date)
        if completed is not None:
            task.completed = bool(completed)
        return True

    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task by its ID.

        Args:
            task_id (str): The ID of the task to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                return True
        return False

    def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (str): ID of the task to complete.

        Returns:
            bool: True if completed, False if task not found.
        """
        task = self.get_task(task_id)
        if not task:
            return False
        task.mark_complete()
        return True

    # ---- Querying ----
    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in the title (case‑insensitive).

        Args:
            keyword (str): The text to search for.

        Returns:
            List[Task]: All tasks whose titles contain the keyword.
        """
        if not keyword:
            return []
        needle = keyword.lower()
        return [t for t in self.tasks if needle in t.title.lower()]

    def get_completed(self) -> List[Task]:
        """
        Get a list of all completed tasks.

        Returns:
            List[Task]: Completed tasks.
        """
        return [t for t in self.tasks if t.completed]

    def get_pending(self) -> List[Task]:
        """
        Get all tasks that are not completed.

        Returns:
            List[Task]: Pending tasks.
        """
        return [t for t in self.tasks if not t.completed]

    def tasks_due_on(self, date) -> List[Task]:
        """
        Retrieve tasks due on a specific date.

        Args:
            date (str or datetime): Target date.

        Returns:
            List[Task]: Tasks due on the given date.
        """
        if isinstance(date, str):
            date = datetime.strptime(date, "%m-%d-%Y")
        return [t for t in self.tasks if t.due_date.date() == date.date()]

    def tasks_overdue(self, as_of: Optional[datetime] = None) -> List[Task]:
        """
        Retrieve all overdue tasks.

        Args:
            as_of (datetime, optional): Date to compare against.
                Defaults to now.

        Returns:
            List[Task]: Overdue, not‑completed tasks.
        """
        as_of = as_of or datetime.now()
        return [t for t in self.tasks if (not t.completed) and (t.due_date < as_of)]

    # ---- Sorting ----
    def sort_by_due_date(self, reverse: bool = False) -> List[Task]:
        """
        Sort tasks by due date.

        Args:
            reverse (bool): If True, latest dates first.

        Returns:
            List[Task]: Sorted tasks.
        """
        return sorted(self.tasks, key=lambda t: t.due_date, reverse=reverse)

    def sort_by_title(self) -> List[Task]:
        """
        Sort tasks alphabetically by title.

        Returns:
            List[Task]: Sorted tasks.
        """
        return sorted(self.tasks, key=lambda t: t.title.lower())

    # ---- Bulk operations ----
    def complete_all(self):
        """
        Mark all tasks in the manager as completed.
        """
        for t in self.tasks:
            t.mark_complete()

    def remove_completed(self):
        """
        Remove all completed tasks.
        """
        self.tasks = [t for t in self.tasks if not t.completed]

    # ---- Persistence ----
    def save(self, filename: str = "tasks.json") -> None:
        """
        Save all tasks to a JSON file.

        Args:
            filename (str): File path to write to. Defaults to 'tasks.json'.
        """
        data = [t.to_dict() for t in self.tasks]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filename: str = "tasks.json") -> bool:
        """
        Load tasks from a JSON file.

        Args:
            filename (str): JSON file path.

        Returns:
            bool: True if file loaded successfully, False if not found.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return False

        loaded = []
        for item in data:
            t = Task.from_dict(item)
            loaded.append(t)

        self.tasks = loaded
        return True

    # ---- Utilities ----
    def to_dict(self) -> List[dict]:
        """
        Convert all tasks to a list of dictionaries.

        Returns:
            List[dict]: Serialized tasks.
        """
        return [t.to_dict() for t in self.tasks]

    def __str__(self) -> str:
        """
        Create a clean readable string of all tasks.

        Returns:
            str: Multi‑line list of formatted tasks.
        """
        if not self.tasks:
            return "No tasks available."
        return "\n".join(str(t) for t in self.tasks)
