import random
print('Your password is: ')
chars = 'qwertyuiopasdfghjklzxcvbnm0987654321;+_-=)(?/'
password = ''
for x in range(14):
    password += random.choice(chars)
print(password)
