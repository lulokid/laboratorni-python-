n = int(input("Введіть n: "))

if n <= 1 or n > 9:
    print("Введіть значення n від 1 до 9")
else:
    for i in range(1, n + 1):
        print(" " * ((n * 2)-2), end="")  
        for num in range(i, 0, -1):
            print(num, end=" ")
        print()

    for i in range(n, 0, -1):
        for num in range(1, i + 1):
            print(num, end=" ")
        print()