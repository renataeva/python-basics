def move(seq):
    seq = [*seq[2:], *seq[0:2]]
    return seq


numbers = [1, 2, 3, 4, 5]

r = move(numbers)
print(r)

assert r == [3, 4, 5, 1, 2]
