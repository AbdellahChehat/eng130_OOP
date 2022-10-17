
def shopping_items():

    shopping_items_list = {"eggs":1.85,
                           "bread": 1.50,
                           "peppers":0.90}

    return shopping_items_list.values()

print(sum(shopping_items()))
print(shopping_items())



def shopping_items():

    shopping_items_list = {"eggs":1.85,
                           "bread": 1.50,
                           "peppers":0.90}

    return shopping_items_list.items()


print(shopping_items())