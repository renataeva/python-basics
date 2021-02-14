import random
pelmeni = list(range(1, 11))87
random.shuffle(pelmeni)
print(pelmeni)
i = 0
while True:
    pelmeni[i]
    if pelmeni[i] % 5 == 0:
        print('Пелмень №', i + 1, ' счасливый.')
        break
    else:
        i = i + 1
        continue
