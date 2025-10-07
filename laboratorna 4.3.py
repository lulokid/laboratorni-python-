def delete():

    A = list(map(int,input('Введіть масив: ').split()))

    print(A)

    result = []

    for x in range(len(A)):

        if x %2 != 0:

            result.append(x)

    print('Масив після видалення парних елементів: ')

    print(result)

    return result

delete()