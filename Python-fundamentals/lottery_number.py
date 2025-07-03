import random

pwd_len = int(input(f"Enter password length"))

def Password_Generator(pwd_len):
    i=1
    results =""
    while i<=pwd_len:
        number = str(random.randint(0,9))
        results+= number
        i+=1
    return results

print(Password_Generator(pwd_len))
