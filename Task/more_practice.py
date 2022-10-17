
# def shopping_items():
#
#     shopping_items_list = {"eggs":1.85,
#                            "bread": 1.50,
#                            "peppers":0.90}
#
#     return shopping_items_list.values()
#
# print(sum(shopping_items()))
# print(shopping_items())
#
#
#
# def shopping_items():
#
#     shopping_items_list = {"eggs":1.85,
#                            "bread": 1.50,
#                            "peppers":0.90}
#
#     return shopping_items_list.items()
#
#
# print(shopping_items())


# def password_length (password):
#
#
#
#     if len(password) < 5:
#         return "Your Password is too short"
#     elif len(password) > 20:
#         return "Your password is too long"
#     else:
#         return "Your pass is an acceptable length"
#
# print(password_length("sdsdddas"))


# create a function called max_profit(data):
# Function should return a list of two ints containing the indicies
# delimiting the range with the max profit

def odd_numbers (a,b):



    for i in range(a,b) :
        if i % 2 != 0:
          print (i, end = " ")

print(odd_numbers(0,100))