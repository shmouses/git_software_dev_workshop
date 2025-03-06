# Collaborative Python Project Exercise

This is a simple task management application that we'll use to practice Git collaboration. The project will help you learn:
- Branching and merging
- Conflict resolution
- Pull request workflows
- Code review practices
- Git ignore rules
- Rebasing

## Project Structure
```
task_manager/
├── src/
│   ├── __init__.py
│   ├── task.py
│   ├── task_list.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   └── test_task_list.py
├── requirements.txt
└── .gitignore
```

## Getting Started

1. Clone the repository:
```bash
git clone [repository-url]
cd task_manager
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
python -m pytest tests/
```

## Exercise Tasks

### Task 1: Basic Git Operations
1. Create a new branch for your feature
2. Add a new task priority level
3. Update tests
4. Create a pull request

### Task 2: Conflict Resolution
1. Add task categories
2. Resolve merge conflicts with another team member
3. Practice rebasing

### Task 3: Advanced Git Features
1. Use Git hooks for pre-commit testing
2. Implement .gitignore rules
3. Create release tags

## Instructor Notes

### Setup Instructions
1. Create a new repository for this exercise
2. Push the initial code structure
3. Create example branches for demonstration
4. Prepare example conflicts for resolution practice

### Teaching Points
- Demonstrate branching strategies
- Show conflict resolution techniques
- Explain pull request workflow
- Cover Git hooks and automation
- Discuss code review best practices

### Common Issues and Solutions
1. Merge conflicts
2. Branch synchronization
3. Git ignore rules
4. Commit message standards 