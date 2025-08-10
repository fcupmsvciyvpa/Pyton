n = int(input("Введите колличество чисел, n не должна быть меньше 1 и больше 100 000:  "))
t = True
if 1 <= n <= 10 ** 4:
    
    p = list(map(float, input(f"Введите {n} чисел в строчку соблюдая пробелы между строчками: ").split()))
    number = set()

    for x in range(len(p)):
        
        if p[x] <= 2 * 10 ** 9 and n == len(p):    
            
            number.add(abs(p[x]))
        else:
            t = False 
            print("Значение не удовлетворяет требованиям")
            break
    
    if t != False:
        print("Колличество различные числа",len(number))