from curses import cbreak
import random
from re import L
from struct import pack


while True:
    b=input("enter the upper value ").lower()
    if b=="q":
        quit()
    elif b.isdigit():
        b=int(b)
        break
    else:
        print("please enter a valid integer")
a=random.randint(0,b)
tries=1
while True:
    user_guess=input("please enter your guess or 'q' to quit ").lower()
    if user_guess=='q':
        quit()
    elif user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess==a:
            if tries==1:
                print("you have successfully guessed in the first try")
            else:
                print(f"you've successfully guessed in {tries} guesses")
            break
        else:
            tries+=1
            print("Incorrect answer,please try again")
            if user_guess>a:
                print("Please guess a little lower")
            else:
                print('please guess a little higher')
    else:
        print("invalid integer,please try again")

    