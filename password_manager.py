
while True:
    master_pwd=input("what's the master password?: ")
    if master_pwd.isdigit():
        master_pwd=int(master_pwd)
        if master_pwd == 1234:
            break
        else :
            print("Incorrect Password")
            continue
    else:
        print("The master password must be a four digit number ")
        
    
def add():
    name=input("account name: ")
    password=input("Whats the password: ")

    with open('password.txt','a') as f:
        f.write(f"Account name = {name} and Password = {password} \n")
        
def view():
     with open('password.txt','r') as f:
        a= f.read()
        print(a)
    
    
while True:
    mode = input("would you like to add a password or add a  new one or quit the program(view,add,quit) ").lower()
    if mode=="quit":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
         