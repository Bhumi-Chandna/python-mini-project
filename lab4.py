Lab 4 : Pattern based Questions.
1.	Write a program to print the following pattern:-
Pattern #1: Simple Number Triangle Pattern
Pattern:
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Pattern #2: Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
 2 2 2 2 
  3 3 3 
   4 4 
    5
Pattern #3: Half Pyramid Pattern of Numbers
Pattern:
1 
              1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5
Pattern #4: Inverted Pyramid of Descending Numbers
Pattern:
5 5 5 5 5 
  4 4 4 4 
    3 3 3 
      2 2 
       1
Pattern #5: Inverted Pyramid of the Same Digit
Pattern:
5 5 5 5 5 
  5 5 5 5 
    5 5 5 
     5 5 
      5
Pattern #6: Reverse Pyramid of Numbers
Pattern:
     1 
     2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1
Pattern #7: Inverted Half Pyramid Number Pattern
Pattern:
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Pattern #8: Pyramid of Natural Numbers Less Than 10
Pattern:
1 
2 3 4 
5 6 7 8 9
Pattern #9: Reverse Pattern of Digits from 10 
Pattern:
1
3 2
6 5 4
10 9 8 7
Pattern #10: Unique Pyramid Pattern of Digits
Pattern:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
Pattern #11: Connected Inverted Pyramid Pattern of Numbers
Pattern:
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5 
5 4 3 3 4 5 
5 4 4 5 
5 5
Pattern #12: Even Number Pyramid Pattern
Pattern:
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
Pattern #13: Pyramid of Horizontal Tables
Pattern:
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16  
0 5 10 15 20 25  
0 6 12 18 24 30 36
Pattern #14: Pyramid Pattern of Alternate Numbers
Pattern:
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
Pattern:
           1 
         1 2 
      1 2 3 
   1 2 3 4 
 1 2 3 4 5
Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
Pattern:
            *   
           * *   
          * * *   
         * * * *   
        * * * * *   
       * * * * * *   
      * * * * * * *
Pattern #17: Downward Triangle Pattern of Stars
Pattern:
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Pattern #18: Pyramid Pattern of Stars
Pattern:
* 
* * 
* * * 
* * * * 
* * * * *


Lab 4: String
2.	Write a program to do the following
A. To separate the following string into comma (,) separated values. X= “ India.is.my.country”
B. To remove a given character from a string. Y=”M.A.N.I.P.A.L” 
C. To remove the (.) dots from the above string.
3.	Write a program to sort strings alphabetically in python. 
4.	Take an input from a user as a string then, reverse it.
5.	Write a program to check if a string contains only digits.
6.	Write a program to find the number of vowels in the string.

ANSWERS
# Pattern Programs

# 1. Simple Number Triangle Pattern
for i in range(1, 6):
    print(" ".join([str(i)] * i))

# 2. Inverted Pyramid of Numbers
for i in range(1, 6):
    print(" " * (i - 1) + " ".join([str(i)] * (6 - i)))

# 3. Half Pyramid Pattern of Numbers
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(map(str, range(1, i + 1))))

# 4. Inverted Pyramid of Descending Numbers
for i in range(5, 0, -1):
    print(" " * (5 - i) + " ".join([str(i)] * i))

# 5. Inverted Pyramid of the Same Digit
for i in range(5, 0, -1):
    print(" " * (5 - i) + " ".join(["5"] * i))

# 6. Reverse Pyramid of Numbers
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(map(str, range(i, 0, -1))))

# 7. Inverted Half Pyramid Number Pattern
for i in range(6, 0, -1):
    print(" ".join(map(str, range(i))))

# 8. Pyramid of Natural Numbers Less Than 10
num = 1
for i in range(1, 6, 2):
    print(" ".join(map(str, range(num, num + i))))
    num += i

# 9. Reverse Pattern of Digits from 10
num = 1
for i in range(1, 5):
    print(" ".join(map(str, range(num + i - 1, num - 1, -1))))
    num += i

# 10. Unique Pyramid Pattern of Digits
for i in range(1, 6):
    print(" ".join(map(str, list(range(1, i + 1)) + list(range(i - 1, 0, -1)))))

# 11. Connected Inverted Pyramid Pattern of Numbers
for i in range(5):
    left = list(range(5, i, -1))
    right = list(range(i + 1, 6))
    print(" ".join(map(str, left + right)))

# 12. Even Number Pyramid Pattern
for i in range(1, 6):
    print(" ".join(map(str, range(10, 10 - i * 2, -2))))

# 13. Pyramid of Horizontal Tables
for i in range(7):
    print(" ".join(map(str, [j * i for j in range(i + 1)])))

# 14. Pyramid Pattern of Alternate Numbers
for i in range(1, 6):
    print(" ".join([str(i * 2 - 1)] * i))

# 15. Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
for i in range(1, 6):
    print(" " * (5 - i) * 2 + " ".join(map(str, range(1, i + 1))))

# 16. Equilateral Triangle with Stars (Asterisk Symbol)
for i in range(1, 8):
    print(" " * (7 - i) + " * " * i)

# 17. Downward Triangle Pattern of Stars
for i in range(6, 0, -1):
    print(" " * (6 - i) + " * " * i)

# 18. Pyramid Pattern of Stars
for i in range(1, 6):
    print("* " * i)

# String Programs

# 2.A Separate string into comma-separated values
X = "India.is.my.country"
result_A = X.replace(".", ",")
print("2.A:", result_A)

# 2.B Remove a given character from a string
Y = "M.A.N.I.P.A.L"
result_B = Y.replace(".", "")
print("2.B:", result_B)

# 2.C Remove dots from a string
result_C = X.replace(".", "")
print("2.C:", result_C)

# 3. Sort strings alphabetically
strings = ["banana", "apple", "cherry"]
sorted_strings = sorted(strings)
print("3. Sorted strings:", sorted_strings)

# 4. Reverse a user-input string
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print("4. Reversed string:", reversed_string)

# 5. Check if a string contains only digits
digit_string = input("Enter a string to check digits: ")
is_digit_only = digit_string.isdigit()
print("5. Contains only digits:", is_digit_only)

# 6. Find the number of vowels in the string
text = input("Enter a string: ")
vowels = sum(1 for char in text.lower() if char in 'aeiou')
print("6. Number of vowels:", vowels)