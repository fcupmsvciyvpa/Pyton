a = int(input("Введите целое число: "))
b = a % 2
print(b)

if a < 0:
    number = "Отрицательное"
else:
    number = "Положительное"

if a == 0:
    print("нулевое число")
elif b == 0:
    print(f"{number} четное число")
else:
    print(f"{number} нечетное число")