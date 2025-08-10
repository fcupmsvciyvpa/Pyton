m = int(input("Введите максимальную массу, которую может выдержать одна лодка. \n\rЗначение должно соответствовать данному требованию 1 ≤ m ≤ 10e6)"))
n = int(input("Введите количество рыбаков. \n\rЗначение должно соответствовать данному требованию 1 ≤ n ≤ 100)"))

Ai = []
lace = 0


if 1 <= n <= 100 and 1 <= m <= 10 ** 6:

# Создаём цыкл заполнения массива, если человек равен весу лодки, тогда считаем, что 1 лодка занята
    for i in range(n):
    
        a = int(input(f"Вес человека под номером {i+1}: "))
        if a == m:
            lace += 1
        elif 1<= a <= m:
            Ai.append(a)
        else:
            print("Введенное значение не соответсвет требованиям '1 ≤ Ai ≤ m'")
            break

#проверяем каждое значение массива со всеми другими значениями этого же массива 
    for g in range(n):
        
        if Ai[g] != 0:

            recalculation = 10 ** 7
            Temporary = 0

            for v in range(n):         

#Подбираем наилучшую пару для лодки
                if g != v and  recalculation > m - Ai[v] + Ai[g] and Ai[v] != 0 and Ai[v] + Ai[g]<= m:
                    recalculation = m - Ai[v] + Ai[g]
                    Temporary = v
                    print("g цыкл = ", g ,"v цыкл = ", v,"значение v = ", Ai[v], "сумм = ", Ai[v] + Ai[g])
                    print(recalculation)
            Ai[Temporary] = 0
            Ai[g] = 0
            lace += 1
    print("Количество лодок", lace)
            
