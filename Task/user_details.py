



def user_details():
    print("Good Morning, Please enter your First Name")
    first_name = input()

    print ("Enter Last Name")
    last_name = input()

    print("Enter DOB (Format ddmmyyyy")
    while True:
        DOB = input()
        if DOB.isdigit() : break
        else: print("Please re enter DOB format ddmmyyyy")

    print("Are you a Uk resident? Answer Yes or No")
    uk_resident = input()

    print("Enter First line of address")
    first_line = input()

    print ("Enter second line of address")
    second_line = input()

    print ("Enter postcode (Format N1 1TB)")
    postcode = input()

    print ("Enter Favourite hobby")
    hobby = input()

    return f'Hello, {first_name.capitalize()} {last_name.capitalize()} Your date of birth is {DOB} and you are {uk_resident} uk resident \nYour address is {first_line} {second_line} {postcode} \n Your favourite hobby is {hobby.lower()}'
    # return f'Your favourite hobby is {hobby.lower()}'

user_details()




# print(f'Hello, {first_name.capitalize()} {last_name.capitalize()} Your date of birth is {DOB} and you are {uk_resident} uk resident')
# print(f'Your address is {first_line} {second_line} {postcode}')
# print(f'Your favourite hobby is {hobby.lower()}')