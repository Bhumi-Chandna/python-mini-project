Lab3:
QUESTIONS
1. Write a program program to check if the given number is a Disarium Number (11+ 72 + 53 = 1+ 49 +125 = 175).
2. Write a program to determine whether the given number is a Harshad Number (If a number is
divisible by the sum of its digits, then it will be known as a Harshad Number).
3. Write a program to Print Armstrong Number from 1 to 1000.
4. Write a program to Compute the Value of Xn.
5. Write a program to Calculate the value of nCr.
6. Write a program to count the sum of digits in the entered number.

ANSWERS
#1
num = int(input("Enter a number: "))
sum_of_powers = sum(int(digit) ** (i + 1) for i, digit in enumerate(str(num)))
print(f"{num} is a Disarium number." if sum_of_powers == num else f"{num} is not a Disarium number.")
#2
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print(f"{num} is a Harshad number." if num % sum_of_digits == 0 else f"{num} is not a Harshad number.")
#3
for num in range(1, 1001):
    sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
    if sum_of_powers == num:
        print(num, end=" ")
#4
x = float(input("Enter the base (X): "))
n = int(input("Enter the exponent (n): "))
result = x ** n
print(f"The value of {x}^{n} is {result}")
#5
import math

n = int(input("Enter n: "))
r = int(input("Enter r: "))
nCr = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print(f"{n}C{r} = {nCr}")
#6
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_of_digit