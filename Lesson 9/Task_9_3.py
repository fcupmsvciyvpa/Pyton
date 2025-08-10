p = list(map(float, input(f"Введите чисела в строчку соблюдая пробелы между числами: ").split()))
number = set()
for x in p:
    
    if x in number:  
        
        print("YES")

    else:
        print("NO")
        number.add(x)
    
