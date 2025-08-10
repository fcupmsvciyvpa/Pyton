def fact(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

num = []
n = int(input("Введите число: "))
p = fact(n)
for tmp in range(p, 0, -1):
    num.append(fact(tmp))
print(f"Факториал числа {n} равен {num}") 