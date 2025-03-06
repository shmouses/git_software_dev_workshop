from typing import List, Optional
from .task import Task, Priority

class TaskList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, priority: Priority = Priority.MEDIUM) -> Task:
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def get_task(self, index: int) -> Optional[Task]:
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def complete_task(self, index: int) -> bool:
        task = self.get_task(index)
        if task:
            task.complete()
            return True
        return False

    def get_incomplete_tasks(self) -> List[Task]:
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.completed]

    def sort_by_priority(self) -> List[Task]:
        return sorted(self.tasks, key=lambda x: x.priority.value, reverse=True)

    def __str__(self):
        if not self.tasks:
            return "No tasks"
        return "\n".join(str(task) for task in self.tasks) 