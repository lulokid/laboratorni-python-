# З'ясувати, чи вірно, що в заданому слові є усі букви, що входять в запропоноване користувачем слово.
word1 = input("Введіть задане слово: ")
userword = input("Введіть запропоноване слово: ")

indexs = 0
length = len(userword)
spivpadinnya = True

while indexs < length:
    litera = userword[indexs]
    if litera not in word1:
        spivpadinnya = False
    indexs += 1
if spivpadinnya:
    print("Усі букви запропонованого слова входять у задане слово.")
else:
    print("Лише деякі букви або жодна буква запропонованого слова не входять у задане слово.")