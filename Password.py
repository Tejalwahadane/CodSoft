import random
import string

def gen_pass():
    try:
        length=int(input("Enter length of Password : "))
        if length<=0:
            print("Password length should be greater than 0")
            return
    except ValueError:
        print("Invalid Input")
        return
    characters = string.ascii_letters+ string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    print("Generated Password is : "+password)
    
gen_pass()
