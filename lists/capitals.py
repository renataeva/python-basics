capitals = input().split(', ')
capitals.append(input('vvedite novoju stolicu:'))
print(*capitals)
for i in range(len(capitals)-1, -1, -1):
    if len(capitals[i]) < 5:
        del capitals[i]
print(*capitals)
