# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]

# def reduce_adjacent_elements(nums):
#     if not nums:
#         return []
    
#     result = [nums[0]]  
    
#     for num in nums[1:]:
#         if num != result[-1]: 
#             result.append(num)
    
#     return result

# nums = [1, 1, 1, 2 , 2, 3, 3, 4, 4, 5, 6, 6, 6, 7]
# print(reduce_adjacent_elements(nums)) 
# *******************************************************************************

# 2-
# - Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abcde’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back

# def divide_and_concatenate(a, b):
#     mid_a = (len(a) + 1) // 2  
#     mid_b = (len(b) + 1) // 2 
    
#     a_front, a_back = a[:mid_a], a[mid_a:]
#     b_front, b_back = b[:mid_b], b[mid_b:]
    
#     return a_front + b_front + a_back + b_back

# a = 'abcde'
# b = '12345'
# print(divide_and_concatenate(a, b)) 

# *******************************************************************************

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

# def all_different(sequence):
#     return len(sequence) == len(set(sequence))
# seq1 = [1, 5, 7, 9]
# seq2 = [2, 4, 5, 5, 7, 9]

# print(all_different(seq1)) 
# print(all_different(seq2))  

# *******************************************************************************

# 4- Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)
# def bubble_sort(arr):
#     size_of_array = len(arr)
    
#     for i in range(size_of_array):
#         for j in range(0, size_of_array-i-1):
#             if arr[j] > arr[j+1]:
#              temp = arr[j]  
#              arr[j] = arr[j+1]
#              arr[j+1] = temp

# unordered_list = [64, 49, 25, 12, 43, 50, 100]
# print("Unsorted list:", unordered_list)

# bubble_sort(unordered_list)

# print("Sorted list (Ascendingly):", unordered_list)
    
# *******************************************************************************

# 5- Guessing game !!


# import random

# def guessing_game():

#     random_number = random.randint(1, 100)
#     tries = 10
#     guessed_numbers = set()
    
#     print("Welcome to the Guessing Game!")
#     print("Guess a number between 1 and 100.")
    
#     while tries > 0:
#         guess = input("Enter your guess: ")
        
#         if not guess.isdigit():
#             print("Please enter a valid number.")
#             continue
        
#         guess = int(guess)
        
#         if guess < 1 or guess > 100:
#             print("Your guess is out of range. Please enter a number between 1 and 100.")
#             continue
        
#         if guess in guessed_numbers:
#             print("You've already guessed this number. Try a different one.")
#             continue
        
#         guessed_numbers.add(guess)
        
#         tries -= 1
        
#         if guess < random_number:
#             print("Too low! Try again." "(tries) : " , tries)
            
#         elif guess > random_number:
#             print("Too high! Try again." "(tries) : " , tries)
#         else:
#             print("Congratulations! You guessed the number correctly!")
#             if tries > 0:
#                 print("Let's play again with a new number.")
#                 return True
#             else:
#                 print("You've run out of tries.")
#                 return False
    
#     return False

# while True:
#     if not guessing_game():
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             print("Thank you for playing. Goodbye!")
#             break

   

 
