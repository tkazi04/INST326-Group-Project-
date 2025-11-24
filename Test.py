import pytest
from Task import Task
from Course import Course
from TaskManager import TaskManager
from datetime import datetime

# Task Test

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
        Task("Homework", "11-05-2025")

def test_task_mark_complete_toggle():
    t = Task("Quiz", "11-05-2025")
    t.mark_complete()
    assert t.completed is True
    t.mark_incomplete()
    assert t.completed is False

def test_task_update_fields():
    t = Task("Old", "11-05-2025")
    t.update_title("New")
    t.update_due_date("11-05-2025")
    assert t.title == "New"
    assert t.due_date.strftime("%m-%d-%Y") == "11-05-2025"