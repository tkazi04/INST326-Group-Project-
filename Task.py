class Task:
    """
    Represents a single task and assignment in the Campus Task Organizer.

    Attributes:
        title: The title of the task.
        due_date: The due date in 'MM-DD-YYYY' format.
        description: A short description of the task.
        completed: Whether the task has been completed.
    """

    def __init__(self, title, due_date, description="", completed=False):
        """
        Initialize a new Task with information.

        Args:
            title: The title of the task.
            due_date: Due date in 'MM-DD-YYYY' format.
            description: Optional description of the task.
            completed: Initial completion status (default is False).
        """
        self.title = title
        self.due_date = due_date
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark this task as not completed."""
        self.completed = False

    def toggle_complete(self):
        """Flip the completion status of the task."""
        self.completed = not self.completed

    def edit_title(self, new_title):
        """
        Change the title of the task.

        Args:
            new_title: The new title to use.
        """
        self.title = new_title

    def edit_due_date(self, new_due_date):
        """
        Change the due date of the task.

        Args:
            new_due_date: The new due date in 'YYYY-MM-DD' format.
        """
        self.due_date = new_due_date

    def edit_description(self, new_description):
        """
        Change the description of the task.

        Args:
            new_description: The new description text.
        """
        self.description = new_description

    def is_overdue(self, today):
        """
        Check whether the task is overdue.

        Args:
            today: Today's date in 'YYYY-MM-DD' format.

        Returns:
            bool: True if the task is past its due date, False otherwise.
        """
        return today > self.due_date

    def is_due_on(self, date_str):
        """
        Check whether the task is due on a specific date.

        Args:
            date_str: Date to compare in 'YYYY-MM-DD' format.

        Returns:
            bool: True if the task is due on that date, False otherwise.
        """
        return self.due_date == date_str

    def __str__(self):
        """
        Return a readable string representation of the task.

        Returns:
            str: A formatted string with title, due date, and status.
        """
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.title} - Due: {self.due_date} - {status}"
