Question: Create a class Person with attributes name and age, and a method display() that prints the name and age. Then, create a subclass Student that inherits from Person and adds an attribute student_id. Write a method show_details() in Student to print all details, including student_id.
Question: Create a class Vehicle with a method info() that prints "This is a vehicle". Inherit Car from Vehicle and add a method car_info() to print "This is a car". Further, create another subclass ElectricCar that inherits from Car and adds a method battery_info() to print "This car has a battery." Demonstrate how multilevel inheritance works by calling all methods from an ElectricCar object.
Question: Create two classes Teacher and Author, each with their own description() method to describe the profession. Then, create a subclass TutorAuthor that inherits from both Teacher and Author. Use this subclass to call the description() method from each parent class. Use the super() function to resolve any conflicts if necessary.
Question: Create a class Animal with a method sound() that prints "Animals make sound". Then create two subclasses Dog and Cat, each with their own version of sound() method that prints "Dog barks" and "Cat meows" respectively. Demonstrate hierarchical inheritance by calling the sound() method from both Dog and Cat objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def show_details(self):
        self.display()  # Call the display method from the parent class
        print(f"Student ID: {self.student_id}")

# Example usage
student = Student("John Doe", 20, "S12345")
student.show_details()

class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery")

# Example usage
electric_car = ElectricCar()
electric_car.info()           # Method from Vehicle
electric_car.car_info()       # Method from Car
electric_car.battery_info()   # Method from ElectricCar

class Teacher:
    def description(self):
        print("I am a teacher.")

class Author:
    def description(self):
        print("I am an author.")

class TutorAuthor(Teacher, Author):
    def description(self):
        super().description()  # Calls the description method from Teacher first due to method resolution order (MRO)
        print("I am also a tutor and an author.")

# Example usage
tutor_author = TutorAuthor()
tutor_author.description()

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Example usage
dog = Dog()
cat = Cat()

dog.sound()  # Calls the Dog's sound method
cat.sound()  # Calls the Cat's sound method

