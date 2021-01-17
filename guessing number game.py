# GUESSING A NUMBER GAME

import random as r

num = r.randrange(100)
guess = 5

print("Guess a number between 1-100")
print("YOU HAVE 6 GUESSES ")
while guess >= 0:
    your_guess=int(input("Enter your guess "))
    def check(x):
        if your_guess==x:
            print("YOU WIN !!! HURREYYY !!!")
        elif your_guess>x:
            print("You are close try a lower number ")
        else:
            print("You are close try a higher number ")
    if guess>1:
        check(num)
    elif guess==1:
        check(num)
        print("This is your last chance make the best of it")
    else:
        print("You Lost")
    guess=guess-1


