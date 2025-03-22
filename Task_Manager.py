from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    description: str
    deadline: str
    priority: int
    completed: bool = False

    def mark_completed(self):
        self.completed = True

    def show_details(self):
        print(f"\nTitle: {self.title}")
        print(f"Description: {self.description}")
        print(f"Deadline: {self.deadline}")
        print(f"Priority: {self.priority}")
        print(f"Completed: {'Yes' if self.completed else 'No'}\n")

@dataclass
class TaskManager:
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, title: str):
        self.tasks = [task for task in self.tasks if task.title != title]

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} | Priority: {task.priority} | Completed: {'Yes' if task.completed else 'No'} | Description : {task.description} ")

    def complete_task(self, title: str):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"\nTask '{title}' marked as completed!\n")
                return
        print("\nTask not found!\n")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            deadline = input("Deadline: ")
            priority = int(input("Priority (1-5): "))
            task = Task(title, description, deadline, priority)
            manager.add_task(task)
            print("\nTask added successfully!\n")

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            title = input("Enter task title to complete: ")
            manager.complete_task(title)

        elif choice == "4":
            title = input("Enter task title to delete: ")
            manager.remove_task(title)
            print("\nTask deleted successfully!\n")

        elif choice == "5":
            print("\nExiting... Goodbye!\n")
            break

        else:
            print("\nInvalid choice! Try again.\n")

if __name__ == "__main__":
    main()
