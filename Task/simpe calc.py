# define function for multiply
# def multiply(v1,v2):
#     return v1 * v2
# print(multiply(1,2))
#
# #define function for moduls
# def moduls(v1,v2):
#     return v1 % v2
# print(moduls(1,2))
#
# # define function for divide
# def divide(v1,v2):
#     return v1 / v2
# print(divide(1,2))
#
# # ------------------- We can combine them all
#

def multiply(v1,v2):
    return v1 * v2

def moduls(v1,v2):
    return v1 % v2

def divide(v1,v2):
    return v1 / v2

# Gives user options to choose from
print("Select one of the below options")
print("1. Multiply")
print("2. Moduls")
print("3. Divide")

# User inputs decision

user_choice = int(input("Enter choice number (1,2,3): "))

# We create loops with if and elif to excute the users decision

if user_choice == 1 :
    v1 = float(input("First Number: "))
    v2 = float(input("Second Number: "))
    print(multiply(v1,v2))

elif user_choice == 2 :
    v1 = float(input("First Number: "))
    v2 = float(input("Second Number: "))
    print(moduls(v1,v2))

elif user_choice == 3 :
    v1 = float(input("First Number: "))
    v2 = float(input("Second Number: "))
    print(divide(v1, v2))
else:
    print("Invalid choice")




# ------------ OPTIONAL TASK ----------------------
def convert_cm_m(v1):
    return v1 / 100
def conver_m_cm(v1):
    return v1 * 100

# give user options

# allows user to input

# loop
