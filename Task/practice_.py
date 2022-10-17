# def loop_five():
#     for x in range(0, 25):
#         print(x)
#         if x == 5:
#             # Stop function at x == 5
#             return
#     print("This line will not execute.")
#
# loop_five()

import math
import sys



def myFunc(Cities, Distance) :

    myDict = {} # Create a dict to store each city with according distance
    travelledCities = [] # created list to append each new city visited
    currentCity = '' # currentCity

    #Change to dictionary
    for i in range(len(Cities)) :
        myDict[Cities[i] ] = Distance[i]

    # sort a dictionary by distance
    myDict = dict(sorted(myDict.items(), key=lambda item: item[1]))

    for city in myDict:
        if checkLexicography (currentCity, city) :
            travelledCities.append(city)
            currentCity = city
    return(len(travelledCities))

def checkLexicography (city1, city2) :
    return city2 >= city1 # if distance of

print(myFunc(['Tucson','alban','smith','west','berk'],[102,95,114,1421,50]))

# 50 95 102 114 1421
# b a   t   s    w

#
# def soultion (string) :
#
#     new = string.replace(" ", '\n')
#
#
#     return new
# print(soultion('Hello you !'))
#
