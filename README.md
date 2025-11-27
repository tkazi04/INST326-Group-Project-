<div align="center">
  <strong>INST 326 Group Project </strong>
</div>
<div align="center">
  <strong>Members: Douglas, Rene, Talha, Yozell </strong>
</div>
<div align="center">
  <strong>Project: Campus Task Organizer Description</strong>
</div>
<br> 1: Our Campus Task Organizer is a phyton based program that is designed to help help students track and manage their academic tasks. 
<br> 2: In our program users can add, edit, delete, search, and complete tasks through a simple text-based menu interface.  
All tasks can be saved to and loaded from a JSON file so progress is never lost.

<div align="center">
  <strong>3 Classes: Task, Course, and TaskManager</strong>
</div>
<div align="left">
  <light>1: Task:</light>
</div>
<div align="left">
  <light>2: Course:</light>
</div>
<div align="left">
  <light>3: Task Manager:</light>
</div>
### Task.py

- Defines the `Task` class, which represents a single task or assignment in the Campus Task Organizer.
- Each task stores:
  - `id`: a unique numeric/string identifier for the task
  - `title`: the name of the task
  - `due_date`: the due date stored as a `datetime` object (from a `YYYY-MM-DD` string)
  - `completed`: whether the task is done or still pending
- Validates input when creating or updating tasks:
  - Ensures the title is not empty
  - Ensures the due date is either a valid `YYYY-MM-DD` string or a `datetime` object
- Provides methods to manage tasks, including:
  - `mark_complete()` and `mark_incomplete()` to change completion status
  - `update_title(new_title)` and `update_due_date(new_date)` to edit task details
- Includes a `__str__` method to return a readable string showing the task’s status, title, due date, and ID.
- Implements `to_dict()` and `from_dict()` so tasks can be easily saved to and loaded from JSON files.
