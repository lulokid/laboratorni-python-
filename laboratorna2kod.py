from laboratorna2 import summa
from math import tan

def expression(x):
    z = (2 * tan(x) - (x ** 0.5)) / x
    return z

x = int(input("Введіть значення x: "))
if x == 0:
    print("Помилка: x не може бути нулем.")
else:
    print("Значення виразу z =", expression(x))

x = int(input("Введіть від якого числа (x) знаходити суму усіх чисел, кратних 3: "))
y = int(input("Введіть до якого числа (y) знаходити суму усіх чисел, кратних 3: "))

while x > y:
    x = int(input("y не може бути менше x, введіть ще раз від якого числа (х) знаходити суму усіх чисел, кратних 3: "))
    y = int(input("Введіть до якого числа (y) знаходити суму усіх чисел, кратних 3: "))

print("Сума усіх чисел, кратних 3, від x до y =", summa(x, y))
