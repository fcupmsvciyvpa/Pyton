word = input("Введите слово, для проверки на обратное чтение: ")
if word.lower() == word[::-1].lower():
    print("yes")
else:
    print("no")
