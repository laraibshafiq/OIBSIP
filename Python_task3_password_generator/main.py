import random
import os
uppercase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O','P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y','Z']
lowercase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2', '3', '4', '5', '6', '7','8','9']
symbols=['@', '$' , '#','%','&','*']
print("Welcom to password generator \n")
print(os.getcwd())
while True:
    while True:
        try:
            length=int(input("What is your desired password length: "))
            if length<8:
                print("Length should be between 8 and 50")
            else:
                break
        except:
            print("PLease enter a valid number")
    valid_options=['uppercase', 'lowercase', 'numbers', 'symbols']
    while True:
        choose=input("Which character type you want to include: uppercase, lowercase, numbers, symbols(atleast two types must be selected): ").strip().lower().split()
        valid=True
        for item in choose:
            if item not in valid_options:
                 valid=False
                 print("please enter valid input")
        if not valid:
            continue    
       
        chars=[]
        if "uppercase" in choose:
            chars+=uppercase
        if "lowercase" in choose:
            chars+=lowercase
        if "numbers" in choose:
            chars+=numbers
        if "symbols" in choose:
            chars+=symbols 

        if len(choose)<2:
            print("Atleast two types must be selected") 
            continue
        else :     
            password=random.choices(chars, k=length)
            print("Here is your password:")
            print("".join(password))
            break
    lenn=len("".join(password))
    passwordss="".join(password)
    print("Password Strength:")
    if lenn>=8 and lenn<=11:
        print ("weak")
    elif lenn>=12 and lenn<=15:
        print ("Medium")
    elif lenn>=16:
        print("Strong")
    while True:
        save=input("Do you want to save this password?(yes/no) ").lower()
        if save=="yes":
            with open("passwords.txt","a") as file:
                file.write(f"{passwordss}\n")
            print("password saved successfully")    
            break
        elif save=="no":
            print("okayy")
            break
        else: 
          print("Please enter yes/no") 


    while True:
        another=input("want to generate another password (yes/no) ").lower()
        if another=="yes":
         break
        elif another=="no":
         print("okayy")
         print("Thank you for using password generator")
         exit()
        else: 
          print("Please enter yes/no")