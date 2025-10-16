import random

rand=random.randint(1,100)
print("Welcome to the Guessing Game!")
print("you have 3 chances")
count=3
guess=int(input("Enter your guess (between 1 and 100): "))
while guess!=rand and count>1:
    if guess>rand:
        print("high, think smaller")
    elif guess<rand:
        print("low,think bigger")
    guess=int(input('enter again the number between 1-100'))
    count=count-1
if count>=1 and guess==rand:
    print("congratulations! you guessed it right")
else:
    print("sorry, you are out of chances. The correct number was", rand)
    