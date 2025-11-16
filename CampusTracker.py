class Task:
    """
    Represents a single task or assignment in the Campus Task Organizer.
    """

    def __init__(self, title, due_date, description="", completed=False):
        self.title = title
        self.due_date = due_date  # Example format: 'YYYY-MM-DD'
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def edit_task(self, new_title=None, new_due_date=None, new_description=None):
        """Edit the task details."""
        if new_title:
            self.title = new_title
        if new_due_date:
            self.due_date = new_due_date
        if new_description:
            self.description = new_description

    def is_overdue(self, today):
        """Check if the task is past its due date, given today's date as a string."""
        return today > self.due_date

    def __str__(self):
        """String representation of the task."""
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.title} - Due: {self.due_date} - {status}"
