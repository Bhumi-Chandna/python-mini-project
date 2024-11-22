Lab 6: Object-Oriented Programming Concepts
1. Write a program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age. 
2. Create a class named 'Student' with String variable 'name' and integer variable 'roll_no'. Assign the value of roll no as '2' and that of name as "John" by creating an object of the class Student. 
3. Write a program to define a class to represent a bank account, with methods to deposit, withdraw, and check the balance.
4. Write a program to define a class Student with attributes like name and age, and create objects to represent different students.

ANSWERS 
# 1. Create a class called "Person" with name and age attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating two instances of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Printing their name and age
print("Person 1:", person1.name, "-", person1.age)
print("Person 2:", person2.name, "-", person2.age)

# 2. Create a class named 'Student' with variables 'name' and 'roll_no'

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# Creating an object of Student with name "John" and roll_no 2
student = Student("John", 2)
print("Student Name:", student.name)
print("Student Roll Number:", student.roll_no)

# 3. Define a class to represent a bank account with deposit, withdraw, and balance check methods

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

# Creating a BankAccount object and testing its methods
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.check_balance()

# 4. Define a class Student with attributes like name and age, and create objects for different students

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects for different students
student1 = Student("Alice", 21)
student2 = Student("Bob", 22)

# Printing details of the students
print("Student 1:", student1.name, "-", student1.age)
print("Student 2:", student2.name, "-", student2.age)