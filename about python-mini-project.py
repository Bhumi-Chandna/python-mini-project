Objective:
The objective of this project is to develop a simple To-Do List application that helps users efficiently manage and organize their daily tasks. The application enables users to add, update, delete, search, and filter tasks while tracking due dates.

Description:
This Python-based To-Do List application is designed to provide a structured and user-friendly way to manage tasks. Built with object-oriented principles, the application allows users to store tasks with optional due dates. It features an intuitive text-based menu, allowing users to perform common task management operations, such as adding tasks, searching by keywords, or marking tasks as completed. The program ensures data integrity by validating inputs (e.g., dates) and offers flexibility with features like task updates. Each task can include a description and an optional due date, allowing users to prioritize and manage their schedules effectively. The inclusion of Object-Oriented Programming (OOP) principles ensures the application is modular, scalable, and easy to maintain. It is designed with a user-friendly menu-driven interface that simplifies navigation and ensures all features are easily accessible. This project not only addresses personal productivity needs but also serves as an excellent learning tool for programmers exploring OOP concepts.

Key Features:
Task Management: Add, update, and delete tasks.
Add tasks with descriptions and optional due dates.
Edit task descriptions or update existing ones.
Mark tasks as completed or delete them.
Due Date Tracking: Optional due dates for tasks. Display tasks clearly, showing the task description and due date.
Search Functionality: Locate tasks using keywords.
Object-Oriented Design: Implements Task and ToDoList classes for maintainable code.
Text-Based Menu: Simple navigation for all operations.
Search tasks by specific keywords.
Filter tasks based on criteria like completion status.
Exit the program safely without losing data during runtime.

Concepts Used:
Object-Oriented Programming (OOP): Encapsulation through Task and ToDoList classes.
Input Validation: Error handling for incorrect date formats.
Loops and Conditionals: Efficiently manage menu navigation.
List Manipulation: Dynamic task storage and processing.

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