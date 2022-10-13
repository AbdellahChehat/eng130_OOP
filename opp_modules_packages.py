# Lucky draw
# Key word called import
# Import random
import sys
# print(random)
#
# print(random.random()) #Each time it's run it generates a random number


# Calculate DOB or year of birth

from random import *
import math # compute any number - e.g round the figure up
from datetime import *
import sys
import os

# number = 23.66
# print(math.ceil(number)) #round up by using the method .ceil from the math import
# print(math.floor(number)) #round down by using the method .floor from the math import

# print(os.cpu_count()) #this will result in number cpu based your OS
# print(date.today()) # This will result in prinitng todays date based on your OS
# print(sys.path)


# Don't repeat yourself  - reusable
# Lets build some functions
# Let's build a function - SYNTAX def name(): - e.g def calc():

# How to build a function (STEP 1)

def greeting():
    print("Hello bob")
greeting()


# Create a function that take an arg - the name

def greet_user(firstname):
    print(f'Hello {firstname.capitalize()} how are you')
greet_user("abdellah")


# This time you do not know how many arg will be passed so we use * so that we can receive a tuple
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# This function we can pass arguments with the key = value syntax.
def my_function1( child3, child2, child1):
  print("The youngest child is " + child3)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#-----------------------------


# return statement

# If you are using a return statement and calling the fucntion you must have a print statement

def add(v1,v2):

    return v1 + v2
print(add(2,2))


# ------------------ Passing list as an arguement

def function_food(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)