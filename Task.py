import uuid
from datetime import datetime

class Task:
    """
    Represents a single task with validation, unique IDs, and
    improved formatting. Suitable for use with the upgraded TaskManager.
    """

    def __init__(self, title, due_date, completed=False):
        """Initialize a new Task.

        Args:
            title (str): The title of the task.
            due_date (str or datetime): The due date in MM-DD-YYYY format or a datetime object.
            completed (bool): Whether the task is already completed.

        Raises:
            ValueError: If the title is empty or due_date is an invalid string.
            TypeError: If due_date is not a string or datetime object.
        """
        if not isinstance(title, str) or title.strip() == "":
            raise ValueError("Task title cannot be empty.")

        if isinstance(due_date, str):
            try:
                due_date = datetime.strptime(due_date, "%m-%d-%Y")
            except ValueError:
                raise ValueError("Due date must be in MM-DD-YYYY format.")
        elif not isinstance(due_date, datetime):
            raise TypeError("due_date must be a datetime object or MM-DD-YYYY string.")

        self.id = str(uuid.uuid4())
        self.title = title
        self.due_date = due_date
        self.completed = bool(completed)

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as not completed."""
        self.completed = False

    def update_title(self, new_title):
        """Update the task's title.

        Args:
            new_title (str): The new title for the task.

        Raises:
            ValueError: If the new title is empty.
        """
        if not new_title or not isinstance(new_title, str):
            raise ValueError("Title cannot be empty.")
        self.title = new_title

    def update_due_date(self, new_date):
        """Update the due date of the task.

        Args:
            new_date (str or datetime): New due date.

        Raises:
            ValueError: If new_date is an improperly formatted date string.
        """
        if isinstance(new_date, str):
            try:
                new_date = datetime.strptime(new_date, "%m-%d-%Y") 
            except ValueError:
                raise ValueError("Due date must be in MM-DD-YYYY format.")
        self.due_date = new_date

    def __str__(self):
        """Return a readable string representation of the task.

        Returns:
            str: A formatted description of the task.
        """
        status = "✓ Completed" if self.completed else "✗ Pending"
        return f"[{status}] {self.title} | Due: {self.due_date.strftime('%m-%d-%Y')} | ID: {self.id}"

    def to_dict(self):
        """Convert the task to a dictionary for saving.

        Returns:
            dict: A dictionary representing the task.
        """
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date.strftime('%m-%d-%Y'),
            "completed": self.completed,
        }

    @staticmethod
    def from_dict(data):
        """Reconstruct a Task object from a dictionary.

        Args:
            data (dict): Dictionary containing task fields.

        Returns:
            Task: A reconstructed Task instance.
        """
        task = Task(data["title"], data["due_date"], data["completed"])
        task.id = data["id"]
        return task
