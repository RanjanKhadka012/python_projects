you=input(''' Enter\n
S for Sissors \n
P for Paper\n
R for Rock
''')
my_dict={ 'S':'Sissors',
's':'Sissors',
'R':'Rock',
'r':'Rock',
'P':'Paper',
'p':'Paper'
}
Valid_answers=['S','s','p','r','P','R']
import random
random_integer=random.randint(1,3)
if random_integer==1:
    computer=my_dict.get('S')
elif random_integer==2:
    computer=my_dict.get('P')
elif random_integer==3:
    computer=my_dict.get('R')


if you in Valid_answers:
    def game_of_spr(computer,you):
        if my_dict.get(you)==computer:
            pass
        elif my_dict.get(you)==my_dict.get('S'):
            if computer==my_dict.get('P'):
                return True
            elif computer==my_dict.get('R'):
                return False
        
        elif my_dict.get(you)==my_dict.get('P'):
            if computer==my_dict.get('R'):
                return True
            elif computer==my_dict.get('S'):
                return False
        

        elif my_dict.get(you) ==my_dict.get('R'):
            if computer==my_dict.get('S'):
                return True
            elif computer==my_dict.get('P'):
                return False
    d=game_of_spr(computer,you)
    if d==True:
        print("Congratulations!You have won")
    elif d==False:
        print("Alas!You have lost")
    elif d==None:
        print("The game was a tie")
    print(f"Your move was {my_dict.get(you)} and computer's move was {computer}")
else:
    print("Your input was invalid")