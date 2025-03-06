from task_list import TaskList
from task import Priority

def main():
    # Create a task list
    task_list = TaskList()

    # Add some example tasks
    task_list.add_task(
        "Complete Git Workshop",
        "Finish all exercises and submit pull requests",
        Priority.HIGH
    )
    task_list.add_task(
        "Review Code",
        "Review team members' pull requests",
        Priority.MEDIUM
    )
    task_list.add_task(
        "Document Changes",
        "Update documentation with new features",
        Priority.LOW
    )

    # Display all tasks
    print("All Tasks:")
    print(task_list)
    print("\n")

    # Complete a task
    task_list.complete_task(0)
    print("After completing first task:")
    print(task_list)
    print("\n")

    # Display incomplete tasks
    print("Incomplete Tasks:")
    for task in task_list.get_incomplete_tasks():
        print(task)
    print("\n")

    # Display completed tasks
    print("Completed Tasks:")
    for task in task_list.get_completed_tasks():
        print(task)
    print("\n")

    # Display tasks sorted by priority
    print("Tasks Sorted by Priority:")
    for task in task_list.sort_by_priority():
        print(task)

if __name__ == "__main__":
    main() 