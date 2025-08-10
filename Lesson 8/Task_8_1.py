n = int(input("Введите количество чисел, n не должна быть меньше 1 и больше 10 000:  "))
Entrance = []
exit = []


if 1 <= n <= 10000:
   
    for i in range(n):
        a = int(input("Значение: "))
        Entrance.append(a)
        exit.append(a)
    print("Получееные значения на входе:", *Entrance)

    for g in range(len(Entrance),0 ,-1):
        exit[g-1] = Entrance[-1*g]

    print("Выходное значение:",*exit)

else:
    print("Введено некорректное значение")