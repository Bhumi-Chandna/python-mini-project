Create a class ComplexNumber that represents a complex number with real and imaginary parts and contain following methods:
1.
A constructor to initialize the complex number.
2.
add(ComplexNumber c): Returns a new ComplexNumber that is the sum of the current object and another complex number.
3.
magnitude(): Returns the magnitude of the complex number.
Write a java program to create two ComplexNumber objects, perform operation, and print the results along with their magnitudes.

ANSWERS
import math

class ComplexNumber:
# 1. Constructor to initialize the complex number
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

# 2. add method to add another complex number and return a new ComplexNumber
    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

# 3. magnitude method to calculate the magnitude of the complex number
    def magnitude(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    # Method to display the complex number in "a + bi" format
    def display(self):
        print(f"{self.real} + {self.imaginary}i")

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print("Complex Number 1:", end=" "); c1.display()
print("Complex Number 2:", end=" "); c2.display()

sum_complex = c1.add(c2)
print("Sum of Complex Numbers:", end=" "); sum_complex.display()

print("Magnitude of Complex Number 1:", c1.magnitude())
print("Magnitude of Complex Number 2:", c2.magnitude())
print("Magnitude of Sum:", sum_complex.magnitude())