# To write a password manager that will generate new password for user 
# create a function password manager
# receive length of password
# receive how many letters
# receive how many numbers
# generate new password with random characters to include special characters
# return generated password


import random
import string

print("Hi, generate a new password!\n\nChoose how long you want it to be (cannot be less than six characters).\
      \nChoose how many letters and numbers you want included, special chracters will make up the rest.")
      
user_length = int(input("How long do you want your password to be? (*Minimum of 6 characters): "))
while user_length < 6:
    print("Password length has to be a minimum of six (6) characters")
    user_length = int(input("How long do you want your password to be? (*Minimum of 6 characters): "))

letters = int(input("How many letters do you want?: "))
nos = int(input("How many numbers do you want?: "))

def PasswordManager(user_length):
    password = []
    for i in range(letters):
        password.append(string.ascii_letters)
      
    for i in range(nos):
        password.append(string.digits)
    special_chr = ('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')    
    while len(password) < user_length:
        password.append(special_chr)
    random.shuffle(password)
    return ''.join(random.choice(p) for p in password)

print("Your password is", PasswordManager(user_length))
