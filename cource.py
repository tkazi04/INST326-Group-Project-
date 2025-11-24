from Task import Task
from datetime import datetime

class Course:
    """
    Represents a single course containing multiple tasks/assignments.
    A Course organizes tasks by subject and provides methods to manage them.
    """
    
    def __init__(self, course_name, course_code, instructor=""):
        """
        Initialize a new Course.

        Args:
            course_name: Name of the course (e.g., 'Biology 101').
            course_code: Short code (e.g., 'BIO101').
            instructor: Name of instructor (optional).
        """
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.tasks = [] 
    
    # Task Management 
    def add_task(self, title, due_date):
        """Create and add a new Task to this course."""
        t = Task(title, due_date)
        self.tasks.append(t)
        return t

    def remove_task(self, task_id):
        """Remove a task from this course by ID."""
        for t in self.tasks:
            if t.id == task_id:
                self.tasks.remove(t)
                return True
        return False

    def get_task(self, task_id):
        """Retrieve a Task by its ID."""
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    # Filters
    def get_all_tasks(self):
        """Return all tasks for this course."""
        return list(self.tasks)

    def get_completed_tasks(self):
        """Return only completed tasks."""
        return [t for t in self.tasks if t.completed]

    def get_pending_tasks(self):
        """Return tasks not completed yet."""
        return [t for t in self.tasks if not t.completed]

    def get_overdue_tasks(self, today=None):
        """
        Return all overdue tasks.
        Args:
            today: Optional reference date.
        """
        if isinstance(today, str):
            today = datetime.strptime(today, "%Y-%m-%d")
        today = today or datetime.now()
        return [t for t in self.tasks if (not t.completed and t.due_date < today)]
    
    # Utility
    def __str__(self):
        """Return a readable string representation of the course and its tasks."""
        header = f"{self.course_name} ({self.course_code}) - Instructor: {self.instructor}"
        if not self.tasks:
            return header + "\n  No tasks in this course yet."
        task_list = "\n".join("  " + str(t) for t in self.tasks)
        return header + "\n" + task_list