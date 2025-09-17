a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

while a < 0 or b <= 0:
    print("Числа мають бути додатними")
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))

if a > b:
    c = (a / b) + 31
elif a == b:
    c = -25
else:
    c = (a - 5) / b

print("Результат обчислень =", c)