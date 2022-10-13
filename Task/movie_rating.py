
# film_rating = input("enter age please: ")
# def movie_rating(age):

print("Please Enter Your Age")
age = int(input())

# if range is equal

def movie_rating(age):
    # Age range between 18 and 117
    if age >= 18 and age <= 117:
        print("You can watch any movie")
# Age equal to 16 and less than 18 can watch these movies
    elif age >= 16 and age < 18:
     print("You can only watch 16 rated and below movies")
    elif age >= 12 and age < 16:
     print("You can only watch 12a movies")

    elif age >= 8 and age < 12:
     print("You can only watch pg movies")
    else:
    #
     print("Sorry, you cannot watch any movies here")

movie_rating(age)