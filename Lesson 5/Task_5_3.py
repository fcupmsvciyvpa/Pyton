
print("Введите пятизначное целое число")
X = int(input("Минимальная сумма инвестиций в Долларах = "))
A = int(input("Инвестиций Майкла в Долларах = "))
B = int(input("Инвестиций Иван в Долларах = "))

if A + B < X:
    print("0")
elif A >= X and B < X:
    print("Mike")
elif A < X and B >= X:
    print("Ivan")
elif A > X and B > X:
    print("2")
    print(A)
    print(B)
    print(A+B)
else:
    print("1")
