def smallest(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c

assert smallest(1, 2, 3) == 1
assert smallest(2, 1, 3) == 1
assert smallest(3, 2, 1) == 1
