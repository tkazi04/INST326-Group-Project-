import pytest
from Task import Task
from Course import Course
from TaskManager import TaskManager

# Task Tests
def test_task_creation_valid():
    t = Task("Homework", "11-05-2025")
    assert t.title == "Homework"
    assert t.due_date.strftime("%m-%d-%Y") == "11-05-2025"
    assert t.completed is False

def test_task_invalid_title():
    with pytest.raises(ValueError):
        Task("", "11-05-2025")

def test_task_invalid_date():
    with pytest.raises(ValueError):
        Task("Homework", "2025/11/05")  # wrong format

def test_task_mark_complete_toggle():
    t = Task("Quiz", "11-05-2025")
    t.mark_complete()
    assert t.completed is True
    t.mark_incomplete()
    assert t.completed is False

def test_task_update_fields():
    t = Task("Old", "11-05-2025")
    t.update_title("New")
    t.update_due_date("12-01-2025")
    assert t.title == "New"
    assert t.due_date.strftime("%m-%d-%Y") == "12-01-2025"

# Course Tests
def test_course_creation():
    c = Course("INST326", "INST326", "Mr. Lou")
    assert c.course_name == "INST326"
    assert c.course_code == "INST326"
    assert c.instructor == "Mr. Lou"
    assert len(c.tasks) == 0

def test_course_add_and_get_task():
    c = Course("Math", "MATH101")
    t = c.add_task("HW1", "11-01-2025")
    fetched = c.get_task(t.id)
    assert fetched is t

def test_course_completed_pending():
    c = Course("BIO101", "BIO101")
    t1 = c.add_task("Lab", "11-05-2025")
    t2 = c.add_task("Read", "11-05-2025")
    t1.mark_complete()
    assert len(c.get_completed_tasks()) == 1
    assert len(c.get_pending_tasks()) == 1

# TaskManager Tests
def test_taskmanager_add_get_task():
    tm = TaskManager()
    t = tm.add_task("Study", "11-05-2025")
    assert tm.get_task(t.id) is t

def test_taskmanager_edit_task():
    tm = TaskManager()
    t = tm.add_task("Project", "11-05-2025")
    tm.edit_task(t.id, title="Final Project", completed=True)
    updated = tm.get_task(t.id)
    assert updated.title == "Final Project"
    assert updated.completed is True

def test_taskmanager_save_load(tmp_path):
    filename = tmp_path / "tasks.json"

    tm = TaskManager()
    tm.add_task("A", "11-05-2025")
    tm.add_task("B", "11-05-2025")
    tm.save(str(filename))

    tm2 = TaskManager()
    assert tm2.load(str(filename)) is True
    assert len(tm2.tasks) == 2
