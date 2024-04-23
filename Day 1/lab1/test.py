''' 1- Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them 

first = input('Enter your first name please \n')
last = input('Enter your last name please \n')
print(last + " " + first)
'''
# *****************************************************************************************
'''
2- Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615

n = int(input('Enter an integer please \n'))
output = (n + int(str(n)*2) + int(str(n)*3)) 
print(output)
'''
# *****************************************************************************************

'''3- Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example'''

"""
print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')
"""
# *****************************************************************************************
# 4- Write a Python program to get the volume of a sphere with radius 6.
# radius = 6
# volume = 4/3 * 3.14 * radius * 3
# print(volume)
# *****************************************************************************************
 
#  5- Write a Python program that will accept the base and height of a triangle and compute
# the area.

# base = int(input('Enter the base \n'))
                 
# height = int(input('Enter the height \n'))
# Area = 1/2 * base * height
# print(Area)

# *****************************************************************************************

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# rows = 5
# for i in range(rows):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# for i in range(rows - 1, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# *****************************************************************************************
# 7- Write a Python program that accepts a word from the user and reverse it.

# word = input('Enter a word please \n')
# reversed_word = word[::-1]
# print(reversed_word)

# *****************************************************************************************

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# i = 0
# for i in range(6):
#         if i != 3 and i !=6:
#          print(i)

# *****************************************************************************************

# 9-Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# a, b = 0, 1
# print(a, end=" ")
# print(b, end=" ")

# while b < 50:
#     a, b = b, a + b
#     if b < 50:
#         print(b, end=" ")

# *****************************************************************************************
#10- write program to calculate digits and letters of an accepted string

# digit_count = 0
# letter_count = 0
# input_string = input('Enter any string \n')
# for char in input_string:
#     if char.isdigit():
#         digit_count += 1

#     elif char.isalpha():
#         letter_count += 1

# print("Number of digits:", digit_count)
# print("Number of letters:", letter_count)