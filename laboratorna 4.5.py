def text():
    rechennya = input("Введіть текст: ")

    letters_set = set(ch for ch in rechennya if 'a' <= ch <= 'z')
    print(f"Множина літер: {sorted(letters_set)}")

    znaky = (".,!?;:-()[]\"'/")

    count = sum(1 for ch in rechennya if ch in znaky)
    print(f"Кількість розділових знаків: {count}")

text()