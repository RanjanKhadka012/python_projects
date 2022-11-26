with open ("highscore.txt") as f:
    a=f.read()
list=['donkey','monkey','fucker']
for word in list:
    a=a.replace(word,'*****')

    with open ("highscore.txt",'w') as f:
        f.write(a ) 