from datetime import datetime

class Task:
    def _init_(self, task, due_date=None, priority="Medium", completed=False):
        self.task = task
        self.due_date = due_date

    def display(self):
        due_date = self.due_date if self.due_date else "No Due Date"
        return f"{self.task} - Due: {due_date}"


class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task = new_task

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.task.lower()]

    def filter_tasks(self, by, value):
        if by == "status":
            return [task for task in self.tasks if task.completed == (value == "completed")]
        elif by == "priority":
            return [task for task in self.tasks if task.priority.lower() == value.lower()]

    def display_tasks(self):
        if not self.tasks:
            print("\nNo tasks available!")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.display()}")


class ToDoApp:
    def _init_(self):
        self.todo_list = ToDoList()

    def display_menu(self):
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Search Tasks")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.todo_list.display_tasks()
                elif choice == 2:
                    task = input("Enter the task: ")
                    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")

                    try:
                        if due_date:
                            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                        else:
                            due_date = None
                    except ValueError:
                        print("Invalid date format! Task will be added without a due date.")
                        due_date = None

                    self.todo_list.add_task(Task(task, due_date))
                    print("Task added successfully!")
                elif choice == 3:
                    self.todo_list.display_tasks()
                    try:
                        index = int(input("Enter the task number to update: ")) - 1
                        new_task = input("Enter the updated task: ")
                        self.todo_list.update_task(index, new_task)
                        print("Task updated successfully!")
                    except ValueError:
                        print("Please enter a valid number!")
                elif choice == 4:
                    self.todo_list.display_tasks()
                    try:
                        index = int(input("Enter the task number to mark as completed: ")) - 1
                        self.todo_list.mark_task_completed(index)
                        print("Task marked as completed!")
                    except ValueError:
                        print("Please enter a valid number!")
                elif choice == 5:
                    self.todo_list.display_tasks()
                    try:
                        index = int(input("Enter the task number to delete: ")) - 1
                        removed_task = self.todo_list.delete_task(index)
                        print(f"Task '{removed_task.task}' deleted successfully!")
                    except ValueError:
                        print("Please enter a valid number!")
                elif choice == 6:
                    keyword = input("Enter keyword to search: ")
                    results = self.todo_list.search_tasks(keyword)
                    if results:
                        print("\n--- Search Results ---")
                        for i, task in enumerate(results, 1):
                            print(f"{i}. {task.display()}")
                    else:
                        print("No tasks found with that keyword!")
                elif choice == 7:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")


if _name_ == "_main_":
    app = ToDoApp()
    app.run()
