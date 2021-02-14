#  Шарлотка, солянка мидии, Шашлыки, Картошка в мундире, фондю

bluda = input().split(',')
for i in bluda:
    if i.strip()[0].isupper():
        print(i.strip())
