
def fizz_buzz_(x):
#for-in loop that traverses numbers from 1 to 100
  for number in range(1, x):
  #Check that number is divisible by both 3 / 5
    if number%3==0 and number%5==0:
      print ("FizzBuzz")

  #Check that number is divisible by 5
    elif number%5 == 0:
      print("Buzz")

# checking that number is divisible by 3
    elif number % 3 == 0:
     print("Fizz")
  #And if not divisible by either of them print num as it is
    else:
     print(number)

fizz_buzz_(100)
