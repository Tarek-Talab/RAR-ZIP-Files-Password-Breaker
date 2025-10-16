#!/usr/bin/env python3

import random
import string
import time
import pyzipper
import rarfile
import os



def ana_sistem():

    def brute_force_rar(file, wordlist):

        rarfile.UNRAR_TOOL = "C:\\Program Files\\WinRAR\\unrar.exe"

        rar = rarfile.RarFile(file)

        try:
            with open(wordlist, 'r', encoding='utf-8') as file:
                passwords = file.read().splitlines()
        except FileNotFoundError:
            print("Password File Did Not Found!")
            return None

        for password in passwords:
            print(f"Trying Password : {password}")
        
            try:
                rar.extractall(pwd=password.encode('utf-8'))

                print(f"\nPassword Found: {password}\n")
                

                rar_soru ="Do you want to save the contents of the hacked file to a file,Please Type (yes,no):"
                for harf in rar_soru:
                    print(harf,end="",flush=True)
                    time.sleep(0.02)
                print()
                

                while True:
                    soru = input("--> ").strip().lower()
                    

                    if soru == "yes":

                        print("Please select a name for the file will be created:")
                        save_path = input("-->")
                        
                        rar.extractall(pwd=password.encode("utf-8"), path=save_path)
                        print("process successful")
                        break
                
                    elif soru == "no":
                        print("process successful")
                        break

                    else:
                        rar_soru_1 = "Please select one of them."
                        for harf in rar_soru_1:
                            print(harf,end="",flush=True)
                            time.sleep(0.02)
                        print()

                return password
                               
            except rarfile.BadRarFile:
                continue  
            except rarfile.RarUnknownError:
                continue  
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            
        print("Password not found.")
        return None
    

    def brute_force_zip(file,wordlist,the_file):

        fileobject = pyzipper.AESZipFile(file)

        with open(wordlist , "rb") as wordlist_file:
            for word in wordlist_file:
                
                try:
                    fileobject.pwd = word.strip()
                    fileobject.read(the_file)
                    
                except:
                    print("Trying Password:", word.decode().strip())
                    continue
                else:
                    print("\nPassword Found:",word.decode().strip())

                    zip_soru ="Do you want to save the contents of the hacked file to a file,Please Type (yes,no):"
                    for harf in zip_soru:
                        print(harf,end="",flush=True)
                        time.sleep(0.02)
                    print()

                    while True:
                        soru = input("-->").strip().lower()
                        if soru == "yes":

                            print("Please select a name for the file will be created:")
                            save_path = input("-->")
                            os.makedirs(save_path)
                            fileobject.extractall(path=save_path)
                            print("process successful")
                            break
                        elif soru == "no":
                            print("process successful")
                            break
                        else:
                            rar_soru_1 = "Please select one of them."
                            for harf in rar_soru_1:
                                print(harf,end="",flush=True)
                                time.sleep(0.02)
                            print()
                    break 

    def pass_creator(sayi,hane):

        if hane == 1:
            if sayi > 10:
                print("Max 10 Passwords can be generated")
                sayi = 10
        if hane == 2:
            if sayi > 90:
                print("Max 90 Passwords can be generated")
                sayi = 90
        if hane == 3:
            if sayi > 1000:
                print("Max 1000 Passwords can be generated")
                sayi = 1000
        if hane == 4:
            if sayi > 10000:
                print("Max 10000 Passwords can be generated")
                sayi = 10000
        if hane == 5:
            if sayi > 100000:
                print("Max 100000 Passwords can be generated")
                sayi = 100000
        if hane == 6:
            if sayi > 1000000:
                print("Max 1000000 Passwords can be generated")
                sayi = 1000000
        if hane == 7:
            if sayi > 10000000:
                print("Max 10000000 Passwords can be generated")
                sayi = 10000000
        
        
        giris = "Hello, welcome to the password creation system."
        for harf in giris:
            print(harf,end="",flush=True)
            time.sleep(0.02)
        print()
        time.sleep(1)

        for _ in range(2):
            for i in range(1,4):
                print("." * i,end="\r",flush=True)
                time.sleep(0.3)
            print(" " * 3,end="\r",flush=True)


        with open("şifre listesi.txt", "w") as dosya:
            digits = string.digits
            mevcut_sifreler = set()
            
            while len(mevcut_sifreler) < sayi:
                random_sifre = "".join(random.choice(digits) for _ in range(hane))
                if random_sifre not in mevcut_sifreler:
                    mevcut_sifreler.add(random_sifre)
                    print(f"{random_sifre}", file=dosya)
                    print(f"{len(mevcut_sifreler)} : {random_sifre}")
                    time.sleep(0.000000000001)
        print("Password Succefuly Created!")


    ana_giris = "Hello, What would you like to do:\n\n1.Password list creation\n\n2.crack zip file password\n\n3.crack rar file password"

    for harf in ana_giris:
        print(harf,end="",flush=True)
        time.sleep(0.02)
    print("\n")

    select = input("--> ")
    try:
        select = int(select)
    except ValueError:
        print("Please select one of them.")
        return ana_sistem()


    if select == 1:

        giris_2 = "How many digits of password do you want to create:"
        for harf in giris_2:
            print(harf,end="",flush=True)
            time.sleep(0.02)
        print()
    
        A = int(input("\n--> "))

        giris_3 = "How many passwords do you want to create:"
        for harf in giris_3:
            print(harf,end="",flush=True)
            time.sleep(0.02)
        print()
  
        B = int(input("--> "))

        pass_creator(B,A)

        print("see you :)")

    elif select == 2:

        print("Please move the file you want to crack to this file and enter its name: \n")
        file = input("-->")
        
        print("please write the name of the file inside the zip file: \n")
        the_file = input("-->")

        wordlist = "şifre listesi.txt"

        brute_force_zip(file,wordlist,the_file)

    elif select == 3:

        print("\nPlease move the file you want to crack to this file and enter its name: \n")
        file = input("-->")
  
        wordlist = "şifre listesi.txt"

        brute_force_rar(file,wordlist)

    else:
        print("Please select one of them.")
        return ana_sistem()

   
ana_sistem()















