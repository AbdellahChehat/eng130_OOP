#return smallest interval between 2 numbers
#must be positive
# max range 100,000 of entries
#



def find_smallest_interval(numbers):

    list_of_numbers =[]

    for x in numbers:
        if x >= 0:
            list_of_numbers.append(x)
            list_of_numbers.sort()

    return list_of_numbers




print(find_smallest_interval([-1,2,4,2,45,34]))




