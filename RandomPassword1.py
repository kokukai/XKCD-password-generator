letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

# Make an 8 letter password by combining characters from the three strings
import random

possible = [letters, caps, numbers]
password = ''

for i in range(8):
    randlist = random.choice(possible)
    password += random.choice(randlist)

print(f'Password is: {password}')