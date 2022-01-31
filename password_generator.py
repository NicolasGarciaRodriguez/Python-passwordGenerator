import os
import random as rd

savedpasswords = []


def show_password(password):
    print("\n\n\nYour random password: {}\n\n\n".format(password))

def password_generator():

    letters = "abcdefghijklmnopqrstuvwxyxABCDEFGHYJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!$%&/()@#€"

    posible_characters = f"{letters}{numbers}{symbols}"

    password = "".join(rd.sample(posible_characters, 15))

    show_password(password)
    save_password(password)

def save_password(password):
    savepassword = None
    save_title = None
    title = None
    while savepassword != "Y" and savepassword != "N":
        savepassword = input("\n\n\nDo you want to save your password? (Y/N)\n\n\n"
                             "Respuesta: ")
    if savepassword != "Y":
        os.system("cls")
        main()
    while save_title != "Y" and save_title != "N":
        os.system("cls")
        save_title = input("\n\n\nDo you want to add a title? (Y/N)\n\n\n"
                           "Respuesta: ")
    if save_title != "Y":
        os.system("cls")
        savedpasswords.append(password)
        print("\n\n\nSaved passwords: {}\n\n\n".format(savedpasswords))
        input("Enter to go back...")
        os.system("cls")
        main()
    os.system("cls")
    title = input("\n\n\nEnter your title...\n\n\n"
                  "Respuesta: ")
    savedpasswords.append(title + ": " + password)
    print ("\n\n\nSaved passwords: {}\n\n\n".format (savedpasswords))
    input ("Enter to go back...")
    os.system("cls")
    main()



def main():
    if len(savedpasswords) > 0:
        print("\n\n\nSaved passwords {}".format(savedpasswords))
    print("\n\n\nWelcome to the password generator\n\n\n")
    input("\n\n\nPress Enter to generate a new password...\n\n\n")
    os.system("cls")
    password_generator()


main()