import random as rnd
import string

password = []

print('welcome to this awesome password generator' '\n' 'follow the instructions to create a strong password')
chars = True
while chars:
    try:
        letters = int(input('how many letters do you want for your password? [a-z] '))
        chars = False
    except ValueError: 
        print('not an int')
        continue
digi = True
while digi:
    try:
        digits = int(input('how many digits do you want for your password? [0-9] '))
        digi = False
    except ValueError: 
        print('not an int')
        continue
symb = True
while symb:
    try:
        symbols = int(input('how many special symbols do you want for your password? [!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~] '))
        symb = False
    except ValueError: 
        print('not an int')
        continue

while True:
    capital = str(input('do you want capital letters?(y/n)')).lower()
    if capital == 'y':
        for i in range(letters):
            let = rnd.choice(string.ascii_letters)
            password.append(let)
        for j in range(digits):
            dig = rnd.choice(string.digits)
            password.append(dig)
        for k in range(symbols):
            sym = rnd.choice(string.punctuation)
            password.append(sym)
        break
    elif capital == 'n':
        for i in range(letters):
            let = rnd.choice(string.ascii_lowercase)
            password.append(let)
        for j in range(digits):
            dig = rnd.choice(string.digits)
            password.append(dig)
        for k in range(symbols):
            sym = rnd.choice(string.punctuation)
            password.append(sym)
        break
    else:
        print('wrong input')
        continue

print('The randomly created password is: ')
print(''.join(password))