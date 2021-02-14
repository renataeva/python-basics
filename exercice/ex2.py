pupils = int(input('Введите число школьников: '))
apples = int(input('Введите число яблок: '))

celoe, ostatok = divmod(apples, pupils)

print('Каждому: ', celoe)
print('В корзине: ', ostatok)
