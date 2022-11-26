you=input('''Welcome to the game 
Choose your answer
Type 
'R' for Rock
'P' for Paper
'S' fpr Sissors
''')
valid_answers=['R','P','S','r','p','s']
Answers_dictionary={
 'S' :'Sissors', 
 's': 'Sissors',
 'R': 'Rock',
 'r':'Rock',
 'p': 'Paper',
 'P': 'Paper'
}
from asyncio import FastChildWatcher
import random
random_integer=random.randint(1,3)
if random_integer==1:
    computer=Answers_dictionary.get('s')
elif random_integer==2:
    computer=Answers_dictionary.get('p')
elif random_integer==3:
    computer=Answers_dictionary.get('r')
a=Answers_dictionary.get(you)
if you in valid_answers:
    def game_of_spr(a,computer):
        if a==computer:
            return None
        elif a==Answers_dictionary.get('R'):
            if computer=='Sissors':
                return True
            elif computer=='Paper':
                return False
        elif a==Answers_dictionary.get('s'):
            if computer=='Rock':
                return False 
            elif computer=='Paper':
                return True
        elif a==Answers_dictionary.get('p'):
            if computer=='Rock':
                return True
            elif computer=='Sissors':
                return False    
    b = game_of_spr(a,computer)
    if b==True:
         print("Congratulations! You've won")
         print(f"conputer chose {computer} whereas you choose {a}")
    elif b==False:
        print("Alas!,You've lost")
        print(f"conputer chose {computer} whereas you choose {a}")
    elif b== None:
        print("The game was a draw")
        print(f"Computer chose {computer} and you also you chose {a}")
else:
    print("Your answer was invalid.")   

                

