LAB 5
1. Write a Python program to triple all numbers in a given list of integers. Use Python map. 
2. Write a Python program to add three given lists using Python map and lambda. 
3. Write a Python program to listify the list of given strings individually using Python map. 
4. Write a Python program to create a list containing the power of said number in bases raised to 
the corresponding number in the index using Python map. 
5. Write a Python program to square the elements of a list using the map() function. 
6. Write a Python program to convert all the characters into uppercase and lowercase and 
eliminate duplicate letters from a given sequence. Use the map() function. 
7. Write a Python program to add two given lists and find the di erence between them. Use the 
map() function. 
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of 
strings. 
9. Write a Python program to create a new list taking specific elements from a tuple and convert 
a string value to an integer. 
10. Write a Python program to compute the square of the first N Fibonacci numbers, using the 
map function and generate a list of the numbers. 
11. Write a Python program to compute the sum of elements of an array of integers. Use the 
map() function.

ANSWERS
#1
numbers = [1, 2, 3, 4, 5]
tripled = list(map(lambda x: x * 3, numbers))
print("Tripled list:", tripled)
#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
summed_lists = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print("Summed lists:", summed_lists)
#3
strings = ["hello", "world", "python"]
listified_strings = list(map(list, strings))
print("Listified strings:", listified_strings)
#4
numbers = [2, 3, 4, 5]
powered = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))
print("List with powers:", powered)
#5
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared list:", squared)
#6
sequence = "HelloWorld"
unique_chars = "".join(set(sequence))
upper_lower = list(map(lambda x: (x.upper(), x.lower()), unique_chars))
print("Uppercase and lowercase:", upper_lower)
#7
list1 = [10, 20, 30]
list2 = [5, 15, 25]
added = list(map(lambda x, y: x + y, list1, list2))
difference = list(map(lambda x, y: x - y, list1, list2))
print("Added:", added)
print("Difference:", difference)
#8
int_list = [1, 2, 3, 4]
int_tuple = (5, 6, 7, 8)
str_list = list(map(str, int_list))
str_tuple = list(map(str, int_tuple))
print("List of strings:", str_list)
print("Tuple of strings:", str_tuple)
#9
sample_tuple = ("10", "20", "30", "40")
converted = list(map(int, sample_tuple[1:3]))  # Take specific elements and convert to int
print("Converted list:", converted)
#10
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

N = 5
squared_fib = list(map(lambda x: x ** 2, fibonacci(N)))
print("Squared Fibonacci numbers:", squared_fib)
#11
array = [1, 2, 3, 4, 5]
sum_of_elements = sum(map(int, array))
print("Sum of elements:", sum_of_elements)