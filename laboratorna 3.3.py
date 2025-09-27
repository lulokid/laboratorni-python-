sentence = input("Введіть речення, мінімум 2 слова: ")
allwords = sentence.split() #split використав для розбиття рядка(речення)

longestword = ""
for word in allwords:
    if len(word) > len(longestword): #len використав для довжини рядка(речення)
        longestword = word

print("Найдовше слово у реченні:", longestword)