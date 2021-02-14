string = input('Введите 3 слова: ')
a = string.find(' ', 0, -1)
first = string[0:a]
b = string.rfind(' ', a+1, )
second = string[a+1:b]
last = string[b+1:]
a = first.count('a')
if 'a' not in second:
    print('error')
    exit(1)
else:
    b = second.replace('a', 'A')
c = len(last)
print(a, b, c ,sep=',')
