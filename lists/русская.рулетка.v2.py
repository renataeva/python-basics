import random

marbles = ['white', 'blue', 'green', 'green', 'green', 'green']
random.shuffle(marbles)

players_counter = 0
while players_counter not in range(1, 4):
    players_counter = int(input('Введите число игроков (между 1 и 3): '))
players = []
i = 1
pc = players_counter
while pc != 0:
    players.append(input(f'Введите имя игрока №{i}: '))
    i+=1
    pc-=1
print(*players)

rules = '''Добро пожаловать в игру “Русская рулетка”!
Правила игры: Из мешка с четермя зелеными шариками, 
одним белым и одним синим каждый игрок по очереди достает
по одному шарику. Если достался зеленый шарик - игра идет
дальше, если кому-нибудь из игроков достался белый, то игра 
заканчивается, а если попался синий, игрок выбывает. Удачи!'''
print(rules)

taken = 0
current_player = 0
while taken < 6:
    print(f'\nОчередь игрока {players[current_player]}')
    input('Нажми Enter, чтобы достать шарик...')
    c = random.randint(0, len(marbles) - 1)
    if marbles[c] == 'white':
        print('_______________\nБелый шарик!')
        print(f'Игрок под именем {players[current_player]} проиграл')
        print('Игра закончена')
        break
    elif marbles[c] == 'blue':
        print('______________\nПопался синий шарик!')
        print(f'Игрок {players[current_player]} выбывает из игры.')
        players.pop(current_player)
    else:
        print('_______________\nВсе хорошо попался зеленый шарик.')
        print('Ход переходит к следуйшему игроку.')
        current_player += 1
        if current_player > len(players) - 1:
            current_player = 0
        taken += 1
        marbles.pop(c)
