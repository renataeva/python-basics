n = 13
if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
    print('2, 3 и 5')
elif n % 2 == 0 and n % 3 == 0:
    print('2 и 3')
elif n % 2 == 0:
    print('2')
elif n % 2 != 0:
    print('0')
