import os
import random as rd
from time import sleep

savedpasswords = []
titles_list = []


def save_file():
    file_name = input("Add your file name\n"
                      "Respone: ")
    save = open(file_name + ".txt", "w")
    save.write("\n".join(savedpasswords))
    save.close()
    print("File sucessfully created")
    sleep(2)
    os.system("cls")
    main()


def add_title_name(password):
    title = input("\n\n\nEnter your title...\n\n\n"
                  "Respuesta: ")

    while title.lower() in titles_list:
        print("A password with this name, already exists")
        print("Saved passwords: {}".format(savedpasswords))
        add_title_name(password)
    if len(title) <= 0 or title == " ":
        print("Name can not be empty")
        add_title_name(password)

    titles_list.append(title.lower())
    savedpasswords.append(title.lower() + ": " + password)
    print("\n\n\nSaved passwords: {}\n\n\n".format(savedpasswords))
    input("Enter to go back...")
    os.system("cls")
    main()

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
    add_title_name(password)



def main():
    if len(savedpasswords) > 0:
        print("\n\n\nSaved passwords {}".format(savedpasswords))
        print ("\n\n\nWelcome to the password generator\n\n\n")
        question = input ("\n\n\nPress Enter to generate a new password or (Y) to create a file...\n\n\n")
        if question == "Y":
            save_file()
        os.system("cls")
        password_generator()
        save_file()
    else:
        print("\n\n\nWelcome to the password generator\n\n\n")
        input("\n\n\nPress Enter to generate a new password...\n\n\n")
        os.system("cls")
        password_generator()

main()