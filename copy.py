with open('copy.txt') as o:
    s=o.read()

with open("this.txt") as f:
    a=f.read()

if s==a:
    print("the files match")
else:
    print('the files do not match')
