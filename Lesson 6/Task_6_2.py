X = int(input("Введите натуральное число: "))
cnt = 0
for i in range(1, X+1):
    if X % i == 0:
        cnt += 1
print(f"Количество делителий чисела {X} равно {cnt}")
