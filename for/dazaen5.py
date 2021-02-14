a = int(input())
m = []
for i in range(1, a + 1):
    print(i)
    if a % i == 0:
        m.append(i)
        print('appended:', i)
print(m)
if len(m) == 2:
    print('ПРОСТОЕ')
else:
    print(' НЕ ПРОСТОЕ')