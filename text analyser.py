"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Krafka
email: zdkr@seznam.cz
discord: zdenekkrafka#2447
"""
from task_template import TEXTS



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

cislo_textu = input("zadej číslo textu....")
jedna = ((TEXTS)[0]).split()
dva = ((TEXTS)[1]).split()
tri = ((TEXTS)[2]).split()
if cislo_textu == str(1):
    numeric_sum = 0 #součet 
    number = 0
    pocet_slov = 0
    capitall = int()
    uppercase = int()
    lowercase = int()
    for item in jedna:
        pocet_slov += 1
    print("počet slov v textu", pocet_slov)
    for item in jedna:
        if item[0].isupper():
            capitall += 1
    print("Počet slov s velkým písmenem je: ", capitall)
    for item in jedna:
        if item[::].isupper() and item[::].isalpha():
            uppercase += 1
    print("Slova psaná jen velkými písmeny:  ",uppercase)
    for item in jedna:
        if item[::].islower() and item[::].isalpha:
            lowercase += 1
    print("Slova psaná jen malými písmeny: ",lowercase)
    for item in jedna:
        if item.isnumeric():
            numeric_sum += int(item)
            number += 1
    print("Počet číselných stringů: ",number,"\n""Součet číselných hodnot:",numeric_sum,"\n")
elif cislo_textu == str(2):
    numeric_sum = 0
    number = 0
    pocet_slov = 0
    capitall = int()
    uppercase = int()
    lowercase = int()
    for item in dva:
        pocet_slov += 1
    print("počet slov v textu", pocet_slov)
    for item in dva:
        if item[::].isupper():
            uppercase += 1
    print("Slova psaná jen velkými písmeny: ",uppercase)
    for item in dva:
        if item[::].islower():
            lowercase += 1
    print("Slova psaná jen malými písmeny: ",lowercase)
    print("Počet slov s velkým písmenem je: ", capitall)
    for item in dva:
        if item.isnumeric():
            numeric_sum += int(item)
            number += 1
    print("Počet číselných stringů: ",number,"\n""Součet číselných hodnot:",numeric_sum,"\n")
elif cislo_textu == str(3):
    numeric_sum = 0
    number = 0
    pocet_slov = 0
    capitall = int()
    uppercase = int()
    lowercase = int()
    for item in tri:
        pocet_slov += 1
    print("počet slov v textu", pocet_slov)
    for item in tri:
        if item[0].isupper():
            capitall += 1
    print("Počet slov s velkým písmenem je: ", capitall)
    for item in tri:
        if item[::].isupper():
            uppercase += 1
    print("Slova psaná jen velkými písmeny: ",uppercase)
    for item in tri:
        if item[::].islower():
            lowercase += 1
    print("Slova psaná jen malými písmeny: ",lowercase)
    for item in tri:
        if item.isnumeric():
            numeric_sum += int(item)
            number += 1
    print("Počet číselných stringů:",number,"\n""Součet číselných hodnot:",numeric_sum,"\n")
else: 
    print("Nezadáno správné číslo textu.")

    