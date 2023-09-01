"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Krafka
email: zdkr@seznam.cz
discord: zdenekkrafka#2447
"""

user = ("bob", "ann", "mike", "liz")
password = ("123", "pass123", "password123", "pass123")
input_user = input("Zadej své jméno:  ")
input_password = input("Zadej své heslo:  ")
code = zip(user, password)
valid_user = []
for customer in code:
    string = "".join(customer)
    valid_user.append(string)

validation = input_user + input_password
if validation in valid_user:
    print(f"""
python projekt1.py \n username: {input_user} \n password: {input_password}\n{"-"*40}
Welcome to the app, {input_user}  \n"We have 3 texts to be analyzed\n{"-"*40}
    """)
else:
    print("unregistered user terminating the program.") 
    exit()

import task_template