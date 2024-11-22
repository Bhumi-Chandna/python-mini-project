QUESTIONS
WAP to find a number is Prime or not.
2.	WAP to find the given number is palindrome or not.
3.	WAP to find the grade of student using given percentage
4.	WAP to create a simple console base calculator
ANSWERS
#1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#2 
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#3
def find_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

percentage = float(input("Enter the percentage: "))
grade = find_grade(percentage)
print(f"Grade: {grade}")

#4
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(num1, num2, operator)
print(f"Result: {result}")