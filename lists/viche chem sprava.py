import random
ur = []
for _ in range(10):
    ur.append(random.randint(130, 150))
print(ur)
for i in range(len(ur) - 1):
    if ur[i] > ur[i+1]:
        print(i, ur[i])
