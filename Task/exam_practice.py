
# CREATE A function that returns number of time a letter appears in a string
#
# #
# def letter_a_counter (x):
#     # Number of times i appears in x
#     # i being any character or string
#
#     i = input("Input word or character: ")
#     # Count is function that counts the amount of times
#     number_of_i_in_x = x.count(i)
#
#     return number_of_i_in_x
#
# print(letter_a_counter("apple are very Very very nice"))


# def solution ():


#------------------------  Factorial question



# # To take input from the user
# #num = int(input("Enter a number: "))
#
# def factorial (n):
#
#     # check if the number is negative, positive or zero
#     if n < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#     elif n == 0:
#          print("The factorial of 0 is 1")
#     else:
#         for i in range(1,n + 1):
#             factorial = factorial*i
#         return  "The factorial of",n,"is",factorial
#
# print(factorial(1))
#
#
# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         return 1
#
#     elif x < 1:
#         return "Invalid"
#     else:
#         # recursive call to the function
#         return (x * factorial(x-1))
#
#
# # change the value for a different result
# num = 7
#
# # to take input from the user
# # num = int(input("Enter a number: "))
#
# # call the factorial function
# result = factorial(num)
# print("The factorial of", num, "is", result)


# ---------------
import math
import sys



# starts west travelling towards east
# Can visit country only further away from west
# sort distance
# make a list and append if x +1 is bigger than current x

#
# def max_cities(distances):
#
#
#     cities_visited = [] # List of places jeff visited according to distance
#
#     distances.sort() # Sort distance
#
#     x = min(distances)
#
#     for i in distances:
#         if x < distances [1:]:
#             cities_visited.append(x)
#
#
#     return (cities_visited)
#
# print(max_cities([1,3,3,32]))

# def factorial(n):
#     if n == 0:
#         return 1
#
#     elif n > 0:
#         return n * factorial(n-1)
#
# print(factorial(9))
arr = [1,5,3,8,2]



print(arr)
