def reversed():

    A = list(map(int,input('Введіть масив: ').split()))

    print(A)

    result = []

    reversed_A = A[::-1]

    print('Масив після запису у зворотньому порядку: ')

    print(reversed_A)

    return reversed_A

reversed()