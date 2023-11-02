import random

print('Your password: ')

chars = "abcdefghijklmnopqrstuvwxyz1234567890%^&*@£$"

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)

