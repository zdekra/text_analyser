"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Krafka
email: zdkr@seznam.cz
discord: zdenekkrafka#2447
"""
from task_template import TEXTS

users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

user = input("Zadej uživatelské jméno: ")
user_password = input("Zadej heslo: ")
if user in users:
    index = users.index(user)
    password = passwords[index]

    if user_password == password:
        print(f"""
python projekt1.py \n username: {user} \n password: {password}\n{"-"*40}
Welcome to the app, {user}  \n"We have 3 texts to be analyzed\n{"-"*40}
    """)
    # else:
    #     print("Heslo je nesprávné.")
else:
    print("unregistered user terminating the program.")
    exit()

cislo_textu = input(f"Enter a number btw. 1 and 3 to select:  ")
print("-"*40, "\n")
zadane_cislo = int(cislo_textu) - 1 
jedna = list()
for slovo in ((TEXTS)[zadane_cislo]).split():
    jedna.append(slovo.strip(",.:;"))

# dva = list()
# for slovo in ((TEXTS)[1]).split():
#     dva.append(slovo.strip(",.:;"))

# tri = list()
# for slovo in ((TEXTS)[2]).split():
#     tri.append(slovo.strip(",.:;"))

if cislo_textu == str(cislo_textu):
    numeric_sum = 0 #součet 
    number = 0
    pocet_slov = 0
    capitall = int()
    uppercase = int()
    lowercase = int()
    for item in jedna:
        pocet_slov += 1
    print("There are", pocet_slov, "words in the selected text.")
    for item in jedna:
        if item[0].isupper():
            capitall += 1
    print("There are", capitall, "titlecase words.")
    for item in jedna:
        if item[::].isupper() and item[::].isalpha():
            uppercase += 1
    print("There are", uppercase, "uppecase words.")
    for item in jedna:
        if item[::].islower() and item[::].isalpha():
            lowercase += 1
    print("There are", lowercase, "lowercase words.")
    for item in jedna:
        if item.isnumeric():
            numeric_sum += int(item)
            number += 1
    print("There are",number,"numeric strings.","\n""The sum of all the numbers",numeric_sum,"\n")
    delka_slova = []
    for slovo in jedna:
        delka_slova.append(len(slovo))   
# elif cislo_textu == str(2):
#     numeric_sum = 0
#     number = 0
#     pocet_slov = 0
#     capitall = int()
#     uppercase = int()
#     lowercase = int()
#     for item in dva:
#         pocet_slov += 1
#     print("There are", pocet_slov, "words in the selected text.")
#     for item in jedna:
#         if item[0].isupper():
#             capitall += 1
#     print("There are", capitall, "titlecase words.")
#     for item in jedna:
#         if item[::].isupper() and item[::].isalpha():
#             uppercase += 1
#     print("There are", uppercase, "uppecase words.")
#     for item in jedna:
#         if item[::].islower() and item[::].isalpha:
#             lowercase += 1
#     print("There are", lowercase, "lowercase words.")
#     for item in dva:
#         if item.isnumeric():
#             numeric_sum += int(item)
#             number += 1
#     print("There is",number,"numeric string.","\n""The sum of all the numbers",numeric_sum,"\n")
#     delka_slova = []
#     for slovo in dva:
#         delka_slova.append(len(slovo))
# elif cislo_textu == str(3):
#     numeric_sum = 0
#     number = 0
#     pocet_slov = 0
#     capitall = int()
#     uppercase = int()
#     lowercase = int()
#     for item in tri:
#         pocet_slov += 1
#     print("There are", pocet_slov, "words in the selected text.")
#     for item in tri:
#         if item[0].isupper():
#             capitall += 1
#     print("There are", capitall, "titlecase words.")
#     for item in tri:
#         if item[::].isupper():
#             uppercase += 1
#     print("There are", uppercase, "uppercase words.")
#     for item in tri:
#         if item[::].islower():
#             lowercase += 1
#     print("There are", lowercase, "lowercase words.")
#     for item in tri:
#         if item.isnumeric():
#             numeric_sum += int(item)
#             number += 1
#     print("There are",number,"numeric strings.","\n""The sum of all the numbers",numeric_sum,"\n")
#     delka_slova = []
#     for slovo in tri:
#         delka_slova.append(len(slovo))
else: 
    print("Nezadáno správné číslo textu.")
    exit()
#print(sorted(delka_slova))    (vypočtená délka slov v listu -  převedeno na číselnou hodnotu)
#print((delka_slova))
occurrences = {}
for num in sorted(delka_slova):
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

print("----------------------------------------")
print("  LEN |  OCCURENCES               |NR.")
print("----------------------------------------")   
for num, pocet in occurrences.items():
    if num >= 10:
        print(f"  {num}  |{'*' * pocet}{' ' * (17 - pocet)}{' '}         |{pocet}")
    else:
        print(f"   {num}  |{'*' * pocet}{' ' * (17 - pocet)}          |{pocet}")

print("\n")