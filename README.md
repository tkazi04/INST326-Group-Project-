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

<div align="center">
  <strong>Task Class Description</strong>
</div>

- Defines the `Task` class, which represents a single task or assignment in the Campus Task Organizer.
- Each task stores:
  - `id`: a unique numeric/string identifier for the task
  - `title`: the name of the task
  - `due_date`: the due date stored as a `datetime` object (from a `MM-DD-YYYY` string)
  - `completed`: whether the task is done or still pending
    
- Validates input when creating and updating tasks:
  - Ensures the title is not empty
  - Ensures the due date is either a valid `MM-DD-YYYY` string or a `datetime` object
    
- Provides methods to manage tasks, including:
  - `mark_complete()` and `mark_incomplete()` to change completion status
  - `update_title(new_title)` and `update_due_date(new_date)` to edit task details
    
- Includes a `__str__` method to return a readable string showing the task’s status, title, due date, and ID.
- Implements `to_dict()` and `from_dict()` so tasks can be easily saved to and loaded from JSON files.

<div align="center">
  <strong>Course Class Description</strong>
</div>

- Defines the `Course` class, which represents a single cource in the Campus Task Organizer.
- Each course stores:
  - `course_name`: the name of the course
  - `course_code`: course code such as "INST326"
  - `instructor`: the name of professor, teacher, etc
  - `tasks`: a list containing Task objects added to the course
 
-Manages tasks within a course by allowing the program to:
  - Add new tasks to the course
  - Retrieve a task using its ID
  - Return all completed tasks
  - Return all pending tasks

Implements simple organization so tasks can be grouped by course when needed.

<div align="center">
<strong>Task Manager Class Description</strong>
</div>

- Defines the `TaskManager` class, which controls all tasks in the Campus Task Organizer. Stores a list of Task objects and manages every core operation in the program.
- Provides system-wide task management, including:
  - `add_task`:
  - `get_task`:
  - `edit_task`:
  - `remove_task`:
  - `complete_task`:
    
- Offers additional features for organizing tasks:
  - `search_task`: by keywords
  - `get_completed` & `get_pending`: for filters
  











