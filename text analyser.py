"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Krafka
email: zdkr@seznam.cz
discord: zdenekkrafka#2447
"""
#import ...

user = ("bob", "ann", "mike", "liz")
password = ("123", "pass123", "password123", "pass123")
inputu = input("Zadej své jméno:  ")
inputp = input("Zadej své heslo:  ")
code = zip(user, password)

valid_user = []
for customer in code:
    string = "".join(customer)
    valid_user.append(string)

validation = inputu + inputp
if validation in valid_user:
    print(f"""
    python projekt1.py \n username: {inputu} \n password: {inputp}
Welcome to the app, {inputu}  \n"We have 3 texts to be analyzed
    """)
else:
    print("unregistered user terminating the program..")   
    #exit()