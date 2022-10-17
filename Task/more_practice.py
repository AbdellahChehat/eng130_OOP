
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


def password_length (password):



    if len(password) < 5:
        return "Your Password is too short"
    elif len(password) > 20:
        return "Your password is too long"
    else:
        return "Your pass is an acceptable length"

print(password_length("sdsdddas"))


