import pytest
from src.task_list import TaskList
from src.task import Priority

@pytest.fixture
def task_list():
    tl = TaskList()
    tl.add_task("Task 1", "Description 1", Priority.HIGH)
    tl.add_task("Task 2", "Description 2", Priority.MEDIUM)
    tl.add_task("Task 3", "Description 3", Priority.LOW)
    return tl

def test_add_task(task_list):
    task = task_list.add_task("New Task", "New Description")
    assert task.title == "New Task"
    assert task.description == "New Description"
    assert task.priority == Priority.MEDIUM  # default priority

def test_get_task(task_list):
    task = task_list.get_task(0)
    assert task.title == "Task 1"
    assert task.priority == Priority.HIGH

def test_get_task_out_of_range(task_list):
    task = task_list.get_task(999)
    assert task is None

def test_complete_task(task_list):
    assert task_list.complete_task(0)
    task = task_list.get_task(0)
    assert task.completed
    assert task.completed_at is not None

def test_complete_task_out_of_range(task_list):
    assert not task_list.complete_task(999)

def test_get_incomplete_tasks(task_list):
    task_list.complete_task(0)
    incomplete = task_list.get_incomplete_tasks()
    assert len(incomplete) == 2
    assert all(not task.completed for task in incomplete)

def test_get_completed_tasks(task_list):
    task_list.complete_task(0)
    completed = task_list.get_completed_tasks()
    assert len(completed) == 1
    assert all(task.completed for task in completed)

def test_sort_by_priority(task_list):
    sorted_tasks = task_list.sort_by_priority()
    assert sorted_tasks[0].priority == Priority.HIGH
    assert sorted_tasks[1].priority == Priority.MEDIUM
    assert sorted_tasks[2].priority == Priority.LOW 