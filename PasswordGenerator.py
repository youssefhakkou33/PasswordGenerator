import random
import string
from os import system
import secrets

system("clear")
alphabet = string.ascii_letters + string.digits
random_string = ''.join((secrets.choice(alphabet)) for i in range(13))

print("Here is your random password: ", random_string)