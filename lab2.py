Lab 2: Flow control and Loops 
QUESTIONS
5.	Write a program to Generate Fibonacci Series 
6.	Write a program to Calculate Factorial Using a Loop 
7.	Write a program to check given number is Armstrong number or not.
8.	Write a program to check given number is the perfect number or not.
9.	Write a program to check given number is strong number of not.
10.	Write a program to Print Multiplication Tables 
11.	Write a program to Calculate the LCM and GCD of Two Numbers
ANSWERS
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#6
n = int(input("Enter a number: "))
result = 1
for i in range(1, n + 1):
    result *= i
print("Factorial:", result)
#7
num = int(input("Enter a number: "))
sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
print(f"{num} is an Armstrong number." if sum_of_powers == num else f"{num} is not an Armstrong number.")
#8
num = int(input("Enter a number: "))
sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
print(f"{num} is a perfect number." if sum_of_divisors == num else f"{num} is not a perfect number.")
#9
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
print(f"{num} is a strong number." if sum_of_factorials == num else f"{num} is not a strong number.")
#10
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#11
import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = math.gcd(num1, num2)
lcm = abs(num1 * num2) // gcd

print("GCD:", gcd)
print("LCM:", lcm)