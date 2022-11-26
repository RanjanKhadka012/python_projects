import random
draw=0
user_wins=0
computer_wins=0
valid=['r','p','s']
while True:
    answer=input(" enter your pic R/P/S or press Q TO quit ").lower()
    if answer=='q':
        break
    if answer not in valid:
        continue

    random_number=random.randint(0,2)
    computer=valid[random_number]

    if answer==computer:
        print("the game was a draw")
        draw=draw+1

    elif answer=="r" and computer=="s":
        print("you won")
        user_wins+=1
    elif answer=="p" and computer=="r":
        print("you won")
        user_wins+=1
    elif answer=="s" and computer=="p":
        print("you won")
        user_wins+=1
    else:
        print("you've lost")
        computer_wins+=1
print(f"You've won {user_wins} ,computer won {computer_wins}  times and the result was a draw {draw} times")