print('Welcome to the quiz')
score=0
playing = input("would you like to play? y/n ")
if playing.lower()!= "y":
    quit()

print('lets play')

answer= input("what is the full form of CPU? " )
if answer.lower()=="central processing unit":
    print('correct!')
    score+=1
else:
    print('Incorrect!')

answer=input("what dies GPU stand for? ").lower()
if answer=='graphics processing unit':
    print('correct')
    score+=1
else:
    print('Incorrect')

answer=input("what does VDU stand for? ").lower()
if answer.lower()=='Visual Display Unit':
    print('correct')
    score+=1
else:
    print('Incorrect')

answer=input("what dies FPS stand for? ").lower()
if answer.lower()=='frames per second':
    print('correct')
    score+=1
else:
    print('Incorrect')
print(f'you got {score} questions correct')


