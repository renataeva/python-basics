n = int(input('Введите трехзначное число: '))
sot, desed = divmod(n, 100)
des, ed = divmod(desed, 10)
print(sot + des + ed)
