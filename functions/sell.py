
def sell(goods, price):
    return goods*price

goods = int(input('Goods...'))
price = int(input('Price...'))

r = sell(goods, price)
print(f'Прибыль составит {r} $')