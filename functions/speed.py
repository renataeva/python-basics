def speed(kilometers, hours):
    return round((kilometers * 1000) / (hours * (60 * 60)), 2)
print(speed(int(input()), int(input())))