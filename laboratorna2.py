def summa(x, y):
    sum = 0
    for i in range(x, y + 1):
        if i % 3 == 0:
            sum += i
    return sum