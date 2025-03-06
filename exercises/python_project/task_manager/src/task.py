from enum import Enum
from datetime import datetime

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, title: str, description: str, priority: Priority = Priority.MEDIUM):
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None

    def complete(self):
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} ({self.priority.name})"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority.name,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        } 