n = int(input())
netilimau = False
for _ in range(0, n):
    a = input()
    if 'кот' in a or 'Кот' in a or 'КОТ' in a:
        netilimau = True
        print('МЯУ')
        break
if not netilimau:
    print('НЕТ')
    exit(0)
