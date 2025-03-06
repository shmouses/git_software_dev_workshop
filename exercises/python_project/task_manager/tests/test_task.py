import pytest
from datetime import datetime
from src.task import Task, Priority

def test_task_creation():
    task = Task("Test Task", "Test Description", Priority.HIGH)
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.priority == Priority.HIGH
    assert not task.completed
    assert task.completed_at is None
    assert isinstance(task.created_at, datetime)

def test_task_completion():
    task = Task("Test Task", "Test Description")
    task.complete()
    assert task.completed
    assert isinstance(task.completed_at, datetime)

def test_task_string_representation():
    task = Task("Test Task", "Test Description", Priority.MEDIUM)
    assert str(task) == "[ ] Test Task (MEDIUM)"
    
    task.complete()
    assert str(task) == "[✓] Test Task (MEDIUM)"

def test_task_to_dict():
    task = Task("Test Task", "Test Description", Priority.LOW)
    task_dict = task.to_dict()
    
    assert task_dict["title"] == "Test Task"
    assert task_dict["description"] == "Test Description"
    assert task_dict["priority"] == "LOW"
    assert not task_dict["completed"]
    assert task_dict["completed_at"] is None
    assert isinstance(task_dict["created_at"], str) 