num = [int(i) for i in input().split()]
print('Список случайных чисел: ', num)
print('Максимальное число из списка: ', max(num))
print('Минимальное число из списка: ', min(num))
a = int(max(num))
b = int(min(num))
print('Разница между минималиным и максимальным: ', a - b)
