# Python Object Oriented Programming 

## What is OOP ?
 - Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic
 - Programming language odel for software development
 - Focuses on what developer want to manipulate rather than how.

## 4 Pillars of OOP

 - Four pillars are basically the software design principles that help you to write clean Object-Oriented Code and these are:
1. Abstraction.
2. Encapsulation.
3. Inheritance.
4. Polymorphism.

##  Advantages and Disadvantages 

![](/Users/faduma/Desktop/Screenshot 2022-10-13 at 15.21.02.png)

## Functionality of each pillar

1. Abstraction. = 
2. Encapsulation. =
3. Inheritance. = 
4. Polymorphism. = 

### Methods/ Function
### Modules 
####

#### Use case - benefits - examples of builtin 


### Importance of imports

-  Imports in Python are important for structuring your code effectively
- example By importing random you're able to make use of all the functions in the random library 


### Defining Functions in python 

- Examples of functions taking in different type of arugments 

```` python
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
def my_function( child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
````
### Return statements 

```` python

# If you are using a return statement and calling the fucntion you must have a print statement

def add(v1,v2):

    return v1 + v2
print(add(2,2))

````