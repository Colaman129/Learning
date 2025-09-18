import random
import string



def generate_password(min_Lengt, Numbers = True, Special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if Numbers:
        characters += digits
    if Special_characters:
        characters += special
    
    password = ""
    has_number = False
    has_special = False
    meets_condition = False

    while not meets_condition or len(password) < min_Lengt:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        if new_character in special:
            has_special = True

        meets_condition = True
        if Numbers:
            meets_condition = has_number
        if Special_characters:
            meets_condition = has_special and meets_condition
    
    return password
def askForInfo():
    while True:
        psw_len = input("How long should the password be?: ")
        if psw_len.isdigit():
            psw_len = int(psw_len)
            break
        else:
            print("Try again")
    while True:
        psw_Numbers = input("Do You want to include numbers  (Yes/No): ")
        if psw_Numbers.lower() == "yes":
            psw_Numbers = True
            break
        elif psw_Numbers.lower() == "no":
            psw_Numbers = False
            break
        else:
            print("Try again")
    while True:
        psw_special = input("Do You want to special characters  (Yes/No): ")
        if psw_special.lower() == "yes":
            psw_special = True
            break
        elif psw_special.lower() == "no":
            psw_special = False
            break
        else:
            print("Try again")
    return psw_len, psw_special, psw_Numbers

def mainLoop():
    psw_len, psw_special, psw_Numbers = askForInfo()
    password = generate_password(psw_len, psw_Numbers, psw_special)
    print(password)

    while True:
        new_password = input("Do you want a new password?: ")
        if new_password.lower() == "yes":
            mainLoop()
        elif new_password.lower() == "no":
            break
        else:
            print("Try again")
mainLoop()