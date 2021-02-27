fruits = ['pineapple', 'lemon', 'pear', 'watermelon', 'tomato', 'apple']
first, second, *middle, firstlast, last = fruits
print(f'''Первый элемент: {first}
Второй: {second}
Посередине: {middle}
Предпоследний: {firstlast}
Последний: {last}''')
