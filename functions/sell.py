
def sell(goods, price):
    result = goods*price
    return result


goods = int(input('Goods...'))
price = int(input('Price...'))

r = sell(goods, price)
print(f'Прибыль сосставит {r} $')