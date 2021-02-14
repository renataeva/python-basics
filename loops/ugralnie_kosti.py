import random

while True:
    ans = int(input('Играем? '))
    if ans == 1:
        c1 = random.randint(1, 6)
        c2 = random.randint(1, 6)
        print(f'Pervyj kubik: {c1}\nVtorj kubik: {c2}')
    elif ans == 0:
        break
    else:
        print('Poprobyjte ewe raz.')
