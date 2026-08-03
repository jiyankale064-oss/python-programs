import random
number = random.randint(1,5)

guess = int(input("Enter an integer from 1 to 5 : "))

while number != guess:
  if guess < number:
      print("guess is small") 
      guess = int(input("Enter an integer from 1 to 5: "))

  if guess > number:
      print("guess is big")
      guess = int(input("Enter an integer from 1 to 5:"))

print("you guessed it")