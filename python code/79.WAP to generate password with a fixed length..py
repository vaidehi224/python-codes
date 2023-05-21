import random
import string
def generate_password(length):
    """Generate a random password with the given length"""
    # define the set of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation 
    # generate the password
    password = " "
    for i in range(length):
        password += random.choice(chars) 
    return password
# get the desired length from the user
length = int(input("Enter the length of the password: "))
# generate the password and print it
password = generate_password(length)
print("Your password is:", password)
