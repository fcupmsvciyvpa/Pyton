# Задание №2

# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.


line = input("Введите строку с разным количеством символов и пробелов, для чистки от лишних пробелов: ")
txt = []
for char in line:
    if char != ' ':
        txt.append(char)
        prev_is_space = False
    elif not prev_is_space:
        txt.append(char)
        prev_is_space = True  


print("".join(txt))