import math;
import random;

print("Welcome to Number Guessing Game")

lower=int(input("Please enter your Lower range " ))
upper =int(input("Please enter your Upper range "))

x=random.randint(lower,upper)

# print("Random number is " +str(x))

print("Lets play")
print("You have ", round(math.log(upper - lower+1,2)), "guesses")

count=0
while count < math.log(upper - lower+1, 2):
    count = count+1
    guess = int(input("Please enter your guess"))

    if guess == x:
        print("Congratulations, You've won it in ", +count,"tries")
        print(" the Random number is", str(x))
        break
    elif guess > x:
        print("You've guessed it higher")
    elif guess < x:
        print("You've guessed it lower")

if count>=math.log(upper-lower+1,2):
    print("Random number is " +str(x))
    print("Better luck next time")
