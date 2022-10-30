import random
number = random.randint(1,10)
playerName = input("Please enter your name")
numberOfGuesses = 0
print ("Ok", playerName, "Please guess a number between 1 and 10")
while numberOfGuesses < 5:
    guess = int(input())
    numberOfGuesses += 1
    if guess < number:
        print ("The guess is too low.")
    elif guess > number:
        print ("The guess is too high.")
    elif guess == number:
        break
if guess == number:
    print ("You have guess the number correctly in", str(numberOfGuesses))
else :
    print ("You did not guess it correctly the correst number is", str (number))