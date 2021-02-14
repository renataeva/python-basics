num = int(input('Число: '))
units = input('Ед. измерения: ')
if 'сантиметр' == units:
    print(num * 100)
elif 'километр' == units:
    print(*divmod(num, 1000), sep='km ', end='m')
else:
    print(num)
