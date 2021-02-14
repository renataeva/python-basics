import random

marbles = []
i = 1
while True:
    marbles.append('green')
    i += 1
    if i == 6:
        break
marbles.insert(random.randint(0, len(marbles) - 1), 'white')

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
Правила игры: Из мешка с пятью зелеными шариками и 
одним белым каждый игрок по очереди достает по одному 
шарику. Если достался зеленый шарик - игра идет дальше, 
если кому-нибудь из игроков достался белый, то игра 
заканчивается. Удачи!'''
print(rules)
taken = 0
current_player = 0
while taken < 6:
    print(f'\nОчередь игрока {players[current_player]}')
    input('Нажми Enter, чтобы достать шарик...')
    c = random.randint(0, len(marbles) - 1)
    if marbles[c] == 'white':
        print('________________________\nБелый шарик!')
        print(f'Игрок под именем {players[current_player]} проиграл')
        print('Игра закончена')
        break
    else:
        print('______________________\nВсе хорошо попался зеленый шарик.')
        print('Ход переходит к следуйшему игроку.')
        current_player += 1
        if current_player > len(players) - 1:
            current_player = 0
        taken += 1
        marbles.pop(c)
