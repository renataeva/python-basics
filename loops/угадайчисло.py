import random
from_num = int(input('От какого числа загадать число?'))
to_num = int(input('До какого числа загадать число?'))
if from_num > to_num:
    print('error')
    exit(1)
secret = random.randint(from_num, to_num)
guess = int()
ogranichitel = int(3)
popitki = int(1)
if secret == guess:
    print('error')
    exit(1)
while guess != secret:
    guess = int(input('Введите число'))
    if guess < secret:
        print('Секретное число больше! Попробуйте ещё раз')
    if guess > secret:
        print('Секретное число меньше! Попробуйте ещё раз')
    if popitki - ogranichitel != 0:
        print(f'Осталось {ogranichitel - popitki} попыток')
        popitki = popitki+1
    else:
        print('У Вас кончились попытки.😐 ')
        break
    if guess == secret:
        print(f'Поздравляем, вы угадали за {popitki} попытки!')
exit(0)
