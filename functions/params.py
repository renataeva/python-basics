
def oper(a, b, op='/'):
    if op in '//+*%-':
        return eval(f'{a} {op} {b}')
    else:
        return eval(f'{op}({a}, {b})')

print(oper(21, 4, op='divmod'))

