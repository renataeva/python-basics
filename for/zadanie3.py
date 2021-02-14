for i in range(-5, 8, 2):
    print(i)
x = 1
summ = 0
for i in range(1,11):
    x*=i
    summ+=i
print(x, summ, sep=',')